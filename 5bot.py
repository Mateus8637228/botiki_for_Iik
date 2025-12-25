import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


TOKEN = "8568170968:AAGoFbr_kMZW0mbimfBo4q-UBytivF8FZM4"


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


print("✅ Бот запускается...")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
   await message.answer("✅ Бот работает! Напиши /email")


@dp.message_handler(commands=['email'])
async def get_email(message: types.Message):
   try:
       response = requests.get("https://reqres.in/api/users/2")
       if response.status_code == 200:
           email = response.json()['data']['email']
           await message.answer(f"📧 {email}")
       else:
           await message.answer(f"❌ API ошибка: {response.status_code}")
   except:
       await message.answer("❌ Ошибка запроса")


executor.start_polling(dp, skip_updates=True)
