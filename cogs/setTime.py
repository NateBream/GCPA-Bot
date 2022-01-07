import shutil
from discord.ext import commands
from player import *

class setTimeCog(commands.Cog, name="set time"):
    @commands.command()
    async def setTime(self, ctx, arg1, arg2):
        #log(ctx)
        player = arg1
        time = arg2
        path = getPlayer(player, 'times')
        if path != 0:
            wb = open(path, 'a+')
        else:
            similar = getSimilar(arg1)
            await ctx.send('```' + arg1 + " not found. Did you mean:\n" + similar[0][0]
                        + '\n' + similar[1][0] + '\n' + similar[2][0] + '```')
            return

        wb.write(time + '\n')
        msg = 'Time added\nPlayer: {0}\nTime: {1}\nMake sure the time is translated to server time (EST)'.format(player, time)
        wb.close()
        await ctx.send('```' + msg + '```')

    @setTime.error
    async def setTime_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Missing argument(s), correct usage:\n?addTime <player> <hh:mm>```')


def setup(bot):
    bot.add_cog(setTimeCog(bot))
