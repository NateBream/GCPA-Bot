import datetime
import sys
import traceback
from os import listdir
from os.path import isfile, join

import discord
from discord.ext import commands
from config import *
from botToken import *

bot = commands.Bot(command_prefix=BOT_PREFIX, case_insensitive=True, help_command=None,
                   activity=discord.Activity(name='?help'))



if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir(COGS_DIR) if isfile(join(COGS_DIR, f))]:
        try:
            bot.load_extension(COGS_DIR + "." + extension)
            print("Extension loaded", extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("?help for Commands"))


@bot.event
async def on_message(message):
    currentDT = datetime.datetime.now()
    f = open("bot.log", "a+")
    msg = '{0}\t{1}\t{2}\n'.format(currentDT.strftime("%Y-%m-%d %H:%M:%S"), message.content, message.author)
    f.write(msg)
    f.close()

    if not message.author.bot and message.content.find('\n') > 1:
        multi = message.content.split('\n')
        for msg in multi:
            message.content = msg
            await bot.process_commands(message)
        return

    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    currentDT = datetime.datetime.now()
    f = open("bot.log", "a+")
    msg = '{0}\t{1}\t{2}\t{3}\n'.format(currentDT.strftime("%Y-%m-%d %H:%M:%S"), ctx.message.content,
                                        ctx.message.author, error)
    f.write(msg)
    f.close()
    if isinstance(error, commands.CommandNotFound):
        msg = 'Command "{0}" not found.\nTry ?help for the commands'.format(ctx.message.content)
        await ctx.send('```' + msg + '```')
        return
    else:
        msg = 'There was an error with "{}"'.format(ctx.message.content)
        await ctx.send('```' + msg + '```')
    raise error


bot.run(TOKEN, bot=True, reconnect=True)
