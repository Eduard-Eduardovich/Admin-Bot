import aiogram
import asyncio 
import os
from aiogram import Router, F
from aiogram import Bot, Dispatcher,types
from dotenv import load_dotenv
from handlers import user_handlers
import keyboards


       
async def main():
    load_dotenv('.env')
    token = os.getenv("TOKEN")
    bot = Bot(token)
    dp = Dispatcher()

    dp.include_routers(user_handlers.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


