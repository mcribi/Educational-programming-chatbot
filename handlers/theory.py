from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from data.topics import cpp_topics
from data.theory_cpp import theory_cpp  # Dict[str, Topic] with list[Lesson]

async def show_lesson_menu(update, context, topic_key=None):
    query = update.callback_query
    await query.answer()

    if not topic_key:
        topic_key = context.user_data["current_topic"]

    context.user_data["current_topic"] = topic_key

    lessons = theory_cpp[topic_key].lessons

    buttons = [
        [InlineKeyboardButton(lesson.title, callback_data=f"lesson_{topic_key}_{i}")]
        for i, lesson in enumerate(lessons)
    ]
    buttons.append([InlineKeyboardButton("⬅ Volver al menú principal", callback_data="main_menu")])

    await query.message.edit_text(
        f"📖 <b>{topic_key}</b>: elige una lección:",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode="HTML"
    )


async def show_lesson(update, context):
    query = update.callback_query
    await query.answer()

    _, topic_key, idx = query.data.split("_", 2)
    idx = int(idx)

    lesson = theory_cpp[topic_key].lessons[idx]

    context.user_data["current_topic"] = topic_key
    context.user_data["current_lesson"] = idx

    buttons = []
    if idx > 0:
        buttons.append(InlineKeyboardButton("⬅ Anterior", callback_data=f"lesson_{topic_key}_{idx - 1}"))
    if idx < len(theory_cpp[topic_key].lessons) - 1:
        buttons.append(InlineKeyboardButton("➡ Siguiente", callback_data=f"lesson_{topic_key}_{idx + 1}"))

    buttons.append(InlineKeyboardButton("📚 Menú del tema", callback_data=f"menu_topic_{topic_key}"))

    await query.message.edit_text(
        text=f"<b>{lesson.title}</b>\n\n{lesson.content}",
        reply_markup=InlineKeyboardMarkup([buttons]),
        parse_mode="HTML"
    )


async def show_theory(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    i = int(query.data.split("_")[1])
    topic = cpp_topics[i]
    await show_lesson_menu(update, context, topic_key=topic)