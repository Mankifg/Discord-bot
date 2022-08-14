import discord
from discord.ext import commands
import asyncio
import aiosqlite
import json
import os
import random

pathToBank = './data/bank.db'

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user)]["wallet"] = 0
        users[str(user)]["bank"] = 0

        with open(pathToBank, 'w') as f:
            json.dump(users, f)
        
        return True

async def get_bank_data():
    with open(pathToBank, 'r') as f:
        users = json.load(f)

    return users

        
        
class EconomyCog(commands.Cog, name="ping command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="Economy", usage="", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def balance(self, ctx):
        await open_account(ctx.author)

        users = await get_bank_data()

        q = discord.Embed(title=f"{ctx.author.name}'s Balance", color=discord.Color.blue())
        q.add_field(name="Wallet", value=f"{users[str(ctx.author.id)]['wallet']}")
        q.add_field(name="Bank", value=f"{users[str(ctx.author.id)]['bank']}")
        q.set_thumbnail(url=ctx.author.avatar_url)

        await ctx.send(embed=q)

    #? beg for money   
    @commands.command(name="getUserData", usage="", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def beg(self, ctx):
        await open_account(ctx.author)
        users = await get_bank_data()
        earning = random.randrange(101)
        await ctx.send(f'You have earned {earning} coins!')
        users[str(ctx.author.id)]['wallet'] += earning 

        with open(pathToBank, 'w') as f:
            json.dump(users, f)      
        

def setup(bot: commands.Bot):
    bot.add_cog(EconomyCog(bot))