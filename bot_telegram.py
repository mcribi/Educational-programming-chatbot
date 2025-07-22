#librerias de telegram
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters


# Base de ejercicios:
# ejercicios = [
#     {
#         "pregunta": "¿Qué imprime este código en Python?\n\nprint(3 + 4 * 2)",
#         "respuesta": "11",
#         "explicacion": "Primero se evalúa 4*2 = 8, luego 3+8 = 11 (reglas de precedencia)."
#     }
# ]

#definimos los temas que va a tener el bot
temas_cpp = [
    "Variables y tipos de datos",
    "Condicionales",
    "Bucles",
    "Funciones",
    "Entrada y salida",
    "Vectores"
]

#Temas de teoria 
teoria_cpp = {
    "Variables y tipos de datos": "En C++ se declaran así: `int edad = 20;` o `float nota = 7.5;`",
    "Condicionales": "Se usan `if`, `else if`, `else`. Ejemplo:\n\nif (x > 0) {\n  cout << \"positivo\";\n}",
    "Bucles": "Bucles comunes:\n`for (int i=0; i<5; i++)`\n`while (condicion)`\n`do { } while`",
    "Funciones": "Ejemplo de función:\n`int suma(int a, int b) { return a + b; }`",
    "Entrada y salida": "Usamos `cin` y `cout`:\n`cin >> x;`\n`cout << x;`",
    "Vectores": "Usamos `#include <vector>` y luego:\n`vector<int> v = {1,2,3};`"
}

#Definimos una lista de saludos para que el usuario le indique al bot para empezar
saludos = ["hola", "buenas", "hey", "holi", "hello", "saludos", "qué tal", "start"]


# Estado temporal por usuario
# estado_usuarios = {}

#Función para empezar: puedes aprender (teoria) o practicar (ejercicios)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await mostrar_menu_principal(update) #mostramos las opciones que haya

#Funcion para que se muestre un menu, en vez de que el usuario tenga que escribirlo
async def mostrar_menu_principal(update):
    teclado = [["Aprender", "Practicar"]]
    reply_markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)
    await update.message.reply_text("¿Qué quieres hacer?", reply_markup=reply_markup)


#elegir opcion
async def manejar_opcion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower().strip()

    if texto in saludos:
        await mostrar_menu_principal(update)

    elif texto == "aprender":
        teclado = [[tema] for tema in temas_cpp] + [["volver"]]
        reply_markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)
        await update.message.reply_text("Elige un tema para aprender:", reply_markup=reply_markup)

    elif texto in [tema.lower() for tema in temas_cpp]:
        tema_original = next(t for t in temas_cpp if t.lower() == texto)
        texto_teoria = teoria_cpp[tema_original]
        teclado = [[tema] for tema in temas_cpp] + [["volver"]]
        reply_markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)
        await update.message.reply_text(texto_teoria, reply_markup=reply_markup)

    elif texto == "practicar":
        await update.message.reply_text("Pronto podrás practicar con ejercicios interactivos.")
        await mostrar_menu_principal(update)

    elif texto == "volver":
        await mostrar_menu_principal(update)

    else:
        await update.message.reply_text("No entendí eso. Usa /start o selecciona una opción.")

#programa principal
if __name__ == "__main__":
    import os

    TOKEN = "7841287040:AAFYlfoFPP42I0ogqdvIaSvYYanM3GelnKo"  #token de telegram

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_opcion))

    print("Bot running...")
    app.run_polling()

