from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def category_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Работа", callback_data="category_work"),
        InlineKeyboardButton(text="Учёба", callback_data="category_study"),
        InlineKeyboardButton(text="Личное", callback_data="category_personal")
    )
    return builder.as_markup()
