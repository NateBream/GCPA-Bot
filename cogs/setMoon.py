import shutil

import openpyxl
from discord.ext import commands
from player import *

class setMoonCog(commands.Cog, name="set moon"):
    @commands.command()
    async def setMoon(self, ctx, arg1, arg2):
        #log(ctx)
        player = arg1
        coordinates = str(arg2)
        path = getPlayer(arg1, 'coords')
        msg = ''
        if path != 0:
            wb = open(path, 'r')
        else:
            similar = getSimilar(arg1)
            await ctx.send('```' + arg1 + " not found. Did you mean:\n" + similar[0][0]
                        + '\n' + similar[1][0] + '\n' + similar[2][0] + '```')
            return

        lines = wb.readlines()

        for line in lines:
            index_line = lines.index(line)  # need for replacing in txt file soon
            line = line.split(' ')  # split for coordinates and moon
            if str(line[0]) == arg2:
                modified_line = '{} yes'.format(line[0])  # new line to be saved. coordinate + a 'yes'
                lines[index_line] = modified_line  # set that line
                msg = 'Moon added for {0} at location: {1}.'.format(player, coordinates)
                break
            else:
                continue

        wb.close()
        wb = open(path, 'w')  # now we want to rewrite that file with our new moon

        for line in lines:
            wb.write(line)
        wb.close()

        if msg == '':  # if we found no location our string will be empty.
            msg = 'The player: {0} does not have a location at: {1} according to our records.'.format(player, coordinates)
        await ctx.send('```' + msg + '```')

    @setMoon.error
    async def setMoon_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Missing argument(s), correct usage:\n?setMoon <player> <coordinate> <moonsize>```')


def setup(bot):
    bot.add_cog(setMoonCog(bot))
