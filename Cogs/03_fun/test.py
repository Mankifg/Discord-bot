import discord
from discord.ext import commands
import os
import functions



class testCog(commands.Cog, name="test command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="test", usage="l")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def test(self, ctx):
        
        emojis = {e.name:str(e) for e in ctx.bot.emojis}
        msg = "Pong :CustomEmoji: {0.author.mention}".format(ctx.message).replace(':CustomEmoji:',emojis['leave'])
        await ctx.send(msg)


def setup(bot: commands.Bot):
    bot.add_cog(testCog(bot))
