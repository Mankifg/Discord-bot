import discord
from discord.ext import commands
from functions import *

import eco



class profileCog(commands.Cog, name="profile command"):
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

        #todo id od pošitelja ali userja ki ga je mentuono  
        
        eco.create_account(id)
        user_data = eco.get_user_data(id)
        
        q = discord.Embed(title=f"{userObj.name.title()}'s total balance {round(user_data['money']+user_data['bank'])}")
                        
        q.add_field(name="Purse", value=user_data['money'], inline=True)
        q.add_field(name="Bank", value=user_data['bank'], inline=True)

        await ctx.send(embed=q)
        
    @commands.command(name="profile", usage=" @username", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def profile(self, ctx, check: discord.Member = None):
    
        if check == None:
            userObj = ctx.author
        else:
            userObj = check  
            
        id = userObj.id

        eco.create_account(id)
        user_data = eco.get_user_data(id)
        
        q = discord.Embed(title=f"{userObj.name.title()}'s profile")
                        
        q.add_field(name="Purse", value=user_data['money'], inline=True)
        q.add_field(name="Bank", value=user_data['bank'], inline=True)
        items = user_data["backpack"]["items"]
        valuable = sorted(items, key=lambda x:x['value'], reverse=True)#[:2]
        d = []
        [d.append(item['name'].title()) for item in valuable]
        s = ""
        for i in range (5):
            try:
                s+=f"**{d[i]}**, "
            except IndexError:
                pass
        timestamp = user_data['data']['date_joined']
        q.add_field(name=f"Items: {len(items)}", value=f"{s[:-2]}.", inline=False)
        q.add_field(name="Joined", value=f"<t:{timestamp}:R>, <t:{timestamp}:f>", inline=False)

        await ctx.send(embed=q)
        
def setup(bot: commands.Bot):
    bot.add_cog(profileCog(bot))