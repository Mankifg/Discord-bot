from logging.config import IDENTIFIER
import discord
from discord.ext import commands
import json
import random

pathToBank = './data/bank.json'

def get_bank_data():
    with open(pathToBank, 'r') as f:
        return json.load(f)

def save_to_bank(data):
    with open(pathToBank, 'w') as f:
        json.dump(data, f)

def create_account(id):
    id = str(id)
    users = get_bank_data()

    
    if id in users:
        return 
    else:
        users[id] = {}
        users[id]['wallet'] = 0
        users[id]['bank'] = 0
    
    save_to_bank(users)

    return 

    

class balCog(commands.Cog, name="ping command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="bal", usage="", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def bal(self, ctx):
        create_account(ctx.author.id) 

        users = get_bank_data()
        user = users[str(ctx.author.id)]
        wallet = user['wallet']
        bank = user['bank']
        q = discord.Embed(title="Balance", color=discord.Color.random())
        q.add_field(name="Wallet", value=wallet, inline=True)
        q.add_field(name="Bank", value=bank, inline=True)
        await ctx.send(embed=q)
    
    @commands.command(name="beg", usage="", description="")
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def beg(self, ctx):
        create_account(ctx.author.id)
        
        users = get_bank_data()

        get_money = random.randrange(1, 100)

        users[str(ctx.author.id)]['wallet'] += get_money

        
        await ctx.send(f"You got {get_money}€.")
        save_to_bank(users)
    
def setup(bot: commands.Bot):
    bot.add_cog(balCog(bot))