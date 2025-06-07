from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def main_menu() -> ReplyKeyboardMarkup:
    """
    Главное меню бота (reply-клавиатура)
    """
    builder = ReplyKeyboardBuilder()
    
    builder.row(
        KeyboardButton(text="📝 Добавить задачу"),
        KeyboardButton(text="📋 Список задач")
    )
    builder.row(
        KeyboardButton(text="⏰ Напоминания"),
        KeyboardButton(text="📤 Экспорт задач")
    )
    builder.row(
        KeyboardButton(text="ℹ️ Помощь")
    )
    
    return builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Выберите действие"
    )

def cancel_keyboard() -> ReplyKeyboardMarkup:
    """
    Клавиатура с одной кнопкой Отмена
    """
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="❌ Отмена"))
    return builder.as_markup(resize_keyboard=True)

def time_selection_keyboard() -> ReplyKeyboardMarkup:
    """
    Клавиатура для быстрого выбора времени
    """
    builder = ReplyKeyboardBuilder()
    
    builder.row(
        KeyboardButton(text="Через 1 час"),
        KeyboardButton(text="Через 3 часа")
    )
    builder.row(
        KeyboardButton(text="Завтра утром"),
        KeyboardButton(text="Вечером")
    )
    builder.row(
        KeyboardButton(text="❌ Без напоминания"),
        KeyboardButton(text="❌ Отмена")
    )
    
    return builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
