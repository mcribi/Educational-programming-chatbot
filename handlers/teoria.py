from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from data.temas import temas_cpp
from data.teoria_cpp import teoria_cpp

async def mostrar_teoria(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    i = int(query.data.split("_")[1])
    tema = temas_cpp[i]
    explicacion = teoria_cpp[tema]
    
    botones = [
        [InlineKeyboardButton("Elegir otro tema", callback_data="aprender")],
        [InlineKeyboardButton("Menú principal", callback_data="volver_menu")]
    ]
    
    await query.message.edit_text(explicacion, reply_markup=InlineKeyboardMarkup(botones), parse_mode="HTML")
