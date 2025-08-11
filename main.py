from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from handlers.menu import start, handle_callback, handle_text
from handlers.exercises import handle_response
from scripts.init_exercises import populate_exercises

populate_exercises() # Initialize exercises

# To decide whether the user is answering an exercise or chatting
async def route_text_or_answer(update, context):
    if "current_topic" in context.user_data: #the user is answering an exercise
        await handle_response(update, context)
    else: #the user is chatting
        await handle_text(update, context)


if __name__ == "__main__":
    from config import TOKEN

    app = ApplicationBuilder().token(TOKEN).build() #create the bot with the token of telegram

    #Handlers:
    app.add_handler(CommandHandler("start", start)) #answer to the /start command
    app.add_handler(CallbackQueryHandler(handle_callback)) # answer to the callback queries (click on buttons)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, route_text_or_answer)) #text messages that are not commands (answering exercises or chatting)

    print("Bot running...")
    app.run_polling() #pooling mode: it checks for new messages in loop
