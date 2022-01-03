import shutil
from player import *
import openpyxl
from discord.ext import commands

template = 'Template.xlsx'


class addCoordCog(commands.Cog, name="Adds Coords"):
    @commands.command()
    async def addCoord(self, ctx, *, arg):
        splt = arg.split()
        player = splt[0]
        flag = 0
        count = -1
        coordList = [[-1 for i in range(2)] for j in range(len(splt))]

        wb = 0
        path = getPlayer(player, 'coords')
        if path != 0:
            wb = open(path, 'a+')
        else:
            similar = getSimilar(player)
            await ctx.send('```' + player + " not found." + '```')
            return
        wb.close()
        
        for g in splt:
            if count == -1:
                count += 1
                continue
            elif ':' in g and flag == 0:
                flag = 1
                coordList[count][0] = g
                coordList[count][1] = 0
                continue
            elif ':' in g and flag == 1:
                flag = 1
                coordList[count][1] = 0
                count += 1
                coordList[count][0] = g
                continue
            elif flag == 1:
                flag = 0
                coordList[count][1] = g
                count += 1
                continue
            else:
                await ctx.send('```Bad format. Moon sizes must follow after coords```')
                return


        for pair in coordList:
            c = pair[0]
            moon = pair[1]
            
            if c == -1:
                continue
            coord = c.split(':')
            if len(coord) != 3:
                await ctx.send('```Bad Coord format. Correct format: <galaxy>:<system>:<slot>' + '\nCoord: ' + c + '```')
                pair[0] = -1
                pair[1] = -1
                continue
            elif coord[0].isalpha() or coord[1].isalpha() or coord[2].isalpha():
                await ctx.send('```Bad Coord. Cannot use letters```')
                pair[0] = -1
                pair[1] = -1
                continue
            elif int(coord[0]) < 1 or int(coord[0]) > 2:
                await ctx.send('```Bad Coord. Out of possible range' + '\nCoord: ' + c + '```')
                pair[0] = -1
                pair[1] = -1
                continue
            elif int(coord[1]) < 1 or int(coord[1]) > 499:
                await ctx.send('```Bad Coord. Out of possible range' + '\nCoord: ' + c + '```')
                pair[0] = -1
                pair[1] = -1
                continue
            elif int(coord[2]) < 1 or int(coord[2]) > 15:
                await ctx.send('```Bad Coord. Out of possible range' + '\nCoord: ' + c + '```')
                pair[0] = -1
                pair[1] = -1
                continue
            if int(moon) > 9999:
                await ctx.send('```Invalid moon size```')
                pair[0] = -1
                pair[1] = -1
                continue
            if len(splt) < 2:
                await ctx.send('```Missing argument(s), correct usage:\n?setCoord <player> <coord> '
                               '<moon_size>\nOR\n?setCoord <player> <coord>```')
                return

        
        
        for pair in coordList:
            wb.close()
            wb = open(path, 'a+')

            f = open(path, 'r')
            lines = f.readlines()
            f.close()
            flag = 0
            if pair[0] == -1:
                continue
            if len(lines) == 0:
                wb.write(str(pair[0]) + ' ' + str(pair[1]) + '\n')
                msg = 'Coord set.\nCoord: {0}\nMoon: {1}'.format(str(pair[0]), str(pair[1]))
                await ctx.send('```' + msg + '```')
                continue
            for line in lines:
                coords = line.split(' ')
                if str(pair[0]) == str(coords[0]) and str(pair[1]) + '\n' == str(coords[1]):
                    msg = 'That coord already exists!\nCoord not added!\nCoord: {0}\nMoon: {1}'.format(str(pair[0]), str(pair[1]))
                    await ctx.send('```' + msg + '```')
                    flag = 0
                    break
                if str(pair[0]) == str(coords[0]) and str(pair[1]) == str(coords[1]):
                    msg = 'That coord already exists!\nCoord not added!\nCoord: {0}\nMoon: {1}'.format(str(pair[0]), str(pair[1]))
                    await ctx.send('```' + msg + '```')
                    flag = 0
                    break
                elif str(pair[0]) == str(coords[0]) and not int(pair[1]) == int(coords[1]) and int(pair[1]) >= 0:
                    i = 0
                    for c in lines:
                        if c.split(' ')[0] == str(pair[0]):
                            break
                        else:
                            i += 1
                    k = 0
                    wb.close()
                    os.remove(path)
                    wb = open(path, 'a')
                    for c in lines:
                        if k == i:
                            continue
                        else:
                            wb.write(c + '\n')
                    wb.write(str(pair[0]) + ' ' + str(pair[1]) + '\n')
                    msg = 'Moon Updated.\nCoord: {0}\nMoon: {1}'.format(str(pair[0]), str(pair[1]))
                    await ctx.send('```' + msg + '```')
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 1:
                wb.write(str(pair[0]) + ' ' + str(pair[1]) + '\n')
                msg = 'Coord set.\nCoord: {0}\nMoon: {1}'.format(str(pair[0]), str(pair[1]))
                await ctx.send('```' + msg + '```')
                    
                
            
        wb.close()
        


def setup(bot):
    bot.add_cog(addCoordCog(bot))

