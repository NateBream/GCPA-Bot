import os

from discord.ext import commands


class ListPlayersCog(commands.Cog, name="Lists all players"):
    @commands.command()
    async def listPlayers(self, ctx):
        x = os.listdir("players/coords")
        msg = "Players:"
        lst = []
        for file in x:
            y = file.split('.')
            lst.append(y[0])
        lst.sort()
        for file in lst:
            msg = msg + '\n' + file
        await ctx.send('```' + msg + '```')


def setup(bot):
    bot.add_cog(ListPlayersCog(bot))
