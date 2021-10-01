import logging
from tkinter import Text

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import message
from aiogram.utils.markdown import text

bot = Bot(token="2047866716:AAFVUm0e1lnt_PWuYuQAEMHK6W_7SJUMJqo")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def say_hello(message: types.Message):
    keyboard = types.InlineKeyboardMarkup();
    keyboard.add(types.InlineKeyboardButton(text="Спина", callback_data="but_back"))
    keyboard.add(types.InlineKeyboardButton(text="Руки", callback_data="but_arms"))
    keyboard.add(types.InlineKeyboardButton(text="Ноги", callback_data="but_legs"))
    await message.reply("Привет!\nЯ помогаю продуктивно заниматься спортом\nДля начала выберите на какую группу мышц Вы нацелены в первую очередь.", reply_markup=keyboard)
    #await message.reply("привет")


@dp.callback_query_handler(text="but_arms")
async def send_for_arms(call: types.CallbackQuery):
    await call.message.answer("Упражнения для рук:\nhttps://www.youtube.com/watch?v=9nxp8P4INJU")
    keyboard = types.InlineKeyboardMarkup();
    keyboard.add(types.InlineKeyboardButton(text="Понедельник", callback_data="choose_days_mnd"))
    keyboard.add(types.InlineKeyboardButton(text="Вторник", callback_data="choose_days_tue"))
    keyboard.add(types.InlineKeyboardButton(text="Среда", callback_data="choose_days_wnd"))
    keyboard.add(types.InlineKeyboardButton(text="Четверг", callback_data="choose_days_thur"))
    keyboard.add(types.InlineKeyboardButton(text="Пятница", callback_data="choose_days_fri"))
    keyboard.add(types.InlineKeyboardButton(text="Суббота", callback_data="choose_days_sat"))
    keyboard.add(types.InlineKeyboardButton(text="Воскресенье", callback_data="choose_days_sun"))
    await call.message.answer("В какие дни недели вы хотите заниматься?", reply_markup=keyboard)


@dp.callback_query_handler(text="but_legs")
async def send_for_arms(call: types.CallbackQuery):
    await call.message.answer("Упражнения для ног:")
    keyboard = types.InlineKeyboardMarkup();
    keyboard.add(types.InlineKeyboardButton(text="Понедельник", callback_data="choose_days_mnd"))
    keyboard.add(types.InlineKeyboardButton(text="Вторник", callback_data="choose_days_tue"))
    keyboard.add(types.InlineKeyboardButton(text="Среда", callback_data="choose_days_wnd"))
    keyboard.add(types.InlineKeyboardButton(text="Четверг", callback_data="choose_days_thur"))
    keyboard.add(types.InlineKeyboardButton(text="Пятница", callback_data="choose_days_fri"))
    keyboard.add(types.InlineKeyboardButton(text="Суббота", callback_data="choose_days_sat"))
    keyboard.add(types.InlineKeyboardButton(text="Воскресенье", callback_data="choose_days_sun"))
    await call.message.answer("В какие дни недели вы хотите заниматься?", reply_markup=keyboard)

@dp.callback_query_handler(text="but_back")
async def send_for_arms(call: types.CallbackQuery):
    await call.message.answer("Упражнения для спины:")
    keyboard = types.InlineKeyboardMarkup();
    keyboard.add(types.InlineKeyboardButton(text="Понедельник", callback_data="choose_days_mnd"))
    keyboard.add(types.InlineKeyboardButton(text="Вторник", callback_data="choose_days_tue"))
    keyboard.add(types.InlineKeyboardButton(text="Среда", callback_data="choose_days_wnd"))
    keyboard.add(types.InlineKeyboardButton(text="Четверг", callback_data="choose_days_thur"))
    keyboard.add(types.InlineKeyboardButton(text="Пятница", callback_data="choose_days_fri"))
    keyboard.add(types.InlineKeyboardButton(text="Суббота", callback_data="choose_days_sat"))
    keyboard.add(types.InlineKeyboardButton(text="Воскресенье", callback_data="choose_days_sun"))
    await call.message.answer("В какие дни недели вы хотите заниматься?", reply_markup=keyboard)


if __name__ == '__main__':
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)