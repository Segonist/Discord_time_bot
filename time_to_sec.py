import datetime
import time


def discord_time_minus(user_year, user_month, user_day, user_hour, user_minute, utc, style):  # функция для орицательного UTC
    time_transformed = datetime.datetime(int(user_year), int(user_month), int(user_day), int(user_hour),
                                         int(user_minute))  # хз что это, но так надо
    time_sec = int(time.mktime(time_transformed.timetuple()))  # время в секундах
    time_sec = time_sec - 7200  # перевод в нулевой UTC
    time_sec = time_sec - (utc * 3600)  # перевод часов в секунды и оптимизация под UTC
    number_to_withdraw = '\<t:' + str(time_sec) + ':' + style + '>'  # добавление дискорд тега
    return number_to_withdraw  # возвращение результата


def discord_time_plus(user_year, user_month, user_day, user_hour, user_minute, utc, style):  # функция для положительного UTC
    time_transformed = datetime.datetime(int(user_year), int(user_month), int(user_day), int(user_hour),
                                         int(user_minute))  # хз что это, но так надо
    time_sec = int(time.mktime(time_transformed.timetuple()))  # время в секундах
    time_sec = time_sec - 7200  # перевод в нулевой UTC
    time_sec = time_sec + (utc * 3600)  # перевод часов в секунды и оптимизация под UTC
    number_to_withdraw = '\<t:' + str(time_sec) + ':' + style + '>'  # добавление дискорд тега
    return number_to_withdraw  # возвращение результата


def discord_time(user_year, user_month, user_day, user_hour, user_minute, style):  # функция для нулевого UTC
    time_transformed = datetime.datetime(int(user_year), int(user_month), int(user_day), int(user_hour),
                                         int(user_minute))  # хз что это, но так надо
    time_sec = int(time.mktime(time_transformed.timetuple()))  # время в секундах
    time_sec = time_sec - 7200  # перевод в нулевой UTC
    number_to_withdraw = '\<t:' + str(time_sec) + ':' + style + '>'  # добавление дискорд тега
    return number_to_withdraw  # возвращение результата
