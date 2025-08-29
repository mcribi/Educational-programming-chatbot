from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from data.exercises import exercises_by_topic
from src.exercise_generator import ExerciseGenerator
from db.database import SessionLocal
from db.models.attempt import Attempt
from db.models.exercise import Exercise as ExerciseModel
from handlers.code import code_help_text

import random

async def start_practice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Entry point after user picks topic + mode."""
    query = update.callback_query
    await query.answer()

    topic = context.user_data["current_topic"]
    mode = context.user_data["current_mode"]

    generator = ExerciseGenerator(exercises_by_topic)
    # Filter exercises by selected mode (test|code)
    all_exercises = [e for e in generator.exercise_db[topic] if e.type == mode]

    if not all_exercises:
        buttons = [
            [InlineKeyboardButton("📚 Elegir otro tipo", callback_data="choose_mode")],
            [InlineKeyboardButton("🏠 Volver al menú", callback_data="main_menu")]
        ]
        await query.message.edit_text(
            f"⚠️ No hay ejercicios disponibles del tipo <b>{mode}</b> para el tema <b>{topic}</b>.",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="HTML"
        )
        return

    # Keep the pool for weighted selection
    context.user_data["available_exercises"] = all_exercises

    await send_question(update, context)


async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send next question depending on mode (test or code)."""
    user_id = context.user_data["user_id"]
    topic = context.user_data["current_topic"]
    mode = context.user_data["current_mode"]
    available_exercises = context.user_data["available_exercises"]

    # Weighted pick based on last attempt per exercise
    weighted_exercises = []
    with SessionLocal() as session:
        for e in available_exercises:
            db_exercise = session.query(ExerciseModel).filter_by(question=e.question).first()
            if db_exercise:
                attempt = session.query(Attempt).filter_by(
                    user_id=user_id,
                    exercise_id=db_exercise.id
                ).order_by(Attempt.timestamp.desc()).first()
                weight = 0.8 if attempt and not attempt.is_correct else 0.2
            else:
                weight = 0.5
            weighted_exercises.append((e, weight))

    exercises, weights = zip(*weighted_exercises)
    exercise = random.choices(exercises, weights=weights, k=1)[0]

    # Store the chosen exercise (src object)
    context.user_data["current_exercise"] = exercise

    # Also store the DB exercise id for /run and /submit
    with SessionLocal() as session:
        row = session.query(ExerciseModel.id).filter_by(question=exercise.question, type="code").first()
        if row:
            context.user_data["current_exercise_id"] = row[0]

    if mode == "test":
        # TEST MODE UI
        options = exercise.options.copy()
        random.shuffle(options)
        context.user_data["current_options"] = options

        buttons = [[InlineKeyboardButton(opt, callback_data=f"resp_{options.index(opt)}")] for opt in options]
        buttons.append([InlineKeyboardButton("⬅ Volver al menú de práctica", callback_data="back_to_mode")])

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"<b>Ejercicio tipo Test</b>\n\n{exercise.question}",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="HTML"
        )
    else:
        # CODE MODE UI
        # Optional stdin example
        stdin_hint = ""
        if hasattr(exercise, "stdin") and exercise.stdin:
            stdin_hint = f"\n\n🧪 <b>Entrada de prueba</b> (stdin):\n<pre>{exercise.stdin}</pre>"

        # Limits (if present on the exercise)
        limits_bits = []
        if getattr(exercise, "time_limit_ms", None):
            limits_bits.append(f"⏱ {exercise.time_limit_ms} ms")
        if getattr(exercise, "memory_limit_mb", None):
            limits_bits.append(f"💾 {exercise.memory_limit_mb} MB")
        limits_line = f"\n\n<b>Límites</b>: {' | '.join(limits_bits)}" if limits_bits else ""

        # Commands cheat-sheet (HTML)
        help_html = (
            "\n\nℹ️ <b>Comandos</b><br/>"
            "• <b>/out</b> — ejecuta tu último código y muestra la salida.<br/>"
            "• <b>/run</b> — ejecuta los <i>ejemplos</i> del enunciado.<br/>"
            "• <b>/submit</b> — ejecuta <i>todos</i> los tests y evalúa.<br/>"
            "• <b>/hint</b> — muestra una pista (si hay).<br/>"
            "• <b>/solution</b> — solución oficial."
        )

        buttons = [
            [InlineKeyboardButton("⬅ Volver al menú de práctica", callback_data="back_to_mode")],
            [InlineKeyboardButton("🔁 Siguiente enunciado", callback_data="repeat_mode")],
        ]

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(
                f"<b>Ejercicio de Programación (C++)</b>\n\n"
                f"{exercise.question}\n\n"
                f"💡 Envía tu solución C++ en un único mensaje. "
                f"Acepto bloques con ```cpp ... ``` o texto plano."
                f"{stdin_hint}"
                f"{limits_line}"
                f"{help_html}"
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="HTML"
        )



async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle multiple-choice answers (TEST MODE)."""
    user_id = context.user_data.get("user_id")
    exercise = context.user_data.get("current_exercise")
    user_answer = update.message.text.strip()
    is_correct = exercise.is_correct(user_answer)

    # Persist attempt
    with SessionLocal() as session:
        db_exercise = session.query(ExerciseModel).filter_by(question=exercise.question).first()
        if db_exercise:
            session.add(Attempt(
                user_id=user_id,
                exercise_id=db_exercise.id,
                is_correct=is_correct
            ))
            session.commit()

    if is_correct:
        await update.message.reply_text("✅ ¡Correcto!")
    else:
        await update.message.reply_text(
            f"❌ Incorrecto.\n\n<b>Explicación:</b> {exercise.explanation}",
            parse_mode="HTML"
        )

    await send_question(update, context)


# code mode exercise
def _extract_cpp_from_message(text: str) -> str:
    """Extract C++ code from message. Accepts fenced blocks or raw text.
    - If fenced: returns the inside.
    - If not fenced: returns the whole message.
    """
    t = text.strip()
    # Triple backticks with or without 'cpp'
    if t.startswith("```"):
        # Remove first fence line
        lines = t.splitlines()
        if not lines:
            return ""
        # Drop first ```, also ignore an optional language tag
        first = lines[0].strip()
        rest = lines[1:]
        # Drop last fence if present
        if rest and rest[-1].strip().startswith("```"):
            rest = rest[:-1]
        return "\n".join(rest).strip()
    return t


async def handle_code_submission(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle code submission, call runner and show compile/runtime results."""
    # Safety: ensure we are in code mode
    if context.user_data.get("current_mode") != "code":
        # If user sends random text while not in code mode, just reroute to test handler
        await handle_response(update, context)
        return

    exercise = context.user_data.get("current_exercise")
    user_id = context.user_data.get("user_id")

    raw = update.message.text or ""
    code = _extract_cpp_from_message(raw)

    if not code or len(code) < 10:
        await update.message.reply_text(
            "⚠️ No he detectado código C++. Envía tu solución otra vez (puedes usar ```cpp ... ```)."
        )
        return

    # exercise can provide stdin 
    stdin = getattr(exercise, "stdin", "") or ""

    try:
        result = await run_cpp(code=code, stdin=stdin)
    except RunnerError as e:
        await update.message.reply_text(f"❌ Error al contactar con el runner: {e}")
        return

    # Build feedback message
    ok = result.get("ok", False)
    stage = result.get("stage", "run")
    stdout = result.get("stdout", "")
    stderr = result.get("stderr", "")
    time_ms = result.get("time_ms", 0)
    exit_code = result.get("exit_code")

    # Heuristic correctness:
    # - If the exercise defines an 'expected_stdout' field, compare trimmed text.
    # - Otherwise, consider success == (ok and exit_code == 0).
    expected = getattr(exercise, "expected_stdout", None)
    if expected is not None:
        is_correct = (stdout.strip() == str(expected).strip())
    else:
        is_correct = bool(ok and (exit_code == 0))

    # Persist attempt as best-effort
    with SessionLocal() as session:
        db_exercise = session.query(ExerciseModel).filter_by(question=exercise.question).first()
        if db_exercise:
            session.add(Attempt(
                user_id=user_id,
                exercise_id=db_exercise.id,
                is_correct=is_correct
            ))
            session.commit()

    # Show the result
    verdict = "✅ Programa OK" if is_correct else "❌ Programa incorrecto"
    details = (
        f"<b>Fase</b>: {stage}\n"
        f"<b>Exit code</b>: {exit_code}\n"
        f"<b>Tiempo</b>: {time_ms} ms\n\n"
        f"<b>STDOUT</b>:\n<pre>{(stdout or '').strip() or '(vacío)'}</pre>\n"
        f"<b>STDERR</b>:\n<pre>{(stderr or '').strip() or '(vacío)'}</pre>"
    )
    await update.message.reply_text(f"{verdict}\n\n{details}", parse_mode="HTML")

    # Ask next one
    await send_question(update, context)
