import discord
from discord.ext import commands
from functions import *

import eco

class shopCog(commands.Cog, name="shop commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="buy", usage="", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def buy(self, ctx, name, value):
        
        try:
            value = int(value)
        except:
            print("int err")
            return
        userObj = ctx.author
        id = userObj.id

        eco.create_account(id)
        user_data = eco.get_user_data(id)

        

        if user_data['money']<value:
            q = discord.Embed(title=f"You don't have enough money to buy {name} for {value}.",
                              description=f"you need {value-user_data['money']} more",
                              color=discord.Color.red())
            await ctx.send(embed=q)
            return
                
        item_json = {"name": name, "value": value}
            
        user_data['backpack']['items'].append(item_json)

        user_data['money'] -= value

        eco.save_user_data(user_data)
        
        q = discord.Embed(title=f"You successfully purchased {name} for {value}",
                              description=f"Now you have only {user_data['money']}",
                              color=discord.Color.green())
        
        await ctx.send(embed=q)
            
    @commands.command(name="sell", usage="", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)       
    async def sell(self, ctx, name, value):
        #? (r)  ®p1fl4r
        try:
            value = int(value)
        except:
            print("int err")
            return
        userObj = ctx.author
        id = userObj.id

        eco.create_account(id)
        user_data = eco.get_user_data(id)


        if name not in list([item['name'] for item in user_data['backpack']['items']]):
            q = discord.Embed(title=f"You don't have {name} to sell it!",
                                color=discord.Color.red())
            await ctx.send(embed=q)
            return
         
            
        """for i in range(len(user_data['backpack']['items'])):
            if user_data['backpack']['items'][i]['name'] == name:
                index = i
                
        if """
        before = len(user_data['backpack']['items'])    
    
        user_data['backpack']['items'] = [item for item in user_data['backpack']['items'] if item['name'] != name]

        after = len(user_data['backpack']['items'])
        
        user_data['money'] += value*(before-after)

        eco.save_user_data(user_data)
        
        q = discord.Embed(title=f"You successfully sold {name} for {value}",
                                description=f"Now you have {user_data['money']}",
                                color=discord.Color.green())
        
        await ctx.send(embed=q)
        
def setup(bot: commands.Bot):
    bot.add_cog(shopCog(bot))
