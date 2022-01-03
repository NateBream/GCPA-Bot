from discord.ext import commands


class HelpCog(commands.Cog, name="Displays info about commands"):
    @commands.command()
    async def help(self, ctx):
        msg = '''    #########################
    #    Uni2 Bot v1.0.1    #
    #########################
    Changlog:
    -Made things work I think
    #########################
    Upcoming Feautures:
    -Flight Time Calculator
    #########################
    Created By: Arcaenus#3492
    Created With: Python 3.6.7 and discord.py 1.1.1
    #########################
    Commands:

    ?setCoord <player> <coord> <moon>
    ?addCoord <player> <coord> <moon>
    Sets coordinates and moon for a player. Moon size is optional
    -------------------------
    ?addPlayer <player>
    Creates a player file
    -------------------------
    ?deletePlayer <player>
    Deletes a players file
    -------------------------
    ?listPlayers
    Lists all players with files
    -------------------------
    ?addTime <player> <time>
    ?setTime <player> <time>
    Adds a time a player is online. Use 24hr time and game time (EST). Only use hour and minute
    Ex: ?addTime sandman09 15:00
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
