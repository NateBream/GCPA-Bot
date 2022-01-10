import shutil
from PIL import Image
from pytesseract import pytesseract
import discord
import re
import os
from discord.ext import commands
from player import *
import requests


class ImageAnalyzerCog(commands.Cog, name="auto adds times based off spy report"):
    @commands.command()
    async def spies(self, ctx):
        image = None
        msg = None
        try:
            url = ctx.message.attachments[0].url
        except IndexError:
            await ctx.send("No image provided!")
        else:
            if url[0:26] == "https://cdn.discordapp.com":
                image = requests.get(url, stream=True)

        if image is None:
            await ctx.send('```Uh oh... No image found...```')

        imageName = "current_image.png"

        with open(imageName, 'wb') as out_file:
            shutil.copyfileobj(image.raw, out_file)

        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image_path = r"./current_image.png"
        img = Image.open(image_path)
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)
        os.remove(image_path)

        text_elements = text.split('\n')
        coordinates = []
        times = []
        msg = ""
        counter = 0
        for element in text_elements:
            substring = re.search("action on (.*)", element)
            if substring is not None:
                coordinate = re.sub("[^0-9:]", "", substring.group(1))
                if coordinate is None or coordinate == "\n" or coordinate ==" " or coordinate == "":
                    continue
                else:
                    print(coordinate)
                    coordinates.append(coordinate)

            substring_time = re.search('Space Control (.*)', element)
            if substring_time is not None:
                first_regex = substring_time.group(1).split(' ')[-1]
                time = re.sub("[^0-9:]", "", first_regex)

                if time is None or time == "\n" or time == " " or time == "":
                    continue
                else:
                    print(time)
                    times.append(time)

        count = len(coordinates)
        count1 = len(times)
        print(count)
        print(count1)
        for coordinate in coordinates:
            if coordinate is not None and coordinates.index(coordinate) is not None:
                msg += "coordinate: {0} with a time stamp of: {1}\n\n".format(coordinate, times[counter])
                counter += 1
            else:
                msg = "Something went wrong while applying Regex..."

        await ctx.send('```' + msg + '```')

    @spies.error
    async def spies_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Missing argument(s), correct usage:\n?```')

def setup(bot):
    # Dont forget this one
    bot.add_cog(ImageAnalyzerCog(bot))
