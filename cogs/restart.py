import discord
from discord.ext import commands
import os

class RestartCog(commands.Cog, name="Restart"):
    @commands.command()
    @commands.has_any_role("Admin", "Dev")
    async def restart(self):
        os.system("./restartBot.sh")
        return

def setup(bot):
    bot.add_cog(RestartCog(bot))
