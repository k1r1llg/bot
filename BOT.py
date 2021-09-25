import logging
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="2047866716:AAFVUm0e1lnt_PWuYuQAEMHK6W_7SJUMJqo")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def say_hello(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Руки", "Спина", "Ноги"]
    keyboard.add(*buttons)
    await message.reply(
        "Привет!\nЯ помогаю продуктивно заниматься спортом\nДля начала выберите на какую группу мышц Вы нацелены в первую очередь.",
        reply_markup=keyboard)


if __name__ == '__main__':
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
