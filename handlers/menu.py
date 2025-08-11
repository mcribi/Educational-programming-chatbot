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


GREETINGS = ["hola", "buenas", "hey", "holi", "hello", "saludos", "qué tal", "start"]

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
        #buttons.append([InlineKeyboardButton("📊 Ver estadísticas", callback_data="view_stats")])
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

        context.user_data["current_topic"] = topic
        context.user_data["current_mode"] = mode

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

        #save attempt
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

        #continue in an infinite loop 
        await asyncio.sleep(0.5)
        await send_question(update, context)


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
        await show_main_menu(update, context)

    #for viewing statistics
    elif data == "view_stats":
        user_id = context.user_data.get("user_id")
        if not user_id:
            await query.message.reply_text("❌ No estás registrado. Usa /start.")
            return

        # Fetch statistics from the database
        stats = {}
        with SessionLocal() as session:
            rows = session.query(
                Exercise.topic,
                Exercise.type,
                func.count().label("total"),
                func.sum(func.cast(Attempt.is_correct, Integer)).label("aciertos")
            ).join(Attempt, Attempt.exercise_id == Exercise.id)\
            .filter(Attempt.user_id == user_id)\
            .group_by(Exercise.topic, Exercise.type)\
            .all()

            for topic, tipo, total, aciertos in rows:
                ratio = (aciertos or 0) / total if total > 0 else 0
                if topic not in stats:
                    stats[topic] = {}
                stats[topic][tipo] = {
                    "aciertos": aciertos or 0,
                    "fallos": total - (aciertos or 0),
                    "ratio": round(ratio * 100)
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

