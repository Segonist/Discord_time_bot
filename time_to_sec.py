import datetime
import time


def discord_time_minus(year, month, day, hour, minute, utc, style):  # функция для орицательного UTC
    time_transformed = datetime.datetime(int(year), int(month), int(day), int(hour),
                                         int(minute))  # хз что это, но так надо
    time_sec = int(time.mktime(time_transformed.timetuple()))  # время в секундах
    time_sec = time_sec - 7200  # перевод в нулевой UTC
    time_sec = time_sec - (utc * 3600)  # перевод часов в секунды и оптимизация под UTC
    number_to_withdraw = '\<t:' + str(time_sec) + ':' + style + '>'  # добавление дискорд тега
    return number_to_withdraw  # возвращение результата


def discord_time_plus(year, month, day, hour, minute, utc, style):  # функция для положительного UTC
    time_transformed = datetime.datetime(int(year), int(month), int(day), int(hour),
                                         int(minute))  # хз что это, но так надо
    time_sec = int(time.mktime(time_transformed.timetuple()))  # время в секундах
    time_sec = time_sec - 7200  # перевод в нулевой UTC
    time_sec = time_sec + (utc * 3600)  # перевод часов в секунды и оптимизация под UTC
    number_to_withdraw = '\<t:' + str(time_sec) + ':' + style + '>'  # добавление дискорд тега
    return number_to_withdraw  # возвращение результата


def discord_time(year, month, day, hour, minute, style):  # функция для нулевого UTC
    time_transformed = datetime.datetime(int(year), int(month), int(day), int(hour),
                                         int(minute))  # хз что это, но так надо
    time_sec = int(time.mktime(time_transformed.timetuple()))  # время в секундах
    time_sec = time_sec - 7200  # перевод в нулевой UTC
    number_to_withdraw = '\<t:' + str(time_sec) + ':' + style + '>'  # добавление дискорд тега
    return number_to_withdraw  # возвращение результата
