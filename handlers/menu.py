from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


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

    elif data == "practicar":
        botones_temas = [
            [InlineKeyboardButton(tema, callback_data=f"tema_{i}")]
            for i, tema in enumerate(temas_cpp)
        ]
        botones_temas.append([InlineKeyboardButton("⬅ Volver", callback_data="volver_menu")])
        await query.message.edit_text(
            "Elige un tema para practicar:",
            reply_markup=InlineKeyboardMarkup(botones_temas)
        )

    elif data == "volver_a_tipo":
        tema = context.user_data.get("tema_actual")
        if not tema:
            await update.callback_query.message.reply_text("⚠️ No hay tema activo. Usa /start.")
            return

        botones_tipos = [
            [InlineKeyboardButton("📝 Test", callback_data="tipo_test")],
            [InlineKeyboardButton("💻 Programar", callback_data="tipo_programar")],
            [InlineKeyboardButton("⬅ Volver al menú", callback_data="volver_menu")]
        ]

        await update.callback_query.message.reply_text(
            f"Has elegido <b>{tema}</b>.\n\n¿Qué tipo de ejercicio quieres hacer?",
            reply_markup=InlineKeyboardMarkup(botones_tipos),
            parse_mode="HTML"
        )

    elif data.startswith("teoria_"):
        from handlers.teoria import mostrar_teoria
        await mostrar_teoria(update, context)

    elif data.startswith("tema_"):
        i = int(data.split("_")[1])
        tema = temas_cpp[i]
        context.user_data["tema_seleccionado"] = tema

        botones_tipos = [
            [InlineKeyboardButton("📝 Test", callback_data="tipo_test")],
            [InlineKeyboardButton("💻 Programar", callback_data="tipo_programar")],
            [InlineKeyboardButton("⬅ Volver", callback_data="practicar")]
        ]
        await query.message.edit_text(
            f"Has elegido <b>{tema}</b>.\n\n¿Qué tipo de ejercicio quieres hacer:",
            reply_markup=InlineKeyboardMarkup(botones_tipos),
            parse_mode="HTML"
        )

    elif data.startswith("tipo_"):
        tipo = data.split("_")[1]
        tema = context.user_data.get("tema_seleccionado")

        if not tema:
            await query.message.edit_text("⚠️ Ocurrió un error. Por favor, vuelve a /start.")
            return

        context.user_data["tema_actual"] = tema
        context.user_data["tipo_actual"] = tipo
        context.user_data["indice_pregunta"] = 0

        from handlers.ejercicios import comenzar_practica
        await comenzar_practica(update, context)

    elif data.startswith("resp_"):
        from handlers.ejercicios import enviar_pregunta

        opcion_index = int(data[5:])
        i = context.user_data["indice_pregunta"]
        ejercicios = context.user_data["ejercicios_filtrados"]
        ejercicio = ejercicios[i]
        opciones = context.user_data["opciones_actuales"]
        opcion_seleccionada = opciones[opcion_index]
        respuesta_correcta = ejercicio["respuesta"]

        if opcion_seleccionada.lower() == respuesta_correcta.lower():
            texto_resultado = f"<b>{ejercicio['pregunta']}</b>\n\n✅ ¡Correcto!"
        else:
            texto_resultado = (
                f"<b>{ejercicio['pregunta']}</b>\n\n"
                f"❌ <b>Incorrecto</b>\n\n"
                f"<b>Explicación:</b> {ejercicio['explicacion']}"
            )

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=texto_resultado,
            parse_mode="HTML"
        )

        context.user_data["indice_pregunta"] += 1

        if context.user_data["indice_pregunta"] < len(ejercicios):
            await asyncio.sleep(0.5)
            await enviar_pregunta(update, context)
        else:
            botones_finales = [
                [InlineKeyboardButton("🔁 Practicar este tipo otra vez", callback_data="repetir_tipo")],
                [InlineKeyboardButton("📚 Elegir otro tipo", callback_data="elegir_tipo")],
                [InlineKeyboardButton("🏠 Menú principal", callback_data="volver_menu")]
            ]
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="🏁 Has terminado los ejercicios de este tipo. ¿Qué te gustaría hacer ahora?",
                reply_markup=InlineKeyboardMarkup(botones_finales)
            )

    elif data == "repetir_tipo":
        from handlers.ejercicios import comenzar_practica
        await comenzar_practica(update, context)

    elif data == "elegir_tipo":
        tema = context.user_data.get("tema_actual")
        if not tema:
            await query.message.edit_text("Ocurrió un error. Usa /start para volver al menú.")
            return

        botones_tipos = [
            [InlineKeyboardButton("📝 Test", callback_data="tipo_test")],
            [InlineKeyboardButton("💻 Programar", callback_data="tipo_programar")],
            [InlineKeyboardButton("⬅ Volver al menú", callback_data="volver_menu")]
        ]

        await query.message.edit_text(
            f"Has elegido <b>{tema}</b>.\n\n¿Qué tipo de ejercicio quieres hacer?",
            reply_markup=InlineKeyboardMarkup(botones_tipos),
            parse_mode="HTML"
        )

    elif data == "volver_menu":
        texto = "¿Qué quieres hacer?"
        botones = [
            [InlineKeyboardButton("Aprender", callback_data="aprender")],
            [InlineKeyboardButton("Practicar", callback_data="practicar")]
        ]

        if update.message:
            await update.message.reply_text(texto, reply_markup=InlineKeyboardMarkup(botones))
        else:
            await update.callback_query.message.reply_text(texto, reply_markup=InlineKeyboardMarkup(botones))
