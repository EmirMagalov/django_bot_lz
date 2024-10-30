import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from private import  user_private_router
from fsm import fsm
from admin import admin_router
load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(fsm)
dp.include_router(admin_router)

async def main():
    await dp.start_polling(bot)



try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("бот остановлен пользователем")