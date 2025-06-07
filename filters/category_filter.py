from aiogram import F
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

class CategoryFilter(BaseFilter):
    def __init__(self, categories: list[str]):
        self.categories = categories

    async def __call__(self, update: Message | CallbackQuery) -> bool:
        if isinstance(update, CallbackQuery):
            return any(update.data.startswith(f"category_{cat}") for cat in self.categories)
        elif isinstance(update, Message):
            return update.text.lower() in self.categories
        return False
