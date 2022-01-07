from discord.ext import commands


class HelpCog(commands.Cog, name="Displays info about commands"):
    @commands.command()
    async def help(self, ctx):
        msg = '''    #########################
    #    Uni2 Bot v2.0.0    #
    #########################
    Changlog:
    -Made things work 
    -Added alot of random functionality
    #########################
    Upcoming Feautures:
    -playerInfo function to show alliance info
    #########################
    Created By: Arc and BrotherVoid2
    #########################
    Commands:

    ?setCoord <player> <coord> <moon>
    ?addCoord <player> <coord> <moon>
    Sets coordinates and moon for a player. Moon size is optional. 
    Ex : ?setCoord BrotherVoid2 1:101:1
    -------------------------
    
    ?addPlayer <player>
    Creates a player file.
    -------------------------
    
    ?deletePlayer <player>
    Deletes a players file.
    -------------------------
    
    ?listPlayers
    Lists all players with active files
    -------------------------
    
    ?addTime <player> <time>
    ?setTime <player> <time>
    Adds a time a player is online. Use 24hr time and game time (EST). Only use hour and minute.
    Ex: ?addTime sandman09 15:00
    -------------------------
    
    ?setMoon <player> <coord>
    Gives the coordinate a moon. 
    Ex: ?setMoon Arc 1:59:12
    -------------------------
    
    ?rename <player> <new_name>
    Renames a player in the Database to a new name.
    Ex: ?rename Arc BrotherVoid2  
    -------------------------
    
    ?getCoords <player>
    Displays all coords/moons for a player
    -------------------------
    
    ?getTime <player>
    Displays an image showing all online times for a player
    -------------------------
    
    ?deleteCoord <player> <coord>
    Deletes a players coord
    -------------------------
    
    ?ping
    Displays the bots ping
    -------------------------
    
    ?help
    This command! Prints out info about bot and all commands
    #########################'''
        await ctx.send('```' + msg + '```')


def setup(bot):
    bot.add_cog(HelpCog(bot))
