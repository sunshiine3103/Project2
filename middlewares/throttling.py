from aiogram import BaseMiddleware
from aiogram.types import Message
from datetime import datetime, timedelta
from cachetools import TTLCache

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: int = 1, ttl: int = 3):
        self.cache = TTLCache(maxsize=10_000, ttl=ttl)
        self.limit = limit

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        current_time = datetime.now()
        
        if user_id in self.cache:
            if self.cache[user_id] >= self.limit:
                await event.answer("Слишком много запросов! Подождите немного.")
                return
            self.cache[user_id] += 1
        else:
            self.cache[user_id] = 1
            
        return await handler(event, data)
