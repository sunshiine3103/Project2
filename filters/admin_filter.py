from aiogram import F
from aiogram.types import Message
from config import settings

def IsAdmin():
    return F.from_user.id.in_(settings.ADMIN_IDS)
