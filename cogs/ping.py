import discord
from discord.ext import commands
import time


class ping(commands.Cog, name="ping"):
    @commands.command()
    async def ping(self, ctx):
        start = time.monotonic_ns()
        await ctx.send('```Pinging Server```')
        end = time.monotonic_ns()
        await ctx.send('```Ping: ' + str((end - start) / 1000000) + 'ms```')


def setup(bot):
    bot.add_cog(ping(bot))
