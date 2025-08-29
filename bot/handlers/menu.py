from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from data.topics import cpp_topics
from data.theory_cpp import theory_cpp
from handlers.theory import show_lesson_menu, show_lesson
from handlers.exercises import start_practice, send_question
from db.models.user import User
from db.database import SessionLocal
from db.models.attempt import Attempt
from sqlalchemy import func, Integer
from db.models.exercise import Exercise
from db.models.topic import Topic
from handlers.code import code_help_text
from telegram.error import BadRequest


GREETINGS = ["hola", "ola", "buenas", "hey", "holi", "hello", "saludos", "qué tal", "start"]

# ---- Helpers for code-mode ---------------------------------------------------
def _pick_next_code_exercise(session, user_id: int, topic_name: str):
    """
    Pick next 'code' exercise for the given topic.
    Preference order:
      1) exercises never solved (no Attempt with is_correct = True)
      2) else any 'code' exercise in topic (ordered by id)
    Returns Exercise row or None.
    """
    topic = session.query(Topic).filter(Topic.name == topic_name).one_or_none()
    if not topic:
        return None

    # All code exercises in this topic
    exercises = (
        session.query(Exercise)
        .filter(Exercise.topic_id == topic.id, Exercise.type == "code")
        .order_by(Exercise.id.asc())
        .all()
    )
    if not exercises:
        return None

    # Prefer exercises without a correct attempt
    for ex in exercises:
        # Is there a correct attempt for this user+exercise?
        ok = (
            session.query(Attempt)
            .filter(Attempt.user_id == user_id, Attempt.exercise_id == ex.id, Attempt.is_correct.is_(True))
            .first()
        )
        if not ok:
            return ex

    # If all were solved, just return the first one (user can practice again)
    return exercises[0]

async def _send_code_prompt(query_or_update, context, ex: Exercise):
    """
    Send a concise prompt for the selected code exercise:
    - title/question
    - sample input/output (first sample)
    - limits + short instructions
    - inline buttons: ℹ️ Ayuda, 🔁 Siguiente, ⬅ Volver
    """
    # Extract first sample to show
    sample_io = ""
    if ex.tests_json and isinstance(ex.tests_json, dict):
        samples = (ex.tests_json or {}).get("sample", []) or []
        if samples:
            s = samples[0]
            inp = (s.get("input") or "").strip()
            out = (s.get("output") or "").strip()
            sample_io = (
                "\n*Ejemplo (sample)*\n"
                f"*Entrada:*\n```\n{inp}\n```\n"
                f"*Salida esperada:*\n```\n{out}\n```"
            )

    limits = []
    if ex.time_limit_ms:
        limits.append(f"{ex.time_limit_ms} ms")
    if ex.memory_limit_mb:
        limits.append(f"{ex.memory_limit_mb} MB")
    limits_str = " · ".join(limits) if limits else "1.5 s · 128 MB"

    text = (
        f"💻 *Ejercicio de programación*\n\n"
        f"*Enunciado:* {ex.question}\n"
        f"{sample_io}\n\n"
        f"*Límites:* {limits_str}\n\n"
        "Envía tu solución en un bloque ```cpp ... ```\n"
        "y usa /out (salida tal cual), /run (ejemplos) o /submit (tests completos).\n"
        "Opcional: /hint y /solution."
    )

    # Inline keyboard ONLY for code mode, with help button
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("ℹ️ Ayuda", callback_data="code_help")],
        [
            InlineKeyboardButton("🔁 Siguiente enunciado", callback_data="repeat_mode"),
            InlineKeyboardButton("⬅ Volver al menú de práctica", callback_data="back_to_mode"),
        ]
    ])

    # Output via callback or message (edit if possible; otherwise send new msg)
    try:
        if hasattr(query_or_update, "message") and query_or_update.message:
            # viene de un update normal
            await query_or_update.message.edit_text(
                text, parse_mode="Markdown", reply_markup=kb
            )
        else:
            # viene de callback_query
            await query_or_update.callback_query.message.edit_text(
                text, parse_mode="Markdown", reply_markup=kb
            )
    except BadRequest as e:
        # If content+markup are identical, Telegram refuses to edit.
        if "Message is not modified" in str(e):
            # send as a new message instead
            if hasattr(query_or_update, "message") and query_or_update.message:
                await query_or_update.message.reply_text(
                    text, parse_mode="Markdown", reply_markup=kb
                )
            else:
                await query_or_update.callback_query.message.reply_text(
                    text, parse_mode="Markdown", reply_markup=kb
                )
        else:
            raise

# ------------------------------------------------------------------------------
# Function to show the main menu
async def show_main_menu(update, context):
    buttons = [
        [InlineKeyboardButton("📚 Aprender", callback_data="learn")],
        [InlineKeyboardButton("📝 Practicar", callback_data="practice")]
    ]
    if update.message:
        await update.message.reply_text("¿Qué quieres hacer?", reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await update.callback_query.message.reply_text("¿Qué quieres hacer?", reply_markup=InlineKeyboardMarkup(buttons))

# Function to start the bot and check user registration
async def start(update, context):
    telegram_id = update.effective_user.id
    username = update.effective_user.username
    first_name = update.effective_user.first_name

    with SessionLocal() as session:
        user = session.query(User).filter_by(telegram_id=telegram_id).first()

        if user:
            context.user_data["user_id"] = user.id
            await update.message.reply_text(
                f"👋 ¡Hola de nuevo, {user.name}!\nTu identificador único es <b>{user.id}</b>.",
                parse_mode="HTML"
            )
            await show_main_menu(update, context)
        else:
            context.user_data["pending_registration"] = {
                "telegram_id": telegram_id,
                "username": username
            }
            await update.message.reply_text(
                "👋 ¡Hola! Parece que es tu primera vez usando el bot.\n\nPor favor, dime tu nombre para poder dirigirme a ti:"
            )

# Function to handle text messages
async def handle_text(update, context):
    if "pending_registration" in context.user_data:
        info = context.user_data.pop("pending_registration")
        name = update.message.text.strip()

        with SessionLocal() as session:
            new_user = User(
                telegram_id=info["telegram_id"],
                username=info["username"],
                name=name
            )
            session.add(new_user)
            session.commit()
            session.refresh(new_user)

        context.user_data["user_id"] = new_user.id

        await update.message.reply_text(
            f"✅ ¡Gracias, {name}!\nTe he registrado correctamente. Tu identificador único es <b>{new_user.id}</b>.",
            parse_mode="HTML"
        )
        await show_main_menu(update, context)
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

    if data == "learn":
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
            [InlineKeyboardButton("⬅ Volver", callback_data="practice")]
        ]
        await query.message.edit_text(
            f"Has elegido <b>{topic}</b>.\n\n¿Qué tipo de ejercicio quieres hacer:",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="HTML"
        )

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
            # --- NEW: pick and present a code exercise now ---
            user_id = context.user_data.get("user_id")
            if not user_id:
                await query.message.edit_text("⚠️ Debes registrarte primero con /start.")
                return

            with SessionLocal() as session:
                ex = _pick_next_code_exercise(session, user_id, topic)
                if not ex:
                    await query.message.edit_text("⚠️ No hay ejercicios de programación en este tema (aún).")
                    return
                # Keep state for code-mode handlers
                context.user_data["current_exercise_id"] = ex.id
                context.user_data["awaiting_code"] = True
                context.user_data.pop("last_code", None)

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
                context.user_data.pop("last_code", None)
            await _send_code_prompt(update, context, ex)
        else:
            await start_practice(update, context)

    elif data == "choose_mode":
        topic = context.user_data.get("current_topic")
        if not topic:
            await query.message.edit_text("Ocurrió un error. Usa /start para volver al menú.")
            return

        buttons = [
            [InlineKeyboardButton("📝 Test", callback_data="mode_test")],
            [InlineKeyboardButton("💻 Programar", callback_data="mode_code")],
            [InlineKeyboardButton("⬅ Volver al menú", callback_data="main_menu")]
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
