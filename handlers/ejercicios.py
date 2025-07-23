from data.ejercicios import ejercicios_por_tema
from data.temas import temas_cpp
from telegram.ext import ContextTypes
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

async def comenzar_practica(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    tema = context.user_data["tema_actual"]
    tipo = context.user_data["tipo_actual"]

    from random import shuffle

    ejercicios_filtrados = [e for e in ejercicios_por_tema[tema] if e["tipo"] == tipo]

    if not ejercicios_filtrados:
        botones = [
            [InlineKeyboardButton("📚 Elegir otro tipo", callback_data="elegir_tipo")],
            [InlineKeyboardButton("🏠 Volver al menú", callback_data="volver_menu")]
        ]
        await query.message.edit_text(
            f"⚠️ No hay ejercicios disponibles del tipo <b>{tipo}</b> para el tema <b>{tema}</b>.",
            reply_markup=InlineKeyboardMarkup(botones),
            parse_mode="HTML"
        )
        return

    shuffle(ejercicios_filtrados)
    context.user_data["indice_pregunta"] = 0
    context.user_data["ejercicios_filtrados"] = ejercicios_filtrados

    await enviar_pregunta(update, context)


async def enviar_pregunta(update, context):
    tema = context.user_data["tema_actual"]
    tipo = context.user_data["tipo_actual"]
    i = context.user_data["indice_pregunta"]

    ejercicios_filtrados = context.user_data["ejercicios_filtrados"]

    if i >= len(ejercicios_filtrados):
        await update.callback_query.message.edit_text("🏁 No hay más ejercicios de este tipo.")
        return

    ejercicio = ejercicios_filtrados[i]
    pregunta = ejercicio["pregunta"]

    # Tipo test con opciones
    if ejercicio["tipo"] == "test":
        import random

        opciones = ejercicio["opciones"].copy()
        random.shuffle(opciones)

        botones = [
            [InlineKeyboardButton(opcion, callback_data=f"resp_{i}")]
            for i, opcion in enumerate(opciones)
        ]

        botones.append(
            [InlineKeyboardButton("⬅ Volver al menú de práctica", callback_data="volver_a_tipo")]
        )

        context.user_data["opciones_actuales"] = opciones


        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"<b>Ejercicio tipo Test</b>\n\n{pregunta}",
            reply_markup=InlineKeyboardMarkup(botones),
            parse_mode="HTML"
        )

    else: #ejercicios de programar (tengo que pensar como ejecutarlos)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"<b>Ejercicio</b>\n\n{pregunta}",
            parse_mode="HTML"
        )
    



async def manejar_respuesta(update, context: ContextTypes.DEFAULT_TYPE):
    tema = context.user_data.get("tema_actual")
    if not tema:
        await update.message.reply_text("Usa /start y selecciona un tema para practicar.")
        return

    i = context.user_data["indice_pregunta"]
    ejercicio = context.user_data["ejercicios_filtrados"][i]
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
