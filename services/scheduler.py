from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.triggers.date import DateTrigger
from datetime import datetime, timedelta
from aiogram import Bot
import logging

# Инициализация планировщика
scheduler = AsyncIOScheduler(
    jobstores={
        'default': SQLAlchemyJobStore(url='sqlite:///storage/reminders.db')
    },
    timezone="Europe/Moscow"
)

def setup_scheduler():
    """Запуск планировщика при старте бота"""
    try:
        if not scheduler.running:
            scheduler.start()
            logging.info("Scheduler started successfully")
    except Exception as e:
        logging.error(f"Scheduler startup error: {e}")

async def send_reminder(chat_id: int, task_text: str, bot: Bot):
    """Функция отправки напоминания"""
    try:
        await bot.send_message(chat_id, f"⏰ Напоминание: {task_text}")
    except Exception as e:
        logging.error(f"Failed to send reminder: {e}")

def schedule_reminder(task_id: int, chat_id: int, task_text: str, reminder_time: datetime, bot: Bot):
    """Создание задания в планировщике"""
    try:
        scheduler.add_job(
            send_reminder,
            trigger=DateTrigger(run_date=reminder_time),
            args=(chat_id, task_text, bot),
            id=f"reminder_{task_id}_{chat_id}",
            replace_existing=True
        )
        logging.info(f"Scheduled reminder for task {task_id} at {reminder_time}")
    except Exception as e:
        logging.error(f"Error scheduling reminder: {e}")

def cancel_reminder(task_id: int, chat_id: int):
    """Отмена запланированного напоминания"""
    try:
        job_id = f"reminder_{task_id}_{chat_id}"
        if scheduler.get_job(job_id):
            scheduler.remove_job(job_id)
            logging.info(f"Cancelled reminder for task {task_id}")
    except Exception as e:
        logging.error(f"Error cancelling reminder: {e}")

def get_user_reminders(chat_id: int):
    """Получение списка активных напоминаний пользователя"""
    return [job for job in scheduler.get_jobs() 
            if f"reminder__{chat_id}" in job.id]
