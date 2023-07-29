import discord
from discord.ext import commands
from functions import *
import os
from supabase import create_client, Client
import supabase

import eco

class sudoCog(commands.Cog, name="sudo command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="sudo", usage="", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def sudo(self, ctx):
        data = eco.get_bank_data()
        await ctx.send(data)

def setup(bot: commands.Bot):
    bot.add_cog(sudoCog(bot))
