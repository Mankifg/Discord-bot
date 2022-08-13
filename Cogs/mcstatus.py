from dis import disco
import discord
from discord.ext import commands
import random
import os
import requests
import json
import base64


link = "https://api.mcsrvstat.us/2/"

class McstatusCog(commands.Cog, name="ping command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="mcstatus", usage=" [server ip]", 
    description="Ping minecraft server using api.mcsrvstat.us", 
    alias=['mcs']
    )
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def mcstatus(self, ctx, server):
        resp = requests.get(link + server).text
        data = json.loads(resp)
        q = discord.Embed(title="Server Status", description="", color=discord.Color.random())
        #q.set_thumbnail(url=data["icon"])


        #q.add_field(name=f"Server name: " + data["hostname"], value=f"Hosted from: {data["ip"]}", inline=False)

        q.add_field(name="Players", value=str(data["players"]["online"]) + "/" + str(data["players"]["max"]), inline=False)
        q.add_field(name="Version", value=data["version"], inline=False)
        q.add_field(name="Ping", value=data["debug"]["ping"], inline=False)
        q.add_field(name="Status", value=data["online"], inline=False)
        q.add_field(name="Motd", value=data["motd"], inline=False)
        q.set_footer(text="Server Status")
        await ctx.send(embed=q)
        

        
def setup(bot: commands.Bot):
    bot.add_cog(McstatusCog(bot))