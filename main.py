#librerias de telegram
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from handlers.menu import start, manejar_callback
from handlers.teoria import mostrar_teoria
from handlers.ejercicios import manejar_respuesta
from handlers.menu import manejar_texto

#para el manejador saber si esta en ejercicios o en teoria
async def manejar_texto_o_respuesta(update, context):
    texto = update.message.text.lower().strip()

    if "tema_actual" in context.user_data:
        # Está respondiendo a un ejercicio
        from handlers.ejercicios import manejar_respuesta
        await manejar_respuesta(update, context)
    else:
        # Es un mensaje libre (hola, volver, etc.)
        from handlers.menu import manejar_texto
        await manejar_texto(update, context)


#programa principal
if __name__ == "__main__":
    import os
    from config import TOKEN 

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(manejar_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_texto_o_respuesta))

    print("Bot running...")
    app.run_polling()

