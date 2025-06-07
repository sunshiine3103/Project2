from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from datetime import datetime, timedelta

from services.database import Database
from services.scheduler import scheduler
from keyboards.inline import confirm_keyboard
from states.reminder import SetReminder

router = Router()

@router.message(Command("remind"))
async def set_reminder_start(message: Message, state: FSMContext):
    """Начало установки напоминания"""
    await state.set_state(SetReminder.waiting_for_task)
    await message.answer("Выберите задачу для напоминания:")

@router.callback_query(SetReminder.waiting_for_task, F.data.startswith("task_"))
async def select_task_for_reminder(callback: CallbackQuery, state: FSMContext):
    """Обработка выбора задачи"""
    task_id = int(callback.data.split("_")[1])
    await state.update_data(task_id=task_id)
    await state.set_state(SetReminder.waiting_for_time)
    await callback.message.answer("Введите время напоминания (ЧЧ:ММ):")

@router.message(SetReminder.waiting_for_time, F.text.regexp(r'^\d{2}:\d{2}$'))
async def set_reminder_time(message: Message, state: FSMContext):
    """Установка времени напоминания"""
    time_str = message.text
    data = await state.get_data()
    
    try:
        # Парсинг времени и установка напоминания
        reminder_time = datetime.strptime(time_str, "%H:%M").time()
        db = Database()
        task = db.get_task(data['task_id'])
        
        # Добавление в планировщик
        scheduler.add_job(
            send_reminder,
            'date',
            run_date=datetime.combine(datetime.now(), reminder_time),
            args=(message.from_user.id, task['title'])
        )
        
        await message.answer(f"⏰ Напоминание установлено на {time_str}")
    except ValueError:
        await message.answer("Некорректный формат времени. Используйте ЧЧ:ММ")
    
    await state.clear()

async def send_reminder(chat_id: int, task_title: str):
    """Функция отправки напоминания"""
    bot = Bot.get_current()
    await bot.send_message(chat_id, f"⏰ Напоминание: {task_title}")
