from data.ejercicios import ejercicios_por_tema
from data.temas import temas_cpp
from telegram.ext import ContextTypes
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

async def comenzar_practica(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    i = int(query.data.split("_")[1])
    tema = temas_cpp[i]

    # Guardamos estado del usuario
    context.user_data["tema_actual"] = tema
    context.user_data["indice_pregunta"] = 0

    await enviar_pregunta(update, context)

async def enviar_pregunta(update, context: ContextTypes.DEFAULT_TYPE):
    tema = context.user_data["tema_actual"]
    i = context.user_data["indice_pregunta"]

    pregunta = ejercicios_por_tema[tema][i]["pregunta"]

    await update.callback_query.message.edit_text(
        f"Ejercicio del tema: <b>{tema}</b>\n\n{pregunta}",
        parse_mode="HTML"
    )

async def manejar_respuesta(update, context: ContextTypes.DEFAULT_TYPE):
    tema = context.user_data.get("tema_actual")
    if not tema:
        await update.message.reply_text("Usa /start y selecciona un tema para practicar.")
        return

    i = context.user_data["indice_pregunta"]
    ejercicio = ejercicios_por_tema[tema][i]
    respuesta_usuario = update.message.text.strip().lower()

    if respuesta_usuario == ejercicio["respuesta"].lower():
        await update.message.reply_text("✅ ¡Correcto!")
    else:
        await update.message.reply_text(f"❌ Incorrecto.\n\n<b>Explicación:</b> {ejercicio['explicacion']}", parse_mode="HTML")

    # Avanzar al siguiente ejercicio
    context.user_data["indice_pregunta"] += 1
    if context.user_data["indice_pregunta"] < len(ejercicios_por_tema[tema]):
        await enviar_pregunta(update, context)
    else:
        await update.message.reply_text("🏁 Has terminado los ejercicios de este tema.")
        context.user_data.clear()
