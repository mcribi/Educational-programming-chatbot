from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from data.topics import cpp_topics
from data.theory_cpp import theory_cpp
from handlers.theory import show_lesson_menu, show_lesson
from handlers.exercises import start_practice, send_question

GREETINGS = ["hola", "buenas", "hey", "holi", "hello", "saludos", "qué tal", "start"]

# Function to start the main menu
async def start(update, context):
    buttons = [
        [InlineKeyboardButton("Aprender", callback_data="learn")],
        [InlineKeyboardButton("Practicar", callback_data="practice")]
    ]
    await update.message.reply_text(
        "¡Hola! ¿Qué quieres hacer?",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# Function to handle text messages
async def handle_text(update, context):
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

        context.user_data["current_topic"] = topic
        context.user_data["current_mode"] = mode
        context.user_data["question_index"] = 0

        await start_practice(update, context)

    elif data.startswith("resp_"):
        option_index = int(data[5:])
        i = context.user_data["question_index"]
        exercises = context.user_data["filtered_exercises"]
        exercise = exercises[i]
        options = context.user_data["current_options"]
        selected = options[option_index]

        if exercise.is_correct(selected):
            response = f"<b>{exercise.question}</b>\n\n✅ ¡Correcto!"
        else:
            response = (
                f"<b>{exercise.question}</b>\n\n"
                f"❌ <b>Incorrecto</b>\n\n"
                f"<b>Explicación:</b> {exercise.explanation}"
            )

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response,
            parse_mode="HTML"
        )

        context.user_data["question_index"] += 1

        if context.user_data["question_index"] < len(exercises):
            await asyncio.sleep(0.5)
            await send_question(update, context)
        else:
            buttons = [
                [InlineKeyboardButton("🔁 Practicar este tipo otra vez", callback_data="repeat_mode")],
                [InlineKeyboardButton("📚 Elegir otro tipo", callback_data="choose_mode")],
                [InlineKeyboardButton("🏠 Menú principal", callback_data="main_menu")]
            ]
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="🏁 Has terminado los ejercicios de este tipo. ¿Qué te gustaría hacer ahora?",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

    elif data == "repeat_mode":
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
        buttons = [
            [InlineKeyboardButton("Aprender", callback_data="learn")],
            [InlineKeyboardButton("Practicar", callback_data="practice")]
        ]

        if update.message:
            await update.message.reply_text("¿Qué quieres hacer?", reply_markup=InlineKeyboardMarkup(buttons))
        else:
            await update.callback_query.message.reply_text("¿Qué quieres hacer?", reply_markup=InlineKeyboardMarkup(buttons))
