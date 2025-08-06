from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from data.exercises import exercises_by_topic
from src.exercise_generator import ExerciseGenerator
from db.database import SessionLocal
from db.models.attempt import Attempt
from db.models.exercise import Exercise as ExerciseModel

import random

async def start_practice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    topic = context.user_data["current_topic"]
    mode = context.user_data["current_mode"]

    generator = ExerciseGenerator(exercises_by_topic)
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

    context.user_data["available_exercises"] = all_exercises

    await send_question(update, context)


async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = context.user_data["user_id"]
    topic = context.user_data["current_topic"]
    mode = context.user_data["current_mode"]
    available_exercises = context.user_data["available_exercises"]

    #calculate weights based on attempts
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

    #select a random exercise based on weights
    exercises, weights = zip(*weighted_exercises)
    exercise = random.choices(exercises, weights=weights, k=1)[0]

    options = exercise.options.copy()
    random.shuffle(options)

    context.user_data["current_exercise"] = exercise
    context.user_data["current_options"] = options

    buttons = [[InlineKeyboardButton(opt, callback_data=f"resp_{options.index(opt)}")] for opt in options]
    buttons.append([InlineKeyboardButton("⬅ Volver al menú de práctica", callback_data="back_to_mode")])

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"<b>Ejercicio tipo Test</b>\n\n{exercise.question}",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode="HTML"
    )


async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = context.user_data.get("user_id")
    exercise = context.user_data.get("current_exercise")
    user_answer = update.message.text.strip()
    is_correct = exercise.is_correct(user_answer)

    # save attempt 
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
