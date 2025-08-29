import logging
import queue
from logging.handlers import QueueHandler, QueueListener
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters,)
from handlers.menu import start, handle_callback, handle_text
from handlers.exercises import handle_response
from scripts.init_exercises import populate_exercises
from data.theory_loader import load_theory
from scripts.init_lessons import populate_lessons_from_loader
import db.models
from utils.db_logging import SQLAlchemyLogHandler
from db.base import Base
from db.database import engine, get_session
from handlers.code import (handle_code_message, cmd_run, cmd_submit, cmd_solution, cmd_hint, cmd_out, cmd_code_help)


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


# ---------- Route plain text either to 'answer exercise' or 'chat' ----------
async def route_text_or_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Route plain text:
    - If practicing and mode == 'code' -> try to capture code (handle_code_message).
    - If practicing and mode != 'code' -> multiple-choice flow (handle_response).
    - Else -> generic chat/menu text (handle_text).
    """
    if "current_topic" in context.user_data:
        if context.user_data.get("current_mode") == "code":
            await handle_code_message(update, context)
        else:
            await handle_response(update, context)
    else:
        await handle_text(update, context)


if __name__ == "__main__":
    
    Base.metadata.create_all(bind=engine)

    # ---------- Logging: queue -> background listener -> DB handler ----------
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

    # ---------- Initial data population (after logging is ready) ----------
    try:
        populate_exercises()
        populate_lessons_from_loader(load_theory)
    except Exception:
        logger.exception("Error during initial population", extra={"context": {"phase": "populate"}})

    # ---------- Telegram bot ----------
    from config import TOKEN

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))
    
    #code-mode commands
    app.add_handler(CommandHandler("run", cmd_run))
    app.add_handler(CommandHandler("submit", cmd_submit))
    app.add_handler(CommandHandler("solution", cmd_solution))
    app.add_handler(CommandHandler("hint", cmd_hint))
    app.add_handler(CommandHandler("out", cmd_out))
    app.add_handler(CommandHandler("codehelp", cmd_code_help))


    # Text router
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, route_text_or_answer))

    # Hook the global error handler
    app.add_error_handler(error_handler)

    logger.info("Bot starting…")
    print("Bot running…")

    try:
        app.run_polling()
    finally:
        # Ensure the logging listener shuts down cleanly
        listener.stop()
