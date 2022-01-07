import discord
from discord.ext import commands

#Replace xxx with command name
class xxxCog(commands.Cog, name="xxx"):
    @commands.command()
    async def xxx(self):
        return
        
    
    @xxx.error
    async def xxx_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Missing argument(s), correct usage:\n?```')


def setup(bot):
    #Dont forget this one
    bot.add_cog(xxxCog(bot))
