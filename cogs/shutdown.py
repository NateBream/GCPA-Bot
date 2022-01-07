import discord
from discord.ext import commands
import os

class ShutdownCog(commands.Cog, name="Shutdown"):
    @commands.command()
    @commands.has_any_role("Admin")
    async def shutdown(self):
        os.system("./shutdownBot.sh")
        return

def setup(bot):
    bot.add_cog(ShutdownCog(bot))
