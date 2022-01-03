import os
import random

from discord.ext import commands


class BeerMeCog(commands.Cog, name="Beer me Bitch"):
    @commands.command()
    async def BeerMe(self, ctx):
        msg = "One beefy Brewski on the way..."
        msg1 = "We are all out of brew! A riot is on the way!"
        msg2 = "You want a Stella?! You pussy. No beer for you!"
        msg3 = "Whats a beer? We drink borboun here..."
        msg4 = "Beer? you meant wild turkey 101. Coming right up..."
    
        msgList = [msg,msg1,msg2,msg3,msg4]
    
        await ctx.send('```' + random.choice(msgList) + '```')

def setup(bot):
    bot.add_cog(BeerMeCog(bot))
