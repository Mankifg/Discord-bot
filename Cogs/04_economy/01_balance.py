import discord
from discord.ext import commands
from functions import *

import eco

class economyCog(commands.Cog, name="economy command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="bal", usage=" @username", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def bal(self, ctx, check: discord.Member = None):
        
        if check == None:
            userObj = ctx.author
        else:
            userObj = check  
            
        id = userObj.id    
               
        eco.create_account(id)
        user_data = eco.get_user_data(id)
        
        q = discord.Embed(title=f"{userObj.name.title()}'s total balance {round(user_data['money']+user_data['bank'])}")
                        
        q.add_field(name="Purse", value=user_data['money'], inline=True)
        q.add_field(name="Bank", value=user_data['bank'], inline=True)

        await ctx.send(embed=q)

def setup(bot: commands.Bot):
    bot.add_cog(economyCog(bot))
