from discord.ext import commands
import time_to_sec
import user_data
import config

bot = commands.Bot(command_prefix=config.settings['PREFIX'], case_insensitive=True)  # префикс,
bot.remove_command('help')  # удаление команды help для создания своей


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))  # проверка запуска бота


@bot.command()
async def help(ctx):
    await ctx.send('>>> 📖'
                   '\nПомощь по боту '
                   '\nРазделы: '
                   '\nℹ!mhelp - Основная информация '
                   '\n📄!chelp - Команды бота '
                   '\n✏!shelp - помощь по стилям времени '
                   '\n🚫!ehelp - частые ошибки')  # команда !help


@bot.command()
async def mhelp(ctx):
    return await ctx.send('>>> ℹ '
                          '\nБот предназначен для создания дат следующего типа - <t:1656667800:f> '
                          '\nТакая дата будет правильно отображаться у всех пользоваетелей, '
                          '\nБот работает как на сервере, так и в личных сообщениях.')  # основная помощь


@bot.command()
async def chelp(ctx):
    return await ctx.send('>>> 📄 '
                          '\nДля выбора часового пояса введите !utс "часовой пояс" '
                          '\nПример: !utc +2 '
                          '\nДля перевода вашей даты в команду, используйте !time "год" "месяц" "день" "час" "минута" '
                          '\nПример: !time 2022 01 06 15 20')  # помощь по командам


@bot.command()
async def shelp(ctx):
    return await ctx.send('>>> ✏ '
                          '\nУ времени в дискорде есть 7 стилей отображения. '
                          '\nВнизу указан символ который надо указывать в !style, и пример отображения'
                          '\nt   <t:1656667800:t> '
                          '\nT  <t:1656667800:T> '
                          '\nd  <t:1656667800:d> '
                          '\nD <t:1656667800:D> '
                          '\nf   <t:1656667800:f> '
                          '\nF  <t:1656667800:F> '
                          '\nR  <t:1656667800:R>')  # помощь по стилям отображения


@bot.command()
async def ehelp(ctx):
    return await ctx.send('>>> 🚫 '
                          '\nP - ошибка '
                          '\nS - возможное решение '
                          '\nP: дата/время оттображается не правильно '
                          '\nS: проверте часовой пояс, !utc; стиль ,!style '
                          '\nS²: проверте правильно ли вы ввели дату и время команды !time, !chelp '
                          '\nP: при вводе какой либо команды ничего не проискходит '
                          '\nS: проверьте правильно ли вы вводите команду '
                          '\nS²: возможно бот отключен. Статус можно проверить в профиле '
                          '\nP: любая другая ошибка '
                          '\nS: обратитесь ко мне в личные сообщения Segonist#4356')  # помощь по ошибкам


@bot.command()
async def utc(ctx, timezone=None):  # команда !utc
    author = ctx.message.author  # автор сообщения
    if timezone is None:  # если сообщение без аргументов
        if user_data.users_utc.get(author) is None:  # если часовой пояс не задан
            await ctx.send('Часовой пояс не задан. Подробнее: !сhelp')
        else:
            timezone = user_data.users_utc[author]  # получение часового пояса
            await ctx.send('Ваш часовой пояс: %s' % timezone)
    else:
        user_data.users_utc.update({author: timezone})  # запись часового пояса в файл
        print('%s utc:%s' % (author, timezone))  # большой брат следит за тобой
        await ctx.send('Ваш часовой пояс: %s' % timezone)  # сообщение с примером


@bot.command()
async def style(ctx, style=None):  # команда style
    author = ctx.message.author  # автор сообщения
    if style is None:  # если сообщение без аргументов
        if user_data.users_style.get(author) is None:  # если стиль не задан
            await ctx.send('Стиль не задан. Подробнее: !shelp')
        else:
            style = user_data.users_style[author]  # получение часового пояса
            await ctx.send('Ваш стиль: ' + style + '. Пример: <t:1656667800:' + style + '>')
    else:
        user_data.users_style.update({author: style})  # запись стиля в файл
        print('%s style:%s' % (author, style))  # большой брат следит за тобой
        await ctx.send('Пример выбранного стиля: <t:1656667800:' + style + '>')  # сообщение с примером


@bot.command(name='time')  # команда !time
async def _time(ctx, user_year, user_month, user_day, user_hour, user_minute):
    author = ctx.message.author  # автор сообщения
    if user_data.users_utc.get(author) is None:
        user_utc = 0
    else:
        user_utc = user_data.users_utc[author]  # получение часового пояса
    if user_data.users_style.get(author) is None:
        style = 'f'
    else:
        style = user_data.users_style[author]
    try:
        split = list(user_utc)  # разделение UTC на знак и значение
    except TypeError:
        pass
    try:
        if split[0] == '+':
            number_to_withdraw = time_to_sec.discord_time_plus(user_year, user_month, user_day, user_hour, user_minute,
                                                               int(split[1]), style)  # если UTC положительный
        elif split[0] == '-':
            number_to_withdraw = time_to_sec.discord_time_minus(user_year, user_month, user_day, user_hour, user_minute,
                                                                int(split[1]), style)  # если UTC отрицательный
    except UnboundLocalError:
        number_to_withdraw = time_to_sec.discord_time(user_year, user_month, user_day, user_hour,
                                                      user_minute, style)  # если UTC нулевой
    await ctx.send(number_to_withdraw)  # отправка результата


bot.run(config.settings['TOKEN'])  # запуск бота
