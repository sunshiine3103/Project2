import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config.settings import settings
from utils.logger import setup_logger
from middlewares.throttling import ThrottlingMiddleware
from routers import commands, handlers

async def main():
    setup_logger()
    
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    
    # Middlewares
    dp.update.middleware(ThrottlingMiddleware())
    
    # Routers
    dp.include_router(commands.router)
    dp.include_router(handlers.router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
