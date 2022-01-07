import discord
from discord.ext import commands
import os

class ShutdownCog(commands.Cog, name="Shutdown"):
    @commands.command()
    @commands.has_any_role("Admin", "Dev")
    async def shutdown(self, ctx):
        os.system("./shutdownBot.sh")
        return

def setup(bot):
    bot.add_cog(ShutdownCog(bot))
