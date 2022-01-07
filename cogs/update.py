import discord
from discord.ext import commands
import os

class UpdateCog(commands.Cog, name="Update"):
    @commands.command()
    @commands.has_any_role("Admin", "Dev")
    async def update(self):
        os.system("./updateBot.sh")
        return

def setup(bot):
    bot.add_cog(UpdateCog(bot))
