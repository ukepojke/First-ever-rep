import logging

from aiogram import Bot, executor, Dispatcher, types

API_TOKEN = "6205855916:AAGBBnelZsdCeSYeNhEDtvXg76pNj9Rbhhg"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

main_button = types.ReplyKeyboardMarkup()
main_button.add(types.KeyboardButton("🏄‍♀️Спорт"),types.KeyboardButton("🎨Творчество"),types.KeyboardButton("👨‍🍳Кулинория"),types.KeyboardButton("👰‍♀️Повседневность"))

second_button = types.InlineKeyboardMarkup()
second_button.add(types.InlineKeyboardButton("🏄‍♀️Спорт", callback_data="lol"))

@dp.message_handler(commands=("start"))
async def user_m(message: types.Message):
    await message.answer("Выберите список заданий,который вам надо будет сделать!", reply_markup=second_button)

@dp.callback_query_handler(lambda callback_query: callback_query.data == 'lol')
async def process_callback(callback_query: types.CallbackQuery):
    # Обработка события
    await bot.send_message(callback_query.from_user.id, "Вы нажали кнопку!")

@dp.message_handler()
async def nothing(message: types.Message):
    if message.text == "lol":
        await message.answer("hello")




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)