from datetime import datetime

def format_task(task: dict) -> str:
    """Форматирование задачи для вывода"""
    status = "✅" if task['is_completed'] else "🕒"
    deadline = ""
    if task['deadline']:
        deadline = f"\n⏰ До: {datetime.fromisoformat(task['deadline']).strftime('%d.%m.%Y %H:%M')}"
    return (
        f"{status} <b>{task['title']}</b>\n"
        f"📁 Категория: {task['category']}"
        f"{deadline}"
    )

def format_reminder(reminder: dict) -> str:
    """Форматирование напоминания"""
    return (
        f"🔔 Напоминание: {reminder['task_title']}\n"
        f"⏰ Время: {reminder['reminder_time']}"
    )
