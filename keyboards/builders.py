from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, KeyboardButton

def build_task_keyboard(tasks: list[dict], action: str = "select") -> InlineKeyboardBuilder:
    """
    Строит динамическую клавиатуру для списка задач
    :param tasks: Список задач из БД
    :param action: Тип действия (select/complete/delete)
    :return: InlineKeyboardBuilder
    """
    builder = InlineKeyboardBuilder()
    
    for task in tasks:
        builder.add(InlineKeyboardButton(
            text=f"{task['title']} ({task['category']})",
            callback_data=f"task_{action}_{task['id']}"
        ))
    
    # Добавляем кнопку отмены
    builder.row(InlineKeyboardButton(
        text="❌ Отмена",
        callback_data="cancel"
    ))
    
    return builder

def build_categories_keyboard(selected: str = None) -> InlineKeyboardBuilder:
    """
    Клавиатура выбора категории с отметкой выбранной
    :param selected: Выбранная категория (если есть)
    """
    categories = {
        "work": "Работа 💼",
        "study": "Учёба 📚", 
        "personal": "Личное 🏠"
    }
    
    builder = InlineKeyboardBuilder()
    
    for key, text in categories.items():
        prefix = "✅ " if key == selected else ""
        builder.add(InlineKeyboardButton(
            text=f"{prefix}{text}",
            callback_data=f"category_{key}"
        ))
    
    builder.adjust(1)  # По одной кнопке в ряд
    
    return builder
