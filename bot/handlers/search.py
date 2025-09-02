from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from sqlalchemy.orm import joinedload
from db.database import SessionLocal
from db.models.lesson import Lesson as LessonModel
from db.models.topic import Topic as TopicModel
from data.theory_cpp import theory_cpp
import re
from html import escape, unescape

SEARCH_MODE_KEY = "mode_search"
PAGE_SIZE = 8

def _snippet(text: str, query: str, radius: int = 80) -> str:
    """
    Devuelve un trozo de texto sin HTML alrededor del primer match.
    - Quita etiquetas HTML del contenido original.
    - Resalta el término con <b>…</b> de forma segura (sin romper parseo).
    """
    # Normalise to plain text
    # decode entities (&lt; &gt; &amp; -> < > &)
    plain = unescape(text or "")
    # remove HTML tags
    plain = re.sub(r"<[^>]+>", " ", plain)
    #  compress spaces and line breaks
    plain = re.sub(r"\s+", " ", plain).strip()

    if not plain:
        return ""

    #Search term (case-insensitive) in plain text
    t_lower = plain.lower()
    q_lower = (query or "").lower().strip()
    i = t_lower.find(q_lower)

    # build window
    if i == -1:
        # no match: first ~2*radius characters
        chunk = plain[: 2 * radius]
        safe_chunk = escape(chunk)
        return (safe_chunk + "…") if len(chunk) == 2 * radius else safe_chunk

    start = max(0, i - radius)
    end = min(len(plain), i + len(q_lower) + radius)
    chunk = plain[start:end]

    # Escape the entire chunk and then highlight only the escaped match
    escaped_chunk = escape(chunk)
    escaped_match = escape(plain[i : i + len(q_lower)])

    # Replace only the first occurrence to avoid multiple <b>
    highlighted = escaped_chunk.replace(escaped_match, f"<b>{escaped_match}</b>", 1)
    return highlighted


def _lesson_index_in_memory(topic_name: str, lesson_title: str) -> int | None:
    try:
        lessons = theory_cpp[topic_name].lessons
        for idx, l in enumerate(lessons):
            if l.title == lesson_title:
                return idx
    except KeyError:
        return None
    return None

async def search_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Entrar en modo búsqueda: pedimos el texto a buscar."""
    query = update.callback_query
    if query:
        await query.answer()
        await query.message.edit_text(
            "🔎 Escribe una palabra o frase para buscar en la teoría.\n\n"
            "Ejemplos: <code>vector</code>, <code>paso por referencia</code>",
            parse_mode="HTML"
        )
    else:
        await update.message.reply_text(
            "🔎 Escribe una palabra o frase para buscar en la teoría."
        )
    context.user_data[SEARCH_MODE_KEY] = True

async def handle_search_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Procesa el texto escrito en modo búsqueda y muestra resultados (página 1)."""
    if not context.user_data.get(SEARCH_MODE_KEY):
        return False  #not in search mode; let other handlers handle the message

    q = (update.message.text or "").strip()
    context.user_data.pop(SEARCH_MODE_KEY, None)

    if not q:
        await update.message.reply_text("Escribe alguna palabra para buscar 😊")
        return True

    # We save the query and page in user_data for pagination.
    context.user_data["search_query"] = q
    context.user_data["search_page"] = 0

    await _send_results(update, context)
    return True

def _fetch_results(q: str):
    like = f"%{q}%"
    session = SessionLocal()
    try:
        rows = (
            session.query(LessonModel, TopicModel)
            .join(TopicModel, LessonModel.topic_id == TopicModel.id)
            .options(joinedload(LessonModel.topic))
            .filter(
                (LessonModel.title.ilike(like)) |
                (LessonModel.content.ilike(like))
            )
            .order_by(TopicModel.name.asc(), LessonModel.title.asc())
            .all()
        )
        # we return ‘simple’ data to avoid using the session outside
        return [
            {
                "topic": top.name,
                "lesson_title": les.title,
                "lesson_content": les.content
            }
            for (les, top) in rows
        ]
    finally:
        session.close()

async def _send_results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = context.user_data.get("search_query", "")
    page = context.user_data.get("search_page", 0)

    results = _fetch_results(q)
    if not results:
        await update.message.reply_text(f"Sin resultados para «{q}».")
        return

    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    page_items = results[start:end]

    for r in page_items:
        topic = r["topic"] or ""
        title = r["lesson_title"] or ""
        # Escape title/subject to avoid tags in titles
        topic_safe = escape(topic)
        title_safe = escape(title)

        snippet = _snippet(r["lesson_content"] or "", q)

        idx = _lesson_index_in_memory(topic, title)
        if idx is not None:
            btn = InlineKeyboardButton("📖 Abrir lección", callback_data=f"lesson_{topic}_{idx}")
        else:
            btn = InlineKeyboardButton("📚 Ir al tema", callback_data=f"menu_topic_{topic}")

        text_line = f"• <b>{topic_safe}</b> — {title_safe}\n<i>{snippet}</i>"

        # Send the block and the button
        await update.message.reply_text(
            text_line,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[btn]])
        )


async def handle_search_pagination(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "search_next":
        context.user_data["search_page"] = context.user_data.get("search_page", 0) + 1
    elif query.data == "search_prev":
        context.user_data["search_page"] = max(0, context.user_data.get("search_page", 0) - 1)
    else:
        return

    # We delete the previous navigation message if you want a cleaner flow
    try:
        await query.message.delete()
    except Exception:
        pass

    # We are bringing back the list from the new page.
    # we use send_message to chat_id
    from telegram import Message
    chat_id = query.message.chat_id
    fake_update = Update(update.update_id, message=None)
    class DummyMsg:
        def __init__(self, bot, chat_id):
            self.bot = bot
            self.chat_id = chat_id
        async def reply_text(self, *args, **kwargs):
            return await context.bot.send_message(chat_id=self.chat_id, *args, **kwargs)
    fake_update.message = DummyMsg(context.bot, chat_id)
    await _send_results(fake_update, context)
