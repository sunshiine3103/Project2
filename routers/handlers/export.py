from aiogram import Router
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command
from datetime import datetime

from services.database import Database

router = Router()

@router.message(Command("export"))
async def export_tasks(message: Message):
    """Экспорт задач в текстовый файл"""
    db = Database()
    tasks = db.get_user_tasks(message.from_user.id)
    
    if not tasks:
        await message.answer("У вас нет задач для экспорта")
        return
    
    # Формирование текстового файла
    export_text = "📋 Ваши задачи:\n\n"
    for task in tasks:
        status = "✅" if task['is_completed'] else "⏳"
        export_text += (
            f"{status} {task['title']} "
            f"(Категория: {task['category']})\n"
            f"Дедлайн: {task['deadline'] or 'нет'}\n\n"
        )
    
    # Создание временного файла
    filename = f"tasks_export_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    file = BufferedInputFile(
        export_text.encode('utf-8'),
        filename=filename
    )
    
    await message.answer_document(
        file,
        caption="Ваши задачи экспортированы"
    )
