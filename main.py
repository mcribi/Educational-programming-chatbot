from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from handlers.menu import start, handle_callback, handle_text
from handlers.exercises import handle_response
from scripts.init_exercises import populate_exercises

populate_exercises() # Initialize exercises

# To decide whether the user is answering an exercise or chatting
async def route_text_or_answer(update, context):
    if "current_topic" in context.user_data:
        await handle_response(update, context)
    else:
        await handle_text(update, context)


if __name__ == "__main__":
    from config import TOKEN

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, route_text_or_answer))

    print("Bot running...")
    app.run_polling()
