import discord
from discord.ext import commands
import datetime
import random
import matplotlib.pyplot as plt
import openpyxl
import os
from player import *

class getTime(commands.Cog, name="gets time"):
    @commands.command()
    async def getTime(self, ctx, arg1):
        path = getPlayer(arg1, 'times')
        if path != 0:
            wb = open(path, 'r')
        else:
            similar = getSimilar(arg1)
            await ctx.send('```' + arg1 + " not found. Did you mean:\n" + similar[0][0]
                        + '\n' + similar[1][0] + '\n' + similar[2][0] + '```')
            return

        lines = wb.readlines()
        
        count = [0] * 24
        for t in lines:
            splt = t.split(":")
            if splt[0] != '\n':
                count[int(splt[0])] = count[int(splt[0])] + 1
            
            
        yAxis = list(count)
        xAxis = range(0, 24)
        plt.figure(figsize=(8,6))
        plt.ylabel('Spies Per Hour')
        plt.title(arg1)
        plt.xlabel('Hours')
        plt.xticks(xAxis)
        plt.bar(xAxis, yAxis)
        plt.savefig('time.png')

        await ctx.send(file=discord.File('time.png'))
        os.remove('time.png')
        wb.close()
        
        


def setup(bot):
    bot.add_cog(getTime(bot))
