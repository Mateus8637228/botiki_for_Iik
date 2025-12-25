from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


TOKEN = "8533962934:AAEGn28Z_5ah2jTpNhSQOQ7C8G2azzYb86A"


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


print("✓ Бот запущен")
print("✓ Жду голосовые сообщения")
print("✓ Текст игнорируется")


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
   await message.answer("Отправь голосовое сообщение")


@dp.message_handler(content_types=['voice'])
async def voice_handler(message: types.Message):
   await message.answer("Голосовое получено!")


# Все остальные сообщения полностью игнорируем
@dp.message_handler()
async def empty_handler(message: types.Message):
   pass


if __name__ == "__main__":
   executor.start_polling(dp, skip_updates=True)

