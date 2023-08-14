import discord
from discord.ext import commands
from functions import *
import os
from supabase import create_client, Client
import supabase
import discord
from discord.ext import commands
import discord
import discord
from discord.ui import Button,View
from discord.ext import commands
import time

import eco

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="name?"))
        self.add_item(discord.ui.InputText(label="value?"))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Created new item")
        
        if int(self.children[1].value) < 1:
            embed= discord.Embed(title="Error", description="Value must be greater than 0",color=discord.Color.red())
            await interaction.response.send_message(embeds=[embed])
            return

        
        max_id = 0
        data = eco.load_second_table_idd(1)
        for item in data["data"]:
            if item["id"] > max_id:
                max_id = item["id"]
        
        item_json = {
            "id": max_id+1,
            "name":self.children[0].value,
            "value": int(self.children[1].value),
            "sell":0.5,
        }
        

        data["data"].append(item_json)
        
        eco.save_second_table_idd(data)
        
        embed.add_field(name="Name", value=self.children[0].value)
        embed.add_field(name="Id", value=max_id)
        embed.add_field(name="Value", value=self.children[1].value)
        
        await interaction.response.send_message(embeds=[embed])

cool_guys = [833403343690530827,650756055390879757]

class sudoCog(commands.Cog, name="sudo command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="sudo", usage="", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def sudo(self, ctx):
        data = eco.get_bank_data()
        await ctx.send(data)


    @discord.command(name="create", usage="", description="")
    async def create(self, ctx):
        if not ctx.author.id in cool_guys:
            q = discord.Embed(title="Missing permissinon to create items.",color=discord.Color.red())
            await ctx.send(embed=q)
            return
        
        modal = MyModal(title="Making a new item")
        
        await ctx.send_modal(modal)
    


def setup(bot: commands.Bot):
    bot.add_cog(sudoCog(bot))
