import openpyxl
from discord.ext import commands
from player import *

class DeleteCoordCog(commands.Cog, name="Deletes Coord"):
    @commands.command()
    async def deleteCoord(self, ctx, arg1, arg2):
        coord = arg2
        player = arg1
        path = getPlayer(arg1, 'times')

        if path != 0:
            wb = open(path, 'r+')
        else:
            similar = getSimilar(arg1)
            await ctx.send('```' + arg1 + " not found. Did you mean:\n" + similar[0][0]
                        + '\n' + similar[1][0] + '\n' + similar[2][0] + '```')
            return


        lines = wb.readlines()
        i = 0
        flag = -1
        for c in lines:
            if c.split(' ')[0] == coord:
                flag = i
                break
            else:
                i = i + 1
        k = 0
        for c in lines:
            if k == i:
                continue
            else:
                wb.write(c + '\n')

        wb.close()

        msg = 'Coord Deleted\nPlayer: {0}\nCoord: {1}'.format(player, coord)
        await ctx.send('```' + msg + '```')

    @deleteCoord.error
    async def deleteCoord_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Missing argument(s), correct usage:\n?deleteCoord <player> <coord>```')


def setup(bot):
    bot.add_cog(DeleteCoordCog(bot))
