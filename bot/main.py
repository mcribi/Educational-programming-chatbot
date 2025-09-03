import logging
import queue
from logging.handlers import QueueHandler, QueueListener
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters,)
from handlers.menu import start, handle_callback, handle_text, cmd_suggest, cmd_suggestions, help_cmd, menu_cmd
from handlers.exercises import handle_response
from scripts.init_exercises import populate_exercises
from data.theory_loader import load_theory
from scripts.init_lessons import populate_lessons_from_loader
import db.models
from utils.db_logging import SQLAlchemyLogHandler
from db.base import Base
from db.database import engine, get_session
from handlers.code import (handle_code_message, cmd_run, cmd_submit, cmd_solution, cmd_hint, cmd_out, cmd_code_help)
from handlers.search import handle_search_text

# ---------- Global error handler for python-telegram-bot ----------
logger = logging.getLogger(__name__)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Catch unhandled exceptions from PTB handlers and send them to logging."""
    ctx = {}
    try:
        if isinstance(update, Update) and update.effective_user:
            ctx["user_id"] = update.effective_user.id
            ctx["username"] = update.effective_user.username
        # Keep this short to avoid huge rows
        ctx["update_snapshot"] = str(update)[:2000]
        if context and context.error:
            ctx["error_repr"] = repr(context.error)
    except Exception:
        pass

    # logger.exception attaches the traceback automatically
    logger.exception("Unhandled exception in Telegram handler", extra={"context": ctx})


# Route plain text either to 'answer exercise' or 'chat/search'
def _is_waiting_mcq(context: ContextTypes.DEFAULT_TYPE) -> bool:
    """True if the user is in a multiple-choice question awaiting a text answer (rare)
    or (more typical) if we want to treat the next tap as a response; we key on the
    presence of both the current exercise and its options in user_data."""
    ud = context.user_data
    return bool(ud.get("current_exercise") and ud.get("current_options"))



# async def route_text_or_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """
#     Routing rules:
#     1) If EXAM is active -> delegate to handle_text (there we capture code without backticks and suggestions).
#     2) If you are practising “code” (outside EXAM) -> handle_code_message.
#     3) If you are in a test and there are options loaded -> handle_response.
#     4) In any other case:
#        - try searching for concepts (handle_search_text)
#        - if it does not apply or there is no result, handle_text will manage it (registration, suggestions, greetings, etc.).
#     """
#     # Active exam: all text is processed by handle_text (code capture/suggestions/logging)
#     if context.user_data.get("exam", {}).get("active"):
#         await handle_text(update, context)
#         return

#     #  Practice outside of exams
#     if context.user_data.get("current_topic"):
#         if context.user_data.get("current_mode") == "code":
#             #Programming: we capture code (with/without cpp)
#             await handle_code_message(update, context)
#             return
#         else:
#             #Test: only if there is actually a question waiting (with options)
#             if _is_waiting_mcq(context):
#                 await handle_response(update, context)
#                 return
#             #If there is no question waiting, we treat the text as a search or chat.

#     # Generic text: first try searching for concepts, if not, menu.handle_text
#     try:
#         handled = await handle_search_text(update, context)  # should return True/False if you implemented that pattern
#         if handled:
#             return
#     except TypeError:
#         # If your handle_search_text does not return bool, simply try and continue.
#         await handle_search_text(update, context)
#         return

#     # If it was not a valid search, let menu.handle_text handle it (suggestions, registration, greetings, etc.).
#     await handle_text(update, context)

async def route_text_or_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # suggestions 
    if context.user_data.get("awaiting_suggestion"):
        await handle_text(update, context)
        return

    # active exam
    if context.user_data.get("exam", {}).get("active"):
        await handle_text(update, context)
        return

    # practise
    if context.user_data.get("current_topic"):
        mode = context.user_data.get("current_mode")
        if mode == "code":
            await handle_code_message(update, context)
            return
        else:
            #test
            if _is_waiting_mcq(context):
                await handle_response(update, context) #answer the question
                return
            else:
                await handle_text(update, context)
                return

    # generic text, we try searching, then not to handle_text
    try:
        handled = await handle_search_text(update, context) 
        if handled:
            return
    except TypeError:
        await handle_search_text(update, context)
        return

    await handle_text(update, context)


async def handle_search_text_guarded(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Run search only when we are NOT in suggestion flow, not in exam,
    and not in a practice flow. Otherwise, do nothing and let the
    other handlers respond.
    """
    if context.user_data.get("awaiting_suggestion"):
        return
    if context.user_data.get("exam", {}).get("active"):
        return
    if context.user_data.get("current_topic"):
        return
    # Safe to run search now
    await handle_search_text(update, context)


if __name__ == "__main__":
    
    Base.metadata.create_all(bind=engine)

    #Logging: queue, background listener, DB handler 
    q = queue.SimpleQueue()

    db_handler = SQLAlchemyLogHandler()
    db_handler.setLevel(logging.WARNING)  # store WARNING+ in DB
    db_handler.setFormatter(logging.Formatter("%(message)s"))  # keep DB messages clean

    # Send all logs to the queue (non-blocking for the bot)
    queue_handler = QueueHandler(q)
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(queue_handler)

    # Also log to console while developing
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter("%(asctime)s — %(levelname)s — %(name)s — %(message)s"))
    root.addHandler(console)

    # Background thread that drains the queue and writes to DB
    listener = QueueListener(q, db_handler, respect_handler_level=True)
    listener.start()

    # Route Python warnings into logging (optional)
    logging.captureWarnings(True)

    #Initial data population (after logging is ready)
    try:
        populate_exercises()
        populate_lessons_from_loader(load_theory)
    except Exception:
        logger.exception("Error during initial population", extra={"context": {"phase": "populate"}})

    # Telegram bot
    from config import TOKEN

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))

    # Commands (code mode, suggest...)
    app.add_handler(CommandHandler("run", cmd_run))
    app.add_handler(CommandHandler("submit", cmd_submit))
    app.add_handler(CommandHandler("solution", cmd_solution))
    app.add_handler(CommandHandler("hint", cmd_hint))
    app.add_handler(CommandHandler("out", cmd_out))
    app.add_handler(CommandHandler("codehelp", cmd_code_help))
    app.add_handler(CommandHandler("suggest", cmd_suggest))
    app.add_handler(CommandHandler("suggestions", cmd_suggestions))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("menu", menu_cmd))

    # principal router
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, route_text_or_answer))
    
    #app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_search_text_guarded))


    # Hook the global error handler
    app.add_error_handler(error_handler)

    logger.info("Bot starting…")
    print("Bot running…")

    try:
        app.run_polling()
    finally:
        # Ensure the logging listener shuts down cleanly
        listener.stop()
