from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import asyncio
from time import time
import random
from data.topics import cpp_topics
from data.theory_cpp import theory_cpp
from handlers.theory import show_lesson_menu, show_lesson
from handlers.exercises import start_practice, send_question
from handlers.search import search_entry, handle_search_pagination
from db.models.user import User
from db.database import SessionLocal
from db.models.attempt import Attempt
from sqlalchemy import func, Integer
from db.models.exercise import Exercise
from db.models.topic import Topic
from handlers.code import code_help_text
from telegram.error import BadRequest
from db.models.suggestion import Suggestion
from bot.config import ADMIN_CHAT_ID
from sqlalchemy.exc import SQLAlchemyError
from html import escape
import json
import re
from html import escape as h
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

try:
    from handlers.code import CODE_KEY
except Exception:
    CODE_KEY = "last_code"


#constant exam
EXAM_NUM_TEST = 10
EXAM_NUM_CODE = 5
EXAM_POINTS_TEST_EACH = 0.5   # 10*0.5=5 5 points of test but 10 test's questions
EXAM_POINTS_CODE_EACH = 1.0   # 5 points of programming

GREETINGS = ["hola", "ola", "buenas", "hey", "holi", "hello", "saludos", "qué tal", "start"]

LETTERS_ES = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Helpers for code mode
def _pick_next_code_exercise(session, user_id: int, topic_name: str, exclude_ids: set[int] | tuple[int, ...] = ()):
    topic = session.query(Topic).filter(Topic.name == topic_name).one_or_none()
    if not topic:
        return None

    exercises = (
        session.query(Exercise)
        .filter(Exercise.topic_id == topic.id, Exercise.type == "code")
        .all()
    )
    random.shuffle(exercises)
    if not exercises:
        return None

    exclude_ids = set(exclude_ids or ())

    # Prefer no resolved and no excluded
    for ex in exercises:
        if ex.id in exclude_ids:
            continue
        ok = (
            session.query(Attempt)
            .filter(Attempt.user_id == user_id, Attempt.exercise_id == ex.id, Attempt.is_correct.is_(True))
            .first()
        )
        if not ok:
            return ex

    # if are all resolved, everyone is not excluded
    for ex in exercises:
        if ex.id not in exclude_ids:
            return ex

    # Fallback, if there is only one and it is excluded, returns that
    return exercises[0]


def _pre(s: str) -> str:
    # Render sure for blocks monospaces
    return f"<pre><code>{h(s)}</code></pre>"

async def _send_code_prompt(query_or_update, context, ex: Exercise):
    """
    Send a concise prompt for the selected code exercise:
    - title/question
    - sample input/output (first sample)
    - limits + short instructions
    - inline buttons: ℹ️ Ayuda, 🔁 Siguiente, ⬅ Volver
    """
    #Sample (no strip: preserve significant spaces) 
    sample_io = ""
    if ex.tests_json and isinstance(ex.tests_json, dict):
        samples = (ex.tests_json or {}).get("sample", []) or []
        if samples:
            s = samples[0]
            inp = (s.get("input") or "")
            out = (s.get("output") or "")
            sample_io = (
                "<b>Ejemplo (sample)</b>\n"
                "<b>Entrada:</b>\n" + _pre(inp) + "\n"
                "<b>Salida esperada:</b>\n" + _pre(out)
            )

    #limits
    limits = []
    if getattr(ex, "time_limit_ms", None):
        limits.append(f"{ex.time_limit_ms} ms")
    if getattr(ex, "memory_limit_mb", None):
        limits.append(f"{ex.memory_limit_mb} MB")
    limits_str = " · ".join(limits) if limits else "1.5 s · 128 MB"

    # Main text (all except <pre><code> blocks)
    enunciado = h(getattr(ex, "question", ""))
    # pista_html = ""
    # if include_hint and getattr(ex, "hint", None):
    #     pista_html = f"\n<b>Pista:</b> {h(ex.hint)}"

    text = (
        "<b>💻 Ejercicio de programación</b>\n\n"
        f"<b>Enunciado:</b> {enunciado}"
        # f"{pista_html}\n\n"
        f"{sample_io}\n\n"
        f"<b>Límites:</b> {h(limits_str)}\n\n"
        "Envía tu solución en un bloque (triple comilla invertida) o pega tu código directamente:\n"
        + _pre("cpp\n// tu código aquí\n") +
        "\nUsa /out (salida tal cual), /run (sample) o /submit (tests completos).\n"
        "Opcional: /hint y /solution."
    )

    #  Inline keyboard 
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("ℹ️ Ayuda", callback_data="code_help")],
        [
            InlineKeyboardButton("🔁 Siguiente enunciado", callback_data="repeat_mode"),
            InlineKeyboardButton("⬅ Volver al menú de práctica", callback_data="back_to_mode"),
        ]
    ])

    # Edit if you can; if not, reply with a new message 
    try:
        if hasattr(query_or_update, "message") and query_or_update.message:
            await query_or_update.message.edit_text(
                text, parse_mode=ParseMode.HTML, reply_markup=kb, disable_web_page_preview=True
            )
        else:
            await query_or_update.callback_query.message.edit_text(
                text, parse_mode=ParseMode.HTML, reply_markup=kb, disable_web_page_preview=True
            )
    except BadRequest as e:
        # If the content matches and Telegram does not want to edit, we send a new message.
        if "Message is not modified" in str(e):
            if hasattr(query_or_update, "message") and query_or_update.message:
                await query_or_update.message.reply_text(
                    text, parse_mode=ParseMode.HTML, reply_markup=kb, disable_web_page_preview=True
                )
            else:
                await query_or_update.callback_query.message.reply_text(
                    text, parse_mode=ParseMode.HTML, reply_markup=kb, disable_web_page_preview=True
                )
        else:
            # If it fails for any other reason, propagate it. 
            raise

#for cleaning the keyborad
async def remove_persistent_keyboard(update):
    """Remove legacy keyboards from ReplyKeyboard, avoiding BadRequest due to empty text."""
    try:
        await update.message.reply_text("👋", reply_markup=ReplyKeyboardRemove())
    except BadRequest:
        await update.message.reply_text("Teclado actualizado.", reply_markup=ReplyKeyboardRemove())


# ------------------------------------------------------------------------------
# Function to show the main menu
async def show_main_menu(update, context):

    if update.message:
        target_msg = update.message
    else:
        await update.callback_query.answer()
        target_msg = update.callback_query.message

    buttons = [
        [InlineKeyboardButton("📚 Aprender", callback_data="learn")],
        [InlineKeyboardButton("📝 Practicar", callback_data="practice")], 
        [InlineKeyboardButton("💡 Sugerencias", callback_data="suggest")], 
        [InlineKeyboardButton("🔎 Buscar concepto", callback_data="search_start")],
        [InlineKeyboardButton("🧪 Examen por tema", callback_data="exam_by_topic")],
        [InlineKeyboardButton("🏁 Examen final", callback_data="exam_final")]
    ]
    await target_msg.reply_text(
        "¿Qué quieres hacer?",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# Function to start the bot and check user registration
async def start(update, context):
    clear_practice_state(context)
    telegram_id = update.effective_user.id
    username = update.effective_user.username
    first_name = update.effective_user.first_name
    await remove_persistent_keyboard(update)

    with SessionLocal() as session:
        user = session.query(User).filter_by(telegram_id=telegram_id).first()

        if user:
            context.user_data["user_id"] = user.id
            await update.message.reply_text(
                f"¡Hola de nuevo, {user.name}!\nTu identificador único es <b>{user.id}</b>.",
                parse_mode="HTML", 
                reply_markup=ReplyKeyboardRemove()
            )
            await show_main_menu(update, context)
        else:
            context.user_data["pending_registration"] = {
                "telegram_id": telegram_id,
                "username": username
            }
            await update.message.reply_text(
                "👋 ¡Bienvenido/a al chatbot educativo de programación en C++!\n\n"
                "📌 Aquí podrás:\n"
                "• Aprender teoría paso a paso.\n"
                "• Practicar ejercicios interactivos con corrección al instante.\n"
                "• Hacer tests de autoevaluación y exámenes.\n\n"
                "⚙️ Comandos principales:\n"
                "• /start – Iniciar el bot. Si notas que el bot está fallando vuelve a introducir /start. \n"
                "• /menu – Volver al menú principal.\n"
                "• /help – Ayuda sobre cómo usar el bot.\n\n"
                "Por lo demás, te puedes mover libremente con los botones.\n\n"
                "🔒 Nota: el bot guardará tu número de usuario de Telegram y tu nombre "
                "para poder gestionar tu progreso y personalizar tu experiencia.\n\n"
                "Por favor, dime tu nombre para poder dirigirme a ti:",
                parse_mode="HTML",
                reply_markup=ReplyKeyboardRemove()
            )

# Function to handle text messages
async def handle_text(update, context):

    #Capture code during exam (phase code)
    exam_state = context.user_data.get("exam")
    if exam_state and exam_state.get("active") and exam_state.get("phase") == "code":
        raw = update.message.text or ""
        code = _extract_code_block(raw)
        if code:
            # store code where cmd_submit will read it
            context.user_data[CODE_KEY] = code
            context.user_data["exam_have_code"] = True
            # show Enviar / Reintentar buttons
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ Enviar", callback_data="exam_submit_code"),
                InlineKeyboardButton("🔁 Reintentar", callback_data="exam_retry_code")]
            ])
            await update.message.reply_text("✅ Código recibido.", reply_markup=kb)
        else:
            await update.message.reply_text(
                "✍️ Envía tu solución como texto (no hace falta ```cpp```).\nCuando la reciba, te pondré los botones *Enviar* y *Reintentar*.",
                parse_mode="Markdown"
            )
        return

    #Capture code in normal 'programar' mode too
    if context.user_data.get("awaiting_code"):
        raw = update.message.text or ""
        code = _extract_code_block(raw)
        if code:
            context.user_data[CODE_KEY] = code
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ Enviar (/submit)", callback_data="code_submit_cb"),
                InlineKeyboardButton("🔁 Reintentar", callback_data="code_retry_cb")]
            ])
            await update.message.reply_text("✅ Código recibido.", reply_markup=kb)
        else:
            await update.message.reply_text(
                "✍️ Envía tu solución como texto (no hace falta ```cpp```)."
                "Cuando la reciba, verás los botones *Enviar* y *Reintentar*.",
                parse_mode="Markdown"
            )
        return

    if "pending_registration" in context.user_data:
        info = context.user_data.pop("pending_registration")
        name = update.message.text.strip()

        with SessionLocal() as session:
            try:
                new_user = User(
                    telegram_id=info["telegram_id"],
                    username=info["username"],
                    name=name
                )
                session.add(new_user)
                session.commit()
                session.refresh(new_user)
            except SQLAlchemyError:
                session.rollback()
                await update.message.reply_text(
                    "❌ Ha ocurrido un error registrándote. Inténtalo de nuevo en unos segundos."
                )
                return


        context.user_data["user_id"] = new_user.id

        await update.message.reply_text(
            f"✅ ¡Gracias, {name}!\nTe he registrado correctamente. Tu identificador único es <b>{new_user.id}</b>.",
            parse_mode="HTML"
        )
        await show_main_menu(update, context)
        return

    elif context.user_data.get("awaiting_suggestion"):
        text = (update.message.text or "").strip()
        if not text:
            await update.message.reply_text("❌ El mensaje está vacío. Escribe tu sugerencia o pulsa cancelar.")
            return
        if len(text) > 1000:
            await update.message.reply_text("⚠️ Intenta resumir (máx. 1000 caracteres).")
            return

        # Anti-spam 30s between suggestion
        now = time()
        last = context.user_data.get("last_suggestion_ts", 0)
        if now - last < 30:
            await update.message.reply_text("⏳ Demasiado rápido. Espera unos segundos y vuelve a intentarlo.")
            return

        user_id = context.user_data.get("user_id")
        tg = update.effective_user

        # save in the db
        try:
            with SessionLocal() as session:
                sug = Suggestion(user_id=user_id, text=text)  # user_id puede ser None si no registrado
                session.add(sug)
                session.commit()
        except Exception:
            pass

        # sending to the admin
        try:
            admin_text = (
                "📥 *Nueva sugerencia*\n\n"
                f"👤 Usuario: {tg.username or tg.full_name} (id {tg.id})\n"
                f"🆔 Interno: {user_id or '—'}\n"
                f"💬 Texto:\n{text}"
            )
            if ADMIN_CHAT_ID:
                await context.bot.send_message(
                    chat_id=ADMIN_CHAT_ID,
                    text=admin_text,
                    parse_mode="Markdown"
                )
        except Exception:
            pass

        context.user_data["awaiting_suggestion"] = False
        context.user_data["last_suggestion_ts"] = now

        await update.message.reply_text(
            "✅ ¡Gracias por tu sugerencia! La hemos recibido.",
        )
        await show_main_menu(update, context)
        return
    else:
        text = update.message.text.lower().strip()
        if text in GREETINGS:
            await start(update, context)
        else:
            await update.message.reply_text("Usa los botones o /start para comenzar.")

# Function to handle callback queries
async def handle_callback(update, context):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data == "search_start":
        clear_practice_state(context)
        context.user_data.pop("exam", None)
        context.user_data.pop("awaiting_suggestion", None)
        return await search_entry(update, context)

    elif data in ("search_next", "search_prev"):
        return await handle_search_pagination(update, context)
    
    if data == "suggest":
        clear_practice_state(context)
        context.user_data.pop("search_active", None)
        context.user_data["awaiting_suggestion"] = True

        # prevent practice/test state from hijacking the next text
        for k in ("current_topic", "current_mode", "current_exercise", "current_options", "awaiting_code"):
            context.user_data.pop(k, None)

        # context.user_data["awaiting_suggestion"] = True
        await query.message.edit_text(
            "📝 *Envíame tu sugerencia ahora mismo*\n\n"
            "Puedes contarnos ideas, fallos, mejoras… (máx. 1000 caracteres).\n\n"
            "_Cuando la envíes, te confirmaré la recepción._",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅ Cancelar", callback_data="main_menu")]])
        )

    elif data == "exam_retry_code":
        # borrar código y pedirlo de nuevo
        context.user_data.pop(CODE_KEY, None)
        context.user_data["awaiting_code"] = True
        await query.message.reply_text("🔁 Reintenta: pega de nuevo tu solución para este ejercicio.")
        return

    elif data == "exam_submit_code":
        # no enviar si no hay código aún
        if CODE_KEY not in context.user_data:
            await query.answer("Pega tu código primero.", show_alert=True)
            return

        await query.message.reply_text("📨 Enviando y corrigiendo...")

        from handlers.code import cmd_submit
        await cmd_submit(update, context)  # imprime AC/WA

        # Puntuar y avanzar
        exam = context.user_data.get("exam", {})
        user_id = context.user_data.get("user_id")
        ex_id = context.user_data.get("current_exercise_id")

        got_point = False
        if user_id and ex_id:
            with SessionLocal() as session:
                ok = (session.query(Attempt)
                    .filter(Attempt.user_id == user_id, Attempt.exercise_id == ex_id, Attempt.is_correct.is_(True))
                    .order_by(Attempt.id.desc())
                    .first())
                if ok:
                    got_point = True

        if ex_id:
            exam["answers"].append((ex_id, bool(got_point), "code"))
        if got_point:
            exam["score_code"] = exam.get("score_code", 0.0) + EXAM_POINTS_CODE_EACH

        # after updating score and clearing CODE_KEY
        exam["i_code"] += 1
        context.user_data.pop(CODE_KEY, None)
        context.user_data.pop("last_code", None)
        context.user_data["awaiting_code"] = True

        # send confirmation
        await query.message.reply_text("✅ Solución enviada. Cargando el siguiente ejercicio…")

        # force sending of the following statement as a new message
        from telegram import Update
        fake_update = Update(update.update_id, callback_query=query)
        await _exam_send_current(fake_update, context)

    #for programming outside the exam
    elif data == "code_retry_cb":
        context.user_data.pop(CODE_KEY, None)
        await query.message.reply_text("🔁 Reintenta: pega de nuevo tu solución.")
        return

    elif data == "code_submit_cb":
        if not context.user_data.get(CODE_KEY):
            await query.answer("Pega tu código primero.", show_alert=True)
            return
        from handlers.code import cmd_submit
        await cmd_submit(update, context)
        return
    

    elif data == "exam_by_topic":
        #choose topic
        buttons = [
            [InlineKeyboardButton(topic, callback_data=f"exam_topic_{i}")]
            for i, topic in enumerate(cpp_topics)
        ]
        buttons.append([InlineKeyboardButton("⬅ Volver", callback_data="main_menu")])
        await query.message.edit_text(
            "Elige un tema para el examen:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data.startswith("exam_topic_"):
        index = int(data.split("_")[2])
        topic_name = cpp_topics[index]
        # make an exam only with this topic
        with SessionLocal() as session:
            t = session.query(Topic).filter(Topic.name == topic_name).one_or_none()
            if not t:
                await query.message.edit_text("⚠️ Tema no encontrado.")
                return
            test_ids, code_ids = _build_exam_sets(session, topic_id=t.id)

        if not test_ids and not code_ids:
            await query.message.edit_text("⚠️ No hay contenido para examen en este tema.")
            return

        _exam_bootstrap_state(context, scope="topic", topic=topic_name, test_ids=test_ids, code_ids=code_ids)
        await _exam_send_current(update, context)

    elif data == "exam_final":
        # make an exam with all the topics
        with SessionLocal() as session:
            test_ids, code_ids = _build_exam_sets(session, topic_id=None)  # None=global

        if not test_ids and not code_ids:
            await query.message.edit_text("⚠️ No hay contenido suficiente para el examen final.")
            return

        _exam_bootstrap_state(context, scope="final", topic="Todos los temas", test_ids=test_ids, code_ids=code_ids)
        await query.message.edit_text(
            "🏁 <b>Examen final</b> iniciado.\n\nSe evaluarán 10 preguntas tipo test y 5 ejercicios de programación.",
            parse_mode="HTML"
        )
        await _exam_send_current(update, context)

    elif data.startswith("exam_answer_"):
        if not context.user_data.get("exam", {}).get("active"):
            await query.answer("No hay examen en curso", show_alert=True)
            return

        exam = context.user_data["exam"]
        idx_opt = int(data.split("_")[2])

        i = exam["i_test"]
        ex_id = exam["test_ids"][i] if i < len(exam["test_ids"]) else None

        # options saved in the state by _exam_send_current
        opts = exam.get("current_test_options", [])
        corr_idx = exam.get("current_test_correct_idx")
        corr_txt = exam.get("current_test_correct_text") 

        # selected option
        selected = opts[idx_opt] if 0 <= idx_opt < len(opts) else None

        # validate by index or by text
        is_correct = False
        if corr_idx is not None:
            is_correct = (idx_opt == corr_idx)
        elif corr_txt is not None and selected is not None:
            is_correct = (selected == corr_txt)

        if is_correct:
            exam["score_test"] += EXAM_POINTS_TEST_EACH
        if ex_id:
            exam["answers"].append((ex_id, bool(is_correct), "test"))

        # move forward and clear temporary status
        exam["i_test"] += 1
        exam.pop("current_test_options", None)
        exam.pop("current_test_correct_idx", None)
        exam.pop("current_test_correct_text", None)

        await _exam_send_current(update, context)

    elif data == "exam_cancel":
        context.user_data.pop("exam", None)
        await query.message.edit_text("Examen cancelado.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅ Volver", callback_data="main_menu")]
        ]))

    
    elif data.startswith("sug_page:"):
        #only admin
        if not _is_admin(update):
            await query.answer("Solo admin", show_alert=True)
            return
        _, flt, page = data.split(":")
        await _send_suggestions_page(update, context, flt, int(page), via_callback=True)

    elif data.startswith("sug_filter:"):
        if not _is_admin(update):
            await query.answer("Solo admin", show_alert=True)
            return
        _, flt, page = data.split(":")
        await _send_suggestions_page(update, context, flt, int(page), via_callback=True)

    elif data.startswith("sug_toggle:"):
        if not _is_admin(update):
            await query.answer("Solo admin", show_alert=True)
            return
        # format: sug_toggle:<id>:<new_state>:<flt>:<page>
        try:
            _, sid, new_state, flt, page = data.split(":")
            sid = int(sid)
            to_resolved = (new_state == "1")
            with SessionLocal() as session:
                sug = session.query(Suggestion).filter(Suggestion.id == sid).one_or_none()
                if not sug:
                    await query.answer("No existe", show_alert=True)
                else:
                    sug.resolved = to_resolved
                    session.commit()
                    await query.answer("Actualizado", show_alert=False)
            # refresh the same page
            await _send_suggestions_page(update, context, flt, int(page), via_callback=True)
        except Exception:
            await query.answer("Error actualizando", show_alert=True)


    elif data == "learn":
        clear_practice_state(context)
        buttons = [
            [InlineKeyboardButton(topic, callback_data=f"theory_{i}")]
            for i, topic in enumerate(cpp_topics)
        ]
        buttons.append([InlineKeyboardButton("⬅ Volver", callback_data="main_menu")])
    
        await query.message.edit_text(
            "Elige un tema de C++ para aprender:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data == "practice":
        buttons = [
            [InlineKeyboardButton(topic, callback_data=f"topic_{i}")]
            for i, topic in enumerate(cpp_topics)
        ]
        buttons.append([InlineKeyboardButton("📊 Ver estadísticas", callback_data="view_stats")])
        buttons.append([InlineKeyboardButton("⬅ Volver", callback_data="main_menu")])
        await query.message.edit_text(
            "Elige un tema para practicar:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data == "back_to_mode":
        topic = context.user_data.get("current_topic")
        if not topic:
            await query.message.reply_text("⚠️ No hay tema activo. Usa /start.")
            return

        buttons = [
            [InlineKeyboardButton("📝 Test", callback_data="mode_test")],
            [InlineKeyboardButton("💻 Programar", callback_data="mode_code")],
            [InlineKeyboardButton("⬅ Volver al menú", callback_data="main_menu")]
        ]

        await query.message.reply_text(
            f"Has elegido <b>{topic}</b>.\n\n¿Qué tipo de ejercicio quieres hacer?",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="HTML"
        )

    elif data.startswith("theory_"):
        index = int(data.split("_")[1])
        topic = cpp_topics[index]
        await show_lesson_menu(update, context, topic_key=topic)

    elif data.startswith("topic_"):
        index = int(data.split("_")[1])
        topic = cpp_topics[index]
        context.user_data["selected_topic"] = topic

        buttons = [
            [InlineKeyboardButton("📝 Test", callback_data="mode_test")],
            [InlineKeyboardButton("💻 Programar", callback_data="mode_code")],
            [InlineKeyboardButton("⬅ Volver a temas", callback_data="back_to_topics")]
        ]
        await query.message.edit_text(
            f"Has elegido <b>{topic}</b>.\n\n¿Qué tipo de ejercicio quieres hacer:",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="HTML"
        )
    elif data == "back_to_topics":
        buttons = [
            [InlineKeyboardButton(topic, callback_data=f"topic_{i}")]
            for i, topic in enumerate(cpp_topics)
        ]
        buttons.append([InlineKeyboardButton("📊 Ver estadísticas", callback_data="view_stats")])
        buttons.append([InlineKeyboardButton("⬅ Volver", callback_data="main_menu")])

        await query.message.edit_text(
            "Elige un tema para practicar:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data == "back_to_theory_topics":
        buttons = [
            [InlineKeyboardButton(topic, callback_data=f"theory_{i}")]
            for i, topic in enumerate(cpp_topics)
        ]
        buttons.append([InlineKeyboardButton("⬅ Volver", callback_data="main_menu")])

        await query.message.edit_text(
            "Elige un tema de C++ para aprender:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data.startswith("back_to_lessons:"):
        topic_key = data.split(":", 1)[1]
        # Return to the list of lessons on this topic
        await show_lesson_menu(update, context, topic_key=topic_key)

    elif data.startswith("back_to_lessons_idx:"):
        idx = int(data.split(":", 1)[1])
        topic_key = cpp_topics[idx]
        await show_lesson_menu(update, context, topic_key=topic_key)

    elif data.startswith("mode_"):
        mode = data.split("_")[1]
        topic = context.user_data.get("selected_topic")

        if not topic:
            await query.message.edit_text("⚠️ Ocurrió un error. Por favor, vuelve a /start.")
            return

        # Store current topic & mode for the session
        context.user_data["current_topic"] = topic
        context.user_data["current_mode"] = mode

        if mode == "code":
            # pick and present a code exercise now
            user_id = context.user_data.get("user_id")
            if not user_id:
                await query.message.edit_text("⚠️ Debes registrarte primero con /start.")
                return
            
            context.user_data["served_code_ids"] = set()

            with SessionLocal() as session:
                ex = _pick_next_code_exercise(session, user_id, topic)
                if not ex:
                    await query.message.edit_text("⚠️ No hay ejercicios de programación en este tema (aún).")
                    return
                # Keep state for code-mode handlers
                context.user_data["current_exercise_id"] = ex.id
                context.user_data["awaiting_code"] = True
                context.user_data.pop("last_code", None)

            context.user_data["served_code_ids"].add(ex.id)

            await _send_code_prompt(update, context, ex)
        else:
            # Default -> multiple-choice practice flow
            await start_practice(update, context)

    elif data.startswith("resp_"):
        option_index = int(data[5:])
        options = context.user_data["current_options"]
        selected = options[option_index]
        exercise = context.user_data["current_exercise"]

        if exercise.is_correct(selected):
            response = f"<b>{exercise.question}</b>\n\n✅ ¡Correcto!"
        else:
            response = (
                f"<b>{exercise.question}</b>\n\n"
                f"❌ <b>Incorrecto</b>\n\n"
                f"<b>Explicación:</b> {exercise.explanation}"
            )

        user_id = context.user_data.get("user_id")

        # save attempt (multiple-choice)
        from db.models.exercise import Exercise as ExerciseModel
        with SessionLocal() as session:
            db_ex = session.query(ExerciseModel).filter_by(question=exercise.question).first()
            if db_ex:
                session.add(Attempt(
                    user_id=user_id,
                    exercise_id=db_ex.id,
                    is_correct=exercise.is_correct(selected)
                ))
                session.commit()

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response,
            parse_mode="HTML"
        )

        # continue with next question
        await asyncio.sleep(0.5)
        await send_question(update, context)

    elif data == "repeat_mode":
        # When user wants more practice in the same mode
        if context.user_data.get("current_mode") == "code":
            topic = context.user_data.get("current_topic")
            user_id = context.user_data.get("user_id")
            served = context.user_data.setdefault("served_code_ids", set())
            exclude = set(served)
            cur_id = context.user_data.get("current_exercise_id")
            if cur_id:
                exclude.add(cur_id)
            if not topic or not user_id:
                await query.message.reply_text("⚠️ Ocurrió un error. Usa /start.")
                return
            with SessionLocal() as session:
                ex = _pick_next_code_exercise(session, user_id, topic)
                if not ex:
                    await query.message.reply_text("⚠️ No hay más ejercicios de programación en este tema.")
                    return
                context.user_data["current_exercise_id"] = ex.id
                context.user_data["awaiting_code"] = True
                served.add(ex.id) 
                context.user_data.pop("last_code", None)
            await _send_code_prompt(update, context, ex)
        else:
            await start_practice(update, context)

    elif data == "choose_mode":
        topic = context.user_data.get("current_topic")
        if not topic:
            await query.message.edit_text("Ocurrió un error. Usa /start para volver al menú.")
            return

        # Search index for current topic
        try:
            idx = cpp_topics.index(topic)
        except ValueError:
            idx = 0  #fallback

        buttons = [
            [InlineKeyboardButton("📝 Test", callback_data="mode_test")],
            [InlineKeyboardButton("💻 Programar", callback_data="mode_code")],
            [InlineKeyboardButton("⬅ Volver a temas", callback_data="back_to_topics")]
        ]

        await query.message.edit_text(
            f"Has elegido <b>{topic}</b>.\n\n¿Qué tipo de ejercicio quieres hacer?",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="HTML"
        )


    elif data.startswith("lesson_"):
        await show_lesson(update, context)

    elif data.startswith("menu_topic_"):
        topic_key = data.replace("menu_topic_", "")
        await show_lesson_menu(update, context, topic_key)

    elif data == "main_menu":
        clear_practice_state(context)
        await show_main_menu(update, context)
    
    elif data == "code_help":
        await query.message.reply_text(code_help_text(short=False), parse_mode="Markdown")


    # View statistics
    elif data == "view_stats":
        user_id = context.user_data.get("user_id")
        if not user_id:
            await query.message.reply_text("❌ No estás registrado. Usa /start.")
            return

        # Fetch statistics from the database
        with SessionLocal() as session:
            rows = session.query(
                Topic.name.label("topic"),
                Exercise.type,
                func.count().label("total"),
                func.sum(func.cast(Attempt.is_correct, Integer)).label("aciertos")
            ).join(Exercise, Attempt.exercise_id == Exercise.id
            ).join(Topic, Topic.id == Exercise.topic_id
            ).filter(Attempt.user_id == user_id
            ).group_by(Topic.name, Exercise.type
            ).all()

        stats = {}
        for topic_name, tipo, total, aciertos in rows:
            ratio = (aciertos or 0) / total if total > 0 else 0
            stats.setdefault(topic_name, {})
            stats[topic_name][tipo] = {
                "aciertos": aciertos or 0,
                "fallos": total - (aciertos or 0),
                "ratio": round(ratio * 100),
            }

        if not stats:
            await query.message.reply_text("⚠️ Aún no hay estadísticas registradas.")
            return

        msg = "📊 <b>Tus estadísticas por tema:</b>\n\n"
        for topic, tipos in stats.items():
            msg += f"<b>{topic}</b>\n"
            for tipo, datos in tipos.items():
                msg += (
                    f"  • {tipo.capitalize()}: "
                    f"{datos['aciertos']}✅ / {datos['fallos']}❌ "
                    f"({datos['ratio']}%)\n"
                )
            msg += "\n"

        buttons = [
            [InlineKeyboardButton("⬅ Volver", callback_data="practice")]
        ]
        await query.message.reply_text(
            msg,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(buttons)
        )


# Command /suggest
async def cmd_suggest(update, context):
    context.user_data["awaiting_suggestion"] = True
    await update.message.reply_text(
        "📝 *Envíame tu sugerencia ahora mismo*",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅ Cancelar", callback_data="main_menu")]
        ])
    )

# command /id: show your IDs and the ADMIN_CHAT_ID charge in the container
# async def cmd_id(update, context):
#     u = update.effective_user
#     c = update.effective_chat
#     await update.message.reply_text(
#         f"👤 user.id = {u.id}\n"
#         f"💬 chat.id = {c.id}\n"
#         f"⚙️ ADMIN_CHAT_ID (config) = {ADMIN_CHAT_ID}"
#     )

# # command /pingadmin: send a message of proof to the ADMIN_CHAT_ID
# async def cmd_pingadmin(update, context):
#     try:
#         await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text="✅ Ping al admin OK")
#         await update.message.reply_text("He podido enviar al ADMIN_CHAT_ID.")
#     except Exception as e:
#         await update.message.reply_text(f"❌ No pude enviar al ADMIN_CHAT_ID. Error: {e}")

SUG_PAGE_SIZE = 10

def _is_admin(update) -> bool:
    return update.effective_user and update.effective_user.id == int(ADMIN_CHAT_ID)

def _render_suggestion_row(sug) -> str:
    # sug: (Suggestion, username, telegram_id)
    s, username, tg_id = sug
    who = username or (str(tg_id) if tg_id else "—")
    status = "✅" if s.resolved else "🟠"
    return (
        f"{status} <b>#{s.id}</b> "
        f"<i>{s.created_at.strftime('%Y-%m-%d %H:%M')}</i> — "
        f"<code>{escape(who)}</code>\n"
        f"<pre>{escape((s.text or '')[:500])}</pre>"
    )

async def cmd_suggestions(update, context):
    if not _is_admin(update):
        await update.message.reply_text("⛔ Solo la administradora puede usar este comando.")
        return

    # filter: /suggestions, /suggestions all|open|resolved
    args = (context.args or [])
    flt = (args[0].lower() if args else "open")
    if flt not in ("open", "resolved", "all"):
        flt = "open"

    page = 0
    await _send_suggestions_page(update, context, flt, page, via_callback=False)

async def _send_suggestions_page(update_or_query, context, flt: str, page: int, via_callback: bool):
    # build query according to filter
    with SessionLocal() as session:
        q = session.query(
            Suggestion,
            User.username,
            User.telegram_id
        ).outerjoin(User, User.id == Suggestion.user_id)

        if flt == "open":
            q = q.filter(Suggestion.resolved.is_(False))
        elif flt == "resolved":
            q = q.filter(Suggestion.resolved.is_(True))

        total = q.count()
        suggestions = (
            q.order_by(Suggestion.created_at.desc(), Suggestion.id.desc())
             .offset(page * SUG_PAGE_SIZE)
             .limit(SUG_PAGE_SIZE)
             .all()
        )

    if not suggestions:
        txt = "📭 No hay sugerencias para mostrar." if total == 0 else "📭 No hay más sugerencias en esta página."
        if via_callback:
            await update_or_query.callback_query.message.edit_text(txt)
        else:
            await update_or_query.message.reply_text(txt)
        return

    # body
    lines = ["💡 <b>Sugerencias</b>"]
    if flt == "open":
        lines.append("Filtro: <b>Abiertas</b>")
    elif flt == "resolved":
        lines.append("Filtro: <b>Resueltas</b>")
    else:
        lines.append("Filtro: <b>Todas</b>")
    lines.append(f"Página: <b>{page+1}</b>\n")

    for s in suggestions:
        lines.append(_render_suggestion_row(s))
        sug = s[0]
        # toggle button per row using separate callback
    text = "\n".join(lines)

    #  Keyboard: navigation and filter
    from telegram import InlineKeyboardMarkup, InlineKeyboardButton
    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton("⬅ Prev", callback_data=f"sug_page:{flt}:{page-1}"))
    if (page+1) * SUG_PAGE_SIZE < total:
        nav.append(InlineKeyboardButton("Next ➡", callback_data=f"sug_page:{flt}:{page+1}"))

    filters_row = [
        InlineKeyboardButton("Abiertas", callback_data="sug_filter:open:0"),
        InlineKeyboardButton("Resueltas", callback_data="sug_filter:resolved:0"),
        InlineKeyboardButton("Todas", callback_data="sug_filter:all:0"),
    ]

    # Buttons per row (toggle) in separate messages for simplicity:
    # we will send the list and then, for ergonomics, a keyboard with grouped toggles

    #Create toggle keys in blocks:
    toggles = []
    for s in suggestions:
        sug = s[0]
        label = f"#{sug.id} → " + ("Reabrir" if sug.resolved else "Resolver")
        new_state = "0" if sug.resolved else "1"  # 1=resolve, 0=reopen
        toggles.append(InlineKeyboardButton(label, callback_data=f"sug_toggle:{sug.id}:{new_state}:{flt}:{page}"))

    #  Pack toggles in groups of 3 per row:
    toggle_rows = [toggles[i:i+3] for i in range(0, len(toggles), 3)]
    rows = []
    if nav:
        rows.append(nav)
    rows.append(filters_row)
    rows.extend(toggle_rows)
    rows.append([InlineKeyboardButton("🔄 Refrescar", callback_data=f"sug_page:{flt}:{page}")])

    markup = InlineKeyboardMarkup(rows)

    if via_callback:
        await update_or_query.callback_query.message.edit_text(text, parse_mode="HTML", reply_markup=markup, disable_web_page_preview=True)
    else:
        await update_or_query.message.reply_text(text, parse_mode="HTML", reply_markup=markup, disable_web_page_preview=True)

def _build_exam_sets(session, topic_id: int | None):
    """return (test_ids, code_ids) for the exam. If topic_id is None, use all the topics"""
    q_test = session.query(Exercise).filter(Exercise.type == "test")
    q_code = session.query(Exercise).filter(Exercise.type == "code")
    if topic_id is not None:
        q_test = q_test.filter(Exercise.topic_id == topic_id)
        q_code = q_code.filter(Exercise.topic_id == topic_id)

    test_all = q_test.all()
    code_all = q_code.all()
    random.shuffle(test_all)
    random.shuffle(code_all)
    test_ids = [e.id for e in test_all[:EXAM_NUM_TEST]]
    code_ids = [e.id for e in code_all[:EXAM_NUM_CODE]]
    return test_ids, code_ids

def _exam_bootstrap_state(context, scope: str, topic: str, test_ids: list[int], code_ids: list[int]):
    #cleen flags of others modes
    for k in ("current_mode", "current_exercise", "current_options", "awaiting_code", "last_code"):
        context.user_data.pop(k, None)

    context.user_data["exam"] = {
        "active": True,
        "scope": scope,            # 'topic' or 'final'
        "topic": topic,            # name only for show
        "phase": "test",
        "test_ids": test_ids,
        "code_ids": code_ids,
        "i_test": 0,
        "i_code": 0,
        "score_test": 0.0,
        "score_code": 0.0,
        "answers": [],
        "start_ts": time(),
    }

async def _exam_send_current(update, context):
    """
    Sends the current step of the exam.
    - Test phase: EDIT the existing message (keeps the flow compact).
    - Code phase: POST a NEW message (so the conversation shows the latest
      code exercise at the bottom and doesn't hide previous messages).
    """
    exam = context.user_data.get("exam", {})
    query = getattr(update, "callback_query", None)

    #test phase
    if exam.get("phase") == "test":
        i = exam["i_test"]
        if i < len(exam["test_ids"]):
            ex_id = exam["test_ids"][i]

            # Load the exercise from DB
            with SessionLocal() as session:
                ex = session.query(Exercise).filter(Exercise.id == ex_id).one_or_none()

            # If something went wrong, skip to next one
            if not ex:
                exam["i_test"] += 1
                await _exam_send_current(update, context)
                return

            # Parse options from whatever format is stored in DB
            opts, correct_idx, correct_text = _parse_test_options_from_exercise(ex)
            

            # If there are no options, offer "continue" to skip it
            if not opts:
                if query and query.message:
                    await _safe_edit(
                        query.message,
                        text="⚠️ Esta pregunta no tiene opciones configuradas. La saltaremos.",
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Continuar", callback_data="exam_answer_0")]]
                        ),
                    )
                else:
                    # Fallback: new message (very rare here)
                    await context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text="⚠️ Esta pregunta no tiene opciones configuradas. La saltaremos.",
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Continuar", callback_data="exam_answer_0")]]
                        ),
                    )
                return

            # Save state to check the answer later
            exam["current_test_options"] = opts
            exam["current_test_correct_idx"] = correct_idx
            exam["current_test_correct_text"] = correct_text

            options_text, kb_letters = build_mcq_blocks(
                options=opts,
                cb_prefix="exam_answer_",
                extra_rows=[[InlineKeyboardButton("❌ Cancelar examen", callback_data="exam_cancel")]]
            )

            question_html = h(ex.question)
            body = (
                f"🧪 <b>Examen</b> — Test {i+1}/{len(exam['test_ids'])}\n\n"
                f"{_render_question_html(ex.question)}"
            )

            # Edit and envy messages by the keyboard of letters
            if query and query.message:
                await _safe_edit(
                    query.message,
                    text=body,
                    parse_mode="HTML",
                    reply_markup=kb_letters,
                )
            else:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=body,
                    parse_mode="HTML",
                    reply_markup=kb_letters,
                )
            return

            # Build keyboard: one option per row
            # rows = [
            #     [InlineKeyboardButton(opt, callback_data=f"exam_answer_{idx}")]
            #     for idx, opt in enumerate(opts)
            # ]
            # rows.append([InlineKeyboardButton("❌ Cancelar examen", callback_data="exam_cancel")])

            # # edit the current message in test phase
            # if query and query.message:
            #     await _safe_edit(
            #         query.message,
            #         text=f"🧪 <b>Examen</b> — Test {i+1}/{len(exam['test_ids'])}\n\n<b>{ex.question}</b>",
            #         parse_mode="HTML",
            #         reply_markup=InlineKeyboardMarkup(rows),
            #     )
            # else:
            #     # Fallback: post new message if there is no message to edit
            #     await context.bot.send_message(
            #         chat_id=update.effective_chat.id,
            #         text=f"🧪 <b>Examen</b> — Test {i+1}/{len(exam['test_ids'])}\n\n<b>{ex.question}</b>",
            #         parse_mode="HTML",
            #         reply_markup=InlineKeyboardMarkup(rows),
            #     )
            # return
        else:
            # Switch to code phase
            exam["phase"] = "code"
            exam["i_code"] = 0

    #code phase
    if exam.get("phase") == "code":
        j = exam["i_code"]
        if j < len(exam["code_ids"]):
            ex_id = exam["code_ids"][j]

            # Load the exercise from DB
            with SessionLocal() as session:
                ex = session.query(Exercise).filter(Exercise.id == ex_id).one_or_none()

            # If missing, jump to the next one
            if not ex:
                exam["i_code"] += 1
                await _exam_send_current(update, context)
                return

            # Prepare state for code solving (no hints/solution during exam)
            context.user_data["current_exercise_id"] = ex.id
            context.user_data["awaiting_code"] = True
            context.user_data["exam"] = exam  # persist changes

            text = (
                f"🧪 <b>Examen</b> — Programación {j+1}/{len(exam['code_ids'])}\n\n"
                f"<b>Enunciado:</b> {escape(ex.question)}\n\n"
                "Pega tu solución como <b>texto</b>. Cuando la reciba, aparecerán "
                "los botones <b>Enviar</b> y <b>Reintentar</b>.\n"
                "Durante el examen no hay <i>pistas</i> ni <i>solución</i>."
            )
            kb = InlineKeyboardMarkup(
                [[InlineKeyboardButton("❌ Cancelar examen", callback_data="exam_cancel")]]
            )

            #In code phase we send a new message
            chat_id = update.effective_chat.id if update.effective_chat else query.message.chat_id
            await context.bot.send_message(
                chat_id=chat_id,
                text=text,
                parse_mode="HTML",
                reply_markup=kb,
                disable_web_page_preview=True,
            )
            return
        else:
            await _exam_finish(update, context)
            return


async def _exam_finish(update, context):
    """Send the final exam result as a NEW message (do not edit previous one)."""
    exam = context.user_data.get("exam", {})
    exam["active"] = False

    # Compute final score
    total = round(exam.get("score_test", 0.0) + exam.get("score_code", 0.0), 2)

    # Build result text
    msg = (
        "🎉 <b>Examen finalizado</b>\n\n"
        f"🧮 Puntuación: <b>{total:.2f} / 10</b>\n"
        f"   • Test: {exam.get('score_test', 0.0):.2f} / 5\n"
        f"   • Programación: {exam.get('score_code', 0.0):.2f} / 5\n\n"
        f"Ámbito: <b>{escape(exam.get('topic',''))}</b>"
    )

    # Simple keyboard to return to main menu
    kb = InlineKeyboardMarkup(
        [[InlineKeyboardButton("⬅ Volver al menú", callback_data="main_menu")]]
    )

    # Use effective_chat.id so it works whether we came from a callback or from a message
    chat_id = update.effective_chat.id
    await context.bot.send_message(
        chat_id=chat_id,
        text=msg,
        parse_mode="HTML",
        reply_markup=kb
    )

    # Clear transient code/exam state after sending the result
    for k in ("awaiting_code", "current_exercise_id", "last_code"):
        context.user_data.pop(k, None)


async def _safe_edit(message, *, text, reply_markup=None, parse_mode=None, disable_web_page_preview=False):
    try:
        await message.edit_text(
            text,
            reply_markup=reply_markup,
            parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview
        )
    except BadRequest as e:
        if "Message is not modified" in str(e):
            # Send it as a new message if there are no actual changes
            await message.chat.send_message(
                text,
                reply_markup=reply_markup,
                parse_mode=parse_mode,
                disable_web_page_preview=disable_web_page_preview
            )
        else:
            raise

def _parse_test_options_from_exercise(ex):
    """
    Devuelve (opts, correct_idx, correct_text) aceptando varios formatos:
    - ex.options_json = {"options": [...], "correct_idx": int?, "answer": str?}
    - ex.options = list[str]
    - ex.options = str (JSON o texto con '|' o saltos de línea)
    - ex.answer / ex.correct_answer como texto de la opción correcta
    """
    opts, correct_idx, correct_text = [], None, None

    # JSON standart if exists
    data = getattr(ex, "options_json", None)
    if isinstance(data, dict) and data.get("options"):
        opts = [str(o) for o in (data.get("options") or [])]
        if "correct_idx" in data and isinstance(data["correct_idx"], int):
            correct_idx = data["correct_idx"]
        if "answer" in data and data["answer"] is not None:
            correct_text = str(data["answer"])

    # field options
    raw = getattr(ex, "options", None)
    if not opts and raw is not None:
        if isinstance(raw, list):
            opts = [str(o) for o in raw]
        elif isinstance(raw, str):
            s = raw.strip()
            # try JSON
            try:
                loaded = json.loads(s)
                if isinstance(loaded, list):
                    opts = [str(o) for o in loaded]
                elif isinstance(loaded, dict) and "options" in loaded:
                    opts = [str(o) for o in loaded["options"]]
                    if "correct_idx" in loaded and isinstance(loaded["correct_idx"], int):
                        correct_idx = loaded["correct_idx"]
                    if "answer" in loaded and loaded["answer"] is not None:
                        correct_text = str(loaded["answer"])
            except Exception:
                # fallback by separators
                if "|" in s:
                    opts = [x.strip() for x in s.split("|") if x.strip()]
                else:
                    opts = [x.strip() for x in s.splitlines() if x.strip()]
        else:
            # unknow type 
            opts = [str(raw)]

    #answer text correct from the model
    if correct_text is None:
        correct_text = (getattr(ex, "answer", None) 
                        or getattr(ex, "correct_answer", None))
        if correct_text is not None:
            correct_text = str(correct_text)

    # if we have the correct text, calculate the index if there is in options
    if correct_idx is None and correct_text is not None and opts:
        try:
            correct_idx = next(i for i, o in enumerate(opts) if o == correct_text)
        except StopIteration:
            pass

    return opts, correct_idx, correct_text

# Accept fenced code ```cpp ... ``` or plain C++-looking text
CODE_FENCE_RE = re.compile(
    r"```(?:cpp|c\+\+)?\s*\n([\s\S]*?)\n?```",  # nota: \n? antes de ```
    re.IGNORECASE
)

CPP_SMELLS = (
    "#include", "int main", "using namespace", "::", "std::", ";", "{", "}"
)

def _extract_code_block(text: str) -> str | None:
    if not text:
        return None
    #block ```cpp ... ```
    m = CODE_FENCE_RE.search(text)
    if m:
        return m.group(1).strip()

    #plain text
    s = text.strip()
    multiline = ("\n" in s) or (s.count(";") >= 2) or ("{" in s and "}" in s)
    if multiline and any(tok in s for tok in CPP_SMELLS):
        return s

    return None


async def help_cmd(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ <b>Ayuda</b>\n\n"
        "• Usa los <i>botones</i> para navegar por teoría, práctica, tests y exámenes.\n"
        "• Comandos:\n"
        "  /start – Reinicia el bot.\n"
        "  /menu – Vuelve al menú principal.\n"
        "  /help – Muestra esta ayuda.\n",
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove()
    )

async def menu_cmd(update, context: ContextTypes.DEFAULT_TYPE):
    #await update.message.reply_text("👋", reply_markup=ReplyKeyboardRemove())
    clear_practice_state(context)
    await show_main_menu(update, context)

def clear_practice_state(context):
    """Delete any traces of practice (tests or code)"""
    for k in ("current_topic", "current_mode", "current_exercise",
              "current_options", "awaiting_code", "current_exercise_id",
              "last_code", "served_code_ids"):
        context.user_data.pop(k, None)


def build_mcq_blocks(options: list[str], cb_prefix: str, extra_rows=None):
    """
    Returns (options_text, keyboard):
      - options_text: "A. ...\nB. ...\n..."
      - keyboard: shortcut keys A/B/C/D... (2 per row)
    """
    extra_rows = extra_rows or []

    # complet text, without cut
    lines = [f"{LETTERS_ES[i]}. {h(str(opt))}" for i, opt in enumerate(options)]
    opts_block = "\n".join(lines)

    #shorts buttons
    rows: list[list[InlineKeyboardButton]] = []
    for i in range(len(options)):
        if i % 2 == 0:
            rows.append([])
        rows[-1].append(
            InlineKeyboardButton(LETTERS_ES[i], callback_data=f"{cb_prefix}{i}")
        )

    # extra rows
    rows.extend(extra_rows)

    return opts_block, InlineKeyboardMarkup(rows)


def _render_question_html(q: str) -> str:
    s = str(q or "")
    if ("<pre" in s) or ("<code" in s) or ("</pre>" in s) or ("</code>" in s):
        return s
    m = re.search(r"```(?:\w+)?\s*\n([\s\S]*?)\n?```", s)
    if m:
        inner = h(m.group(1))
        return s[:m.start()] + f"<pre><code>{inner}</code></pre>" + s[m.end():]
    return h(s)
