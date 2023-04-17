import logging
import random

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6205855916:AAGBBnelZsdCeSYeNhEDtvXg76pNj9Rbhhg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Угадайте число от одного до десяти!")



@dp.message_handler()
async def echo(message: types.Message):
    num = 3
    number = random.randrange(0, 10)
    while True:
        if int(message.text) == number:
            await message.answer("Вы угадали!")
        elif num <= 0:
            await message.answer("Исчерпали вы все попытки!")
        else:
            num -= 1
            await message.answer(f"Не правильно! У вас есть еще {num} попытки")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)