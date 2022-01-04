import json
import shutil
from player import *
import openpyxl
from discord.ext import commands


class AddPlayerCog(commands.Cog, name="Adds player"):
    @commands.command()
    async def addPlayer(self, ctx, arg1):
        path = getPlayer(arg1, 'coords')
        path2 = getPlayer(arg1, 'times')
        path3 = getPlayer(arg1, 'playerinfo')
        player = arg1

        player_info = {
            "allies": [],
            "last_alliances": [],
            "timezone": "",
            "region_language": "",
            "coordinates": [],
            "times": []
        }

        if path == 0:
            wb = open('players/coords/' + player + '.txt', 'w+')
            wb.close()
        if path2 == 0:
            wb = open('players/times/' + player + '.txt', 'w+')
            wb.close()
        if path3 == 0:
            with open('players/playerinfo/' + player + '.json', 'w') as outfile:
                json.dump(player_info, outfile)
                outfile.close()

        msg = 'Added player {0}'.format(player)
        await ctx.send('```' + msg + '```')

    @addPlayer.error
    async def addPlayer_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Missing argument(s), correct usage:\n?addPlayer <player>```')


def setup(bot):
    bot.add_cog(AddPlayerCog(bot))
