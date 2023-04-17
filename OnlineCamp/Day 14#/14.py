import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import random

markup = ReplyKeyboardMarkup()
markup.add(KeyboardButton('Камень'), KeyboardButton('Ножницы'))


API_TOKEN = '6205855916:AAGBBnelZsdCeSYeNhEDtvXg76pNj9Rbhhg'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
ml = Dispatcher(bot)

choises = ['Камень', 'Ножницы', 'Бумага']

messagemarkup = InlineKeyboardMarkup()
messagemarkup.add(InlineKeyboardButton('🗿Камень', callback_data='Камень'), InlineKeyboardButton('✂️Ножницы', callback_data='Ножницы'), InlineKeyboardButton('📄Бумага', callback_data='Бумага'))

@ml.message_handler(commands=['start', "help"])
async def send_welcome(message: types.Message):
    await message.answer('Начинаем игру камень, ножницы, бумага', reply_markup=markup)
    await message.answer('Выберите одну из них', reply_markup=messagemarkup)


@ml.message_handler()
async def echo(message: types.Message):
    await message.answer('Прости ничего не умею')


@ml.callback_query_handler()
async def calldatadeffunc(call: types.callback_query):
    choise = random.choice(choises)
    if choise == call.data:
        await bot.send_message(chat_id=call.from_user.id, text='ничья')
    elif choise == 'Бумага' and call.data == 'Камень' or choise == 'Камень' and call.data == 'Ножницы' or choise == 'Ножницы' and call.data == 'Бумага':
        await bot.send_message(chat_id=call.from_user.id, text=f'Я выбрал {choise}\nВы проиграли 😢😢')
    elif call.data == 'Бумага' and choise == 'Камень' or call.data == 'Камень' and choise == 'Ножницы' or call.data == 'Ножницы' and choise == 'Бумага':
        await bot.send_message(chat_id=call.from_user.id, text=f'Я выбрал {choise}\nВы выйграли 🥳🥳')
    await bot.send_message(chat_id=call.from_user.id, text='Выберите одну из них', reply_markup=messagemarkup)


if __name__ == '__main__':
    executor.start_polling(ml, skip_updates=True)