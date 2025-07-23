from telegram import InlineKeyboardMarkup, InlineKeyboardButton

#mis archivos
from data.temas import temas_cpp
from data.teoria_cpp import teoria_cpp

saludos = ["hola", "buenas", "hey", "holi", "hello", "saludos", "qué tal", "start"]

async def start(update, context):
    buttons = [
        [InlineKeyboardButton("Aprender", callback_data="aprender")],
        [InlineKeyboardButton("Practicar", callback_data="practicar")]
    ]
    await update.message.reply_text(
        "¡Hola! ¿Qué quieres hacer?",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


async def manejar_texto(update, context):
    texto = update.message.text.lower().strip()
    if texto in saludos:
        await start(update, context)
    else:
        await update.message.reply_text("Usa los botones o /start para comenzar.")


async def manejar_callback(update, context):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "aprender":
        botones_temas = [
            [InlineKeyboardButton(tema, callback_data=f"teoria_{i}")]
            for i, tema in enumerate(temas_cpp)
        ]
        botones_temas.append([InlineKeyboardButton("⬅ Volver", callback_data="volver_menu")])
        await query.message.edit_text(
            "Elige un tema de C++ para aprender:",
            reply_markup=InlineKeyboardMarkup(botones_temas)
        )

    elif data.startswith("teoria_"):
        from handlers.teoria import mostrar_teoria  # Import diferido
        await mostrar_teoria(update, context)

    elif data == "practicar":
        botones_temas = [
            [InlineKeyboardButton(tema, callback_data=f"ejercicio_{i}")]
            for i, tema in enumerate(temas_cpp)
        ]
        botones_temas.append([InlineKeyboardButton("⬅ Volver", callback_data="volver_menu")])
        await query.message.edit_text(
            "Elige un tema para practicar:",
            reply_markup=InlineKeyboardMarkup(botones_temas)
        )

    elif data.startswith("ejercicio_"):
        from handlers.ejercicios import comenzar_practica
        await comenzar_practica(update, context)

    elif data == "volver_menu":
        await start(update, context)