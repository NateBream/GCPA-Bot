import os
from player import *
from discord.ext import commands


class DeletePlayerCog(commands.Cog, name="Deletes player"):
    @commands.command()
    async def deletePlayer(self, ctx, arg1):
        path = getPlayer(arg1, 'times')
        path2 = getPlayer(arg1, 'coords')
        flag = 0
        flag2 = 0
        msg = path
        if path != 0:
            try:
                os.remove(path)
                msg = "Player deleted"
            except:
                flag = 1

        if path2 != 0:
            try:
                os.remove(path2)
                msg = "Player deleted"
            except:
                flag2 = 1
        if flag + flag2 == 2:
            similar = getSimilar(arg1)
            await ctx.send('```' + arg1 + " not found. Did you mean:\n" + similar[0][0]
                        + '\n' + similar[1][0] + '\n' + similar[2][0] + '```')
            return
        if flag == 1 or flag2 == 1:
                msg = "Unknown error occured. Flag: " + str(flag) + "\nFlag2: " + str(flag2)
                #print(path)
                #print(path2)
        await ctx.send('```' + msg + '```')

    @deletePlayer.error
    async def deletePlayer_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Missing argument(s), correct usage:\n?deletePlayer <player>```')


def setup(bot):
    bot.add_cog(DeletePlayerCog(bot))
