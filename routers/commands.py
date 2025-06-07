from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.reply import main_menu

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "🚀 Добро пожаловать в To-Do Organizer Bot!\n"
        "Используйте /help для списка команд",
        reply_markup=main_menu()
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "📋 Доступные команды:\n"
        "/add - Добавить задачу\n"
        "/list - Список задач\n"
        "/complete - Завершить задачу\n"
        "/remind - Установить напоминание\n"
        "/export - Экспорт задач в файл"
    )
