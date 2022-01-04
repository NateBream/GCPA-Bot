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
            # print(path)
            wb = open(path, 'r')
        else:
            # Get similar names
            similar = getSimilar(arg1)
            await ctx.send('```' + arg1 + " not found. Did you mean:\n" + similar[0][0]
                           + '\n' + similar[1][0] + '\n' + similar[2][0] + '```')
            return
        msg = "css\nKnown Planets for [" + player + "]:\n"  # css for orange coloring

        planets = wb.readlines()

        # Sort array
        planets.sort()
        # Format coord output message
        for line in planets:  # coords come in the format of "X:Y:Z MOON" from players < name.txt where moon = 1 if yes
            coordinates = line.split(' ')
            if len(coordinates) < 2:
                continue
            moon = int(coordinates[1])
            colony = coordinates[0]
            if moon > 0:
                moon = '[Yes]'
            else:
                moon = 'No'

            msg = msg + "\n{:<12}\t   Moon: {}".format(colony, moon)  # buffer of 12 because there is a possible
            # length of 11


        await ctx.send('```' + msg + '```')
        wb.close()

    @getCoords.error
    async def getCoords_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Missing argument(s), correct usage:\n?getCoords <player>```')


def setup(bot):
    bot.add_cog(GetCoordsCog(bot))
