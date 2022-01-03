import openpyxl
from discord.ext import commands
import os
from player import *

class GetCoordsCog(commands.Cog, name="Gets coord of player"):

    # Outputs coords for a player in chat
    # If player cannot be found, suggests
    # 3 most similar names
    @commands.command()
    async def getCoords(self, ctx, arg1):
        player = arg1

        # Get player path (returns 'players/player.xlsx')
        path = getPlayer(arg1, 'coords')
        if path != 0:
            #print(path)
            wb = open(path, 'r')
        else:
            # Get similar names
            similar = getSimilar(arg1)
            await ctx.send('```' + arg1 + " not found. Did you mean:\n" + similar[0][0]
                        + '\n' + similar[1][0] + '\n' + similar[2][0] + '```')
            return
        msg = "Coords for " + player + ":"

        lines = wb.readlines()

        # Sort array
        lines.sort()
        # Format coord output message
        for coord in lines:
            moon = coord.split(' ')
            if len(moon) < 2:
              continue
            moon[1] = int(moon[1])
            a = moon[0].split(':')
            a[0] = int(a[0])
            a[1] = int(a[1])
            a[2] = int(a[2])
            if a[1] < 10 and a[2] < 10:
                msg = msg + "\nCoord: {0}:{1}:{2}\t   Moon: {3}".format(a[0], a[1], a[2], moon[1])
            elif a[1] < 100 and a[2] < 10:
                msg = msg + "\nCoord: {0}:{1}:{2}\t  Moon: {3}".format(a[0], a[1], a[2], moon[1])
            elif a[1] < 100 or a[2] < 10:
                msg = msg + "\nCoord: {0}:{1}:{2}\t Moon: {3}".format(a[0], a[1], a[2], moon[1])
            else:
                msg = msg + "\nCoord: {0}:{1}:{2}\tMoon: {3}".format(a[0], a[1], a[2], moon[1])

        await ctx.send('```' + msg + '```')
        wb.close()

    @getCoords.error
    async def getCoords_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Missing argument(s), correct usage:\n?getCoords <player>```')


def setup(bot):
    bot.add_cog(GetCoordsCog(bot))
