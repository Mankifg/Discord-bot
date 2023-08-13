import discord
from discord.ext import commands
from functions import *

import eco

class profileCog(commands.Cog, name="bank commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="deposit", usage="", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def deposit(self, ctx, value):

        try:
            value = int(value)
        except:
            q = discord.Embed(title=f"Invalid value", description=f"", color=discord.Color.red())
            return
        
        id = ctx.author.id
              
        eco.create_account(id)
        user_data = eco.get_user_data(id)
        
        if user_data['money'] < value:
            q = discord.Embed(title=f"You're too poor", description=f"You need {value-user_data['money']} more", color=discord.Color.red())
            return


        user_data['money'] -= value
        user_data['bank'] += value
    
        q = discord.Embed(title=f"Balance: {round(user_data['money']+user_data['bank'])}")
                        
        q.add_field(name="Purse", value=user_data['money'], inline=True)
        q.add_field(name="Bank", value=user_data['bank'], inline=True)

        await ctx.send(embed=q)
        

def setup(bot: commands.Bot):
    bot.add_cog(profileCog(bot))