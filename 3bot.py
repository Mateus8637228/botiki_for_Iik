from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


# Токен бота
TOKEN = "8533962934:AAEGn28Z_5ah2jTpNhSQOQ7C8G2azzYb86A"


# Инициализация
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


print("Бот бумеранг запущен...")


@dp.message_handler(commands=['start'])
async def startWork(message: types.Message):
   tid = message.chat.id
   welcome_text = "Привет! Я бот-бумеранг!\n\n"
   welcome_text += "Давай познакомимся! Как тебя зовут?"
   await bot.send_message(tid, welcome_text)


@dp.message_handler()
async def echoAll(message: types.Message):
   tid = message.chat.id
   user_text = message.text


   # не повторяем команды
   if user_text.startswith('/'):
       return


   # просто повторяем сообщение пользователя
   response = f"{user_text}, {user_text}..."
   await bot.send_message(tid, response)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
