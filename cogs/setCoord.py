import shutil
from os import listdir
import openpyxl
from discord.ext import commands
from player import *

template = 'Template.xlsx'


class SetCoordCog(commands.Cog, name="Adds Coords"):
    @commands.command()
    async def setCoord(self, ctx, *, arg):
        splt = arg.split()
        string = splt[1]
        coord = string.split(':')
        if len(coord) != 3:
            await ctx.send('```Bad Coord format. Correct format: <galaxy>:<system>:<slot>```')
            return
        elif coord[0].isalpha() or coord[1].isalpha() or coord[2].isalpha():
            await ctx.send('```Bad Coord. Cannot use letters```')
            return
        elif int(coord[0]) < 1 or int(coord[0]) > 2:
            await ctx.send('```Bad Coord. Out of possible range```')
            return
        elif int(coord[1]) < 1 or int(coord[1]) > 499:
            await ctx.send('```Bad Coord. Out of possible range```')
            return
        elif int(coord[2]) < 1 or int(coord[2]) > 15:
            await ctx.send('```Bad Coord. Out of possible range```')
            return
        if string[1:-1] == u'\U0001f4af':
            splt[1] = string[1] + ':100:' + string[-1]
        if len(splt) < 2:
            await ctx.send('```Missing argument(s), correct usage:\n?setCoord <player> <coord> '
                           '<moon_size>\nOR\n?setCoord <player> <coord>```')
            return
        elif len(splt) == 2:
            player = splt[0]
            coord = splt[1]
            moon = 0
        elif len(splt) == 3:
            player = splt[0]
            coord = splt[1]
            moon = splt[2]
        else:
            await ctx.send('```Too many arguments, correct usage:\n?setCoord <player> <coord> '
                           '<moon_size>\nOR\n?setCoord <player> <coord>```')
            return

        
        
        path = getPlayer(player, 'coords')
        if path != 0:
            wb = open(path, 'a+')
            #print(path)
        else:
            #print(path)
            similar = getSimilar(player)
            await ctx.send('```' + player + " not found. Did you mean:\n" + similar[0][0]
                        + '\n' + similar[1][0] + '\n' + similar[2][0] + '```')
            return


        f = open(path, 'r')
        lines = f.readlines()
        for line in lines:
            coords = line.split(' ')
            if coord == coords[0]:
                msg = 'That coord already exists for {0}!\nCoord not added!\nCoord: {1}\nMoon: {2}'.format(player,
                                                                                                           coord, moon)
                await ctx.send('```' + msg + '```')
                return
        
        
        wb.write(str(coord) + ' ' + str(moon) + '\n')

        msg = 'Coord set for {0}\nCoord: {1}\nMoon: {2}'.format(player, coord, moon)
        await ctx.send('```' + msg + '```')
        f.close()
        wb.close()


def setup(bot):
    bot.add_cog(SetCoordCog(bot))
