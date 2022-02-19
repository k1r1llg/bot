import asyncio
import logging
import aioschedule
# import DBwork
from _multiprocessing import send
from faulthandler import is_enabled
#import noti

import schedule
from Tools.scripts.finddiv import process

from aiogram import Bot, Dispatcher, executor, types
from datetime import date, time
import time
# import DBwork
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import TelegramObject

from murkups import mainMenu, trainingMenu, choosing_what_muscles_Menu, set_time_menu, set_time_callback_menu, mail_menu
from aiogram.types import message
from aiogram.utils.markdown import text
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler
import os



bot = Bot(token="2047866716:AAFVUm0e1lnt_PWuYuQAEMHK6W_7SJUMJqo")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

#data = " "
user_id = 665724594
#what_muscles = "back"


async def notif(what_muscles):
    # await bot.send_message(text="тренировка!!!", chat_id=user_id)
    if (what_muscles == "arms"):
        await bot.send_message(text="для рук", chat_id=user_id)
    elif (what_muscles == "legs"):
        await bot.send_message(text="для ног", chat_id=user_id)
    elif (what_muscles == "back"):
        await bot.send_message(text="упражнения для спины", chat_id=user_id)


async def scheduler(data, what_muscles):
    aioschedule.every(data).seconds.do(notif, what_muscles=what_muscles)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


'''
async def notif():
    await bot.send_message(text="тренировка!!", chat_id=665724594)

async def scheduler():
    aioschedule.every().day.at("13:18").do(notif)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(_):
    asyncio.create_task(scheduler())
'''


# ----------------/start-----------

@dp.message_handler(commands="start")
async def say_hello(message: types.Message):
    await message.reply("Привет!\nЯ помогаю продуктивно заниматься спортом", reply_markup=mainMenu)


#                                   ----------------main_menu-----------
@dp.message_handler()
async def main_screen(message: types.Message):
    what_muscles = "legs"
    if message.text == "Тренировки 💪🏻":
        await message.answer("Этот раздел для ...", reply_markup=trainingMenu)
    elif message.text == "Информация о боте":
        await message.answer(
            "Тренер - Бот находится в разработке, скоро будет добавлен новый функционал.\nЕсли Вы хотите помочь в "
            "разработке или знаете, как улучшить наш продукт, пожалуйста, обращайтесь на эту почту:\n",
            reply_markup=mail_menu)

    #                                    ----------------trainings_menu-----------

    elif message.text == "Назад":
        await message.answer("Вернулись назад", reply_markup=mainMenu)
    elif message.text == "Запланировать тренировку":
        await message.answer("Выберите группу мышц", reply_markup=choosing_what_muscles_Menu)

    #                                    ----------------choose_muscles_menu-----------

    elif message.text == "Руки":
        await message.answer("Упражнения для рук", reply_markup=set_time_menu)
        what_muscles = "arms"
    elif message.text == "Ноги":
        await message.answer("упражнения для ног", reply_markup=set_time_menu)
        what_muscles = "legs"
        #user_id = message.from_user.id
        # await DBwork.trainings_add_first(date="None", time="None", user_id=user_id, type_of_exercise="Ноги")
    elif message.text == "Спина":
        await message.answer("упражнения для спины", reply_markup=set_time_menu)
        what_muscles = "back"
        #user_id = message.from_user.id
        # error = await DBwork.trainings_add_first(date="None", time="None", user_id=user_id, type_of_exercise="Спина")
    elif message.text == "Назад":
        await message.answer("Вернулись назад", reply_markup=mainMenu)

    #                                    ----------------set_time_menu-----------

    elif message.text == "Выбрать время для тренировки":
        await message.answer("выберите время")
        pass
    else:
        #global user_id
        user_id = message.from_user.id
        #global data
        '''global data
        data = message.text
        new_data = data
        data = '"'
        data = data + new_data + '"'
        print(data)'''
        data = 10
        notif(what_muscles)
        scheduler(10, what_muscles)
        '''
        async def notif():
            # await bot.send_message(text="тренировка!!!", chat_id=user_id)
            if (what_muscles == "arms"):
                await bot.send_message(text="для рук", chat_id=user_id)
            elif (what_muscles == "legs"):
                await bot.send_message(text="для ног", chat_id=user_id)
            elif (what_muscles == "back"):
                await bot.send_message(text="упражнения для спины", chat_id=user_id)

        async def scheduler():
            aioschedule.every(data).seconds.do(notif)
            while True:
                await aioschedule.run_pending()
                await asyncio.sleep(1)
        '''

async def on_startup(_):
    asyncio.create_task(scheduler(10, what_muscles))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
