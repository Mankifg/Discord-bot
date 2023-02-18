import discord
from discord.ext import commands
import os
import json
import requests
from dotenv import load_dotenv, find_dotenv
import random
from functions import get_color
import urllib.request


website = "https://api.nasa.gov/planetary/apod"

load_dotenv(find_dotenv())
key = os.getenv("NASA")

class ApodCog(commands.Cog, name="ping command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="apod", 
    usage=" for Astronaut Picture of The day", 
    description="Astronaut Picture of The day by Nasa", 
    alias=['APOD', 'apod']
    )

    @commands.cooldown(1, 2, commands.BucketType.member)
    async def apod(self, ctx):
        resp = requests.get(f"{website}?api_key={key}").json()

        try:
            author = resp["copyright"]
        except:
            author = ''
            
        date = resp["date"]
        explain = resp["explanation"]
        pic_url = resp["url"]
        title = resp["title"]

        try:
            explain = explain[0:200] + "..."
        except:
            explain = explain

        urllib.request.urlretrieve(pic_url, "./Photos/apod.png")

        q = discord.Embed(title="Astronomy Picture of the Day", description='', color=get_color("./Photos/apod.png"))
        q.add_field(name="Title: " + title , value="Author: " + author, inline=True)
        q.set_image(url=pic_url)
        q.add_field(name="Date: " + date,value='Desc: ' + explain , inline=False)
        q.set_footer(text="Using Nasa Api")
        await ctx.send(embed=q)

def setup(bot: commands.Bot):
    bot.add_cog(ApodCog(bot))