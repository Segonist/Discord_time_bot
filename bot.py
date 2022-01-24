from discord.ext import commands
import time_to_sec
import user_data
import config
import help_text

bot = commands.Bot(command_prefix=config.settings['PREFIX'], case_insensitive=True)  # префикс, пох на регистр
bot.remove_command('help')  # удаление команды help для создания своей


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))  # проверка запуска бота


@bot.command()
async def help(ctx):
    await ctx.send('>>> 📖 ' + help_text.ru_text.get('help'))  # команда !help


@bot.command()
async def mhelp(ctx):
    return await ctx.send('>>> ℹ ' + help_text.ru_text.get('mhelp'))  # основная помощь


@bot.command()
async def chelp(ctx):
    return await ctx.send('>>> 📄 ' + help_text.ru_text.get('chelp'))  # помощь по командам


@bot.command()
async def shelp(ctx):
    return await ctx.send('>>> ✏ ' + help_text.ru_text.get('shelp'))  # помощь по стилям отображения


@bot.command()
async def ehelp(ctx):
    return await ctx.send('>>> 🚫 ' + help_text.ru_text.get('ehelp'))  # помощь по ошибкам


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
async def style(ctx, format_style=None):  # команда style
    author = ctx.message.author  # автор сообщения
    if format_style is None:  # если сообщение без аргументов
        if user_data.users_style.get(author) is None:  # если стиль не задан
            await ctx.send('Стиль не задан. Подробнее: !shelp')
        else:
            format_style = user_data.users_style[author]  # получение часового пояса
            await ctx.send('Ваш стиль: ' + format_style + '. Пример: <t:1656667800:' + format_style + '>')
    else:
        user_data.users_style.update({author: format_style})  # запись стиля в файл
        print('%s style:%s' % (author, format_style))  # большой брат следит за тобой
        await ctx.send('Пример выбранного стиля: <t:1656667800:' + format_style + '>')  # сообщение с примером


@bot.command(name='time')  # команда !time
async def _time(ctx, year, month, day, hour, minute):
    global number_to_withdraw, split
    author = ctx.message.author  # автор сообщения
    if user_data.users_utc.get(author) is None:
        user_utc = 0
    else:
        user_utc = user_data.users_utc[author]  # получение часового пояса
    if user_data.users_style.get(author) is None:
        format_style = 'f'
    else:
        format_style = user_data.users_style[author]
    try:
        split = list(user_utc)  # разделение UTC на знак и значение
    except TypeError:
        pass
    try:
        if split[0] == '+':
            number_to_withdraw = time_to_sec.discord_time_plus(year, month, day, hour, minute,
                                                               int(split[1]), format_style)  # если UTC положительный
        elif split[0] == '-':
            number_to_withdraw = time_to_sec.discord_time_minus(year, month, day, hour, minute,
                                                                int(split[1]), format_style)  # если UTC отрицательный
    except UnboundLocalError:
        number_to_withdraw = time_to_sec.discord_time(year, month, day, hour,
                                                      minute, style)  # если UTC нулевой
    await ctx.send(number_to_withdraw)  # отправка результата


bot.run(config.settings['TOKEN'])  # запуск бота
