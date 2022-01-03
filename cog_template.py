import discord
from discord.ext import commands

#Replace xxx with command name
class xxxCog(commands.Cog, name="xxx"):
    @commands.command()
    async def xxx(self):
        return


def setup(bot):
    #Dont forget this one
    bot.add_cogCog(xxx(bot))
