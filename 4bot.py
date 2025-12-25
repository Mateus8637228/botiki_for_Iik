from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


# Токен бота
TOKEN = "8286215718:AAGL8qGgAkIomOox0OVxSZB4qaf-6skSTGg"


# Инициализация
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


print("Бот с удаляемой клавиатурой запущен...")


@dp.message_handler(commands=['start'])
async def startWork(message: types.Message):
   tid = message.chat.id


   # создаем клавиатуру
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   keyboard.row("Я никогда", "Не буду", "Копить")
   keyboard.row("Столько", "Долгов")
   keyboard.row("❌ Закрыть клавиатуру")


   welcome_text = "👋 Привет! Я создал клавиатуру с кнопками.\n\n"
   welcome_text += "Нажми на любую кнопку или напиши \"Закрыть\" чтобы убрать клавиатуру."


   await bot.send_message(tid, welcome_text, reply_markup=keyboard)


@dp.message_handler(lambda message: message.text.lower() == "закрыть")
async def closeKeyboard(message: types.Message):
   tid = message.chat.id


   # создаем пустую клавиатуру (удаляем клавиатуру)
   remove_keyboard = types.ReplyKeyboardRemove()


   response = "Клавиатура удалена!\n\n"
   response += "Напиши /start чтобы создать клавиатуру снова."


   await bot.send_message(tid, response, reply_markup=remove_keyboard)


@dp.message_handler(lambda message: message.text == "❌ Закрыть клавиатуру")
async def closeKeyboardButton(message: types.Message):
   tid = message.chat.id


   # создаем пустую клавиатуру (удаляем клавиатуру)
   remove_keyboard = types.ReplyKeyboardRemove()


   response = "Клавиатура удалена через кнопку!\n\n"
   response += "Напиши /start чтобы создать клавиатуру снова."


   await bot.send_message(tid, response, reply_markup=remove_keyboard)


@dp.message_handler(lambda message: message.text in ["Я никогда", "Не буду", "Копить", "Столько", "Долгов"])
async def handleButtons(message: types.Message):
   tid = message.chat.id
   button_text = message.text


   response = f"Вы нажали: {button_text}\n\n"
   response += "Напиши \"Закрыть\" или нажми ❌ чтобы убрать клавиатуру."


   await bot.send_message(tid, response)


@dp.message_handler()
async def handleOtherText(message: types.Message):
   tid = message.chat.id


   response = "Клавиатура активна!\n\n"
   response += "Напиши \"Закрыть\" чтобы убрать клавиатуру.\n"
   response += "Или нажми на одну из кнопок."


   await bot.send_message(tid, response)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
