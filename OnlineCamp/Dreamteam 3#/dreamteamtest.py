from aiogram import Dispatcher, executor, types, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random

TOKEN_API = "6205855916:AAGBBnelZsdCeSYeNhEDtvXg76pNj9Rbhhg"


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

main_menu = InlineKeyboardMarkup()
main_menu.add(InlineKeyboardButton("🏄‍♀️quests", callback_data="/quests"),InlineKeyboardButton("🎲random quests",callback_data="/random_quests"),InlineKeyboardButton("🦸my quests",callback_data="/my_quests"),InlineKeyboardButton("🚪Выйти.",callback_data="/exit"))

second_menu = InlineKeyboardMarkup()
second_menu.add(InlineKeyboardButton("‍❤️Еще задание?",callback_data="/random_quests"),InlineKeyboardButton("🚪Выйти.",callback_data="/exit"))

quests = ["сделать 20 приседаний","написать письмо другу","прочитать главу книги","приготовить ужин",]
user_command = []

help_command = '''/quests - для того что бы выбрать конкретные задания!
/my_quests - что бы самому делать задания!
/random_quests - для случайных заданий!
/exit - выйти.
'''


@dp.message_handler(commands=["start"])
async def hello(message: types.Message):
    global help_command
    await message.answer(help_command,reply_markup=main_menu)
    await message.delete()

@dp.callback_query_handler()
async def user_answer(call: types.callback_query):
    global quests
    if call.data == "/random_quests":
        await bot.send_message(chat_id=call.from_user.id, text=random.choice(quests),reply_markup=second_menu)
    elif call.data == "/exit":
        await bot.send_message(chat_id=call.from_user.id, text="Пока!")
    elif call.data == "/quests":
        await bot.send_message(chat_id=call.from_user.id,text=f" Вот все задания - {quests}",reply_markup=main_menu)
    elif call.data == "/my_quests":
        await bot.send_message(chat_id=call.from_user.id,text="Хз как это функцию ебанную добавить")






if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)