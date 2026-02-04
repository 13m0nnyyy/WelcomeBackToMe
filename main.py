import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

API_TOKEN = "8083855809:AAEEWBI0R9DlKSDLJxw7GhR0ouLRABkLeB4"

bot = Bot(token=API_TOKEN)
dp = Dispatcher

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("бота запущено")

async def main ():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())