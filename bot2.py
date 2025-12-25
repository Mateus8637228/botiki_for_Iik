import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType

BOT_TOKEN = "8492013380:AAFy5ktZJv4MVm8Itp9g3lT14SOCGzqFcfE"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=ContentType.VOICE)
async def handle_voice(message: types.Message):
    await message.reply("✅ Получил ваше голосовое сообщение!")

@dp.message_handler(content_types=[
    ContentType.TEXT,
    ContentType.PHOTO,
    ContentType.VIDEO,
    ContentType.DOCUMENT,
    ContentType.AUDIO,
    ContentType.STICKER,
    ContentType.VIDEO_NOTE,
    ContentType.ANIMATION,
    ContentType.CONTACT,
    ContentType.LOCATION,
    ContentType.POLL,
    ContentType.DICE
])
async def ignore_other_messages(message: types.Message):
    # Ничего не делаем - игнорируем сообщение
    pass

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
