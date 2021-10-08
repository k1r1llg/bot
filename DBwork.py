import datetime
import random
import sqlite3
from contextlib import closing
from time import sleep, gmtime, strftime


def get_content(type_of_exercise, request):
    list_of_response = []
    with closing(sqlite3.connect('data.db')) as connection:
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT * FROM exercises WHERE type_of_exercise = ?
                       """, (type_of_exercise,))
        # получаем все значения
        all_info = cursor.fetchall()
        if request == "exercises":
            for info in all_info:
                list_of_response.append(info[1])
        if request == 'description':
            for info in all_info:
                list_of_response.append(info[2])
        if request == "href_video":
            for info in all_info:
                list_of_response.append(info[3])
        return list_of_response


def trainings_add(date, time, user_id):
    # Написать зпись тренировки (упражнения и в какой день)
    date_reform = ""
    for v in date:
        if v == " ":
            date_reform += "-"
        else:
            date_reform += v

    upload_data = (user_id, time, date_reform)
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(
        """
            INSERT INTO Notification
            VALUES (?, ? , ?)
     """, upload_data
    )
    connection.commit()
    cursor.close()


def notifications():
    # Идея для реализации такая: получать раз в 1 минут наличие тренировки в следущую минуты у пользователей из списка
    pass


if __name__ == '__main__':
    # date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    # print(date.split(" "))
    while True:
        time_now = datetime.datetime.time(datetime.datetime.now())
        time = time_now.strftime('%H:%M')
        date = datetime.datetime.now().strftime('%d-%m-%Y')
        zp = datetime.datetime.now().second
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("""
                              SELECT * FROM Notification WHERE Time = ? and date = ?
                              """, (time, date))
        all_info = cursor.fetchall()
        sleep(60.0 - zp)
