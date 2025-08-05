from src.exercise import Exercise
from data.exercises import exercises_by_topic
from telegram.ext import ContextTypes
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import random

# Function to start the practice mode
async def start_practice(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query #get the callback query
    await query.answer() #acknowledge

    #get the current topic and mode from user data
    topic = context.user_data["current_topic"]
    mode = context.user_data["current_mode"]

    #filter exercises by topic and mode
    filtered = [e for e in exercises_by_topic[topic] if e.type == mode]

    # if no exercises found, show a message
    if not filtered:
        buttons = [
            [InlineKeyboardButton("📚 Elegir otro tipo", callback_data="elegir_tipo")],
            [InlineKeyboardButton("🏠 Volver al menú", callback_data="volver_menu")]
        ]
        await query.message.edit_text(
            f"⚠️ No hay ejercicios disponibles del tipo <b>{mode}</b> para el tema <b>{topic}</b>.",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="HTML"
        )
        return

    random.shuffle(filtered) #shufle the exercises
    context.user_data["question_index"] = 0
    context.user_data["filtered_exercises"] = filtered

    await send_question(update, context)

# function to send the next question
async def send_question(update, context):
    topic = context.user_data["current_topic"]
    mode = context.user_data["current_mode"]
    i = context.user_data["question_index"]

    exercises = context.user_data["filtered_exercises"]

    if i >= len(exercises):
        await update.callback_query.message.edit_text("🏁 No hay más ejercicios de este tipo.")
        return

    exercise: Exercise = exercises[i] #get the current exercise

    if exercise.type == "test":
        options = exercise.options.copy()
        random.shuffle(options)

        buttons = [
            [InlineKeyboardButton(option, callback_data=f"resp_{i}")]
            for i, option in enumerate(options)
        ]
        buttons.append([
            InlineKeyboardButton("⬅ Volver al menú de práctica", callback_data="volver_a_tipo")
        ])

        context.user_data["current_options"] = options

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"<b>Ejercicio tipo Test</b>\n\n{exercise.question}",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="HTML"
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"<b>Ejercicio</b>\n\n{exercise.question}",
            parse_mode="HTML"
        )

# Function to handle text answers for exercises
async def handle_text_answer(update, context: ContextTypes.DEFAULT_TYPE):
    topic = context.user_data.get("current_topic")
    if not topic:
        await update.message.reply_text("Usa /start y selecciona un tema para practicar.")
        return

    i = context.user_data["question_index"]
    exercise: Exercise = context.user_data["filtered_exercises"][i]
    user_answer = update.message.text.strip()

    if exercise.is_correct(user_answer):
        await update.message.reply_text("✅ ¡Correcto!")
    else:
        await update.message.reply_text(
            f"❌ Incorrecto.\n\n<b>Explicación:</b> {exercise.explanation}",
            parse_mode="HTML"
        )

    context.user_data["question_index"] += 1

    if context.user_data["question_index"] < len(context.user_data["filtered_exercises"]):
        await send_question(update, context)
    else:
        await update.message.reply_text("🏁 Has terminado los ejercicios de este tema.")
        context.user_data.clear()
