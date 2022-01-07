import discord
import os
from discord.ext import commands
from player import *

class RenameCog(commands.Cog, name="Renames a player"):
    @commands.command()
    async def rename(self, ctx, arg1, arg2):
        path = getPlayer(arg1, 'coords')
        path2 = getPlayer(arg1, 'times')
        #path3 = getPlayer(arg1, 'playerinfo')
        player = arg2
        
        if path != 0:
            os.rename(path, 'players/coords/' + player + '.txt')
        else:
            wb = open('players/coords/' + player + '.txt', 'w+')
            wb.close()
        
        if path2 != 0:
            os.rename(path2, 'players/times/' + player + '.txt')
        else:
            wb = open('players/times/' + player + '.txt', 'w+')
            wb.close()
            
#        if path3 != 0:
#            os.rename(path3, 'players/playerinfo/' + arg2 + '.json')
#        else:
#            with open('players/playerinfo/' + player + '.json', 'w') as outfile:
#                json.dump(player_info, outfile)
#                outfile.close()

                
        await ctx.send('```Renamed ' + arg1 + ' to ' + player + '```')
        
    @rename.error
    async def rename_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Missing argument(s), correct usage:\n?rename <old name> <new name>```')

def setup(bot):
    #Dont forget this one
    bot.add_cog(RenameCog(bot))
