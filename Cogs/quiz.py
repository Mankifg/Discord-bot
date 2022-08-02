import discord
from discord.ext import commands

class quizCog(commands.Cog, name="ping command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="quiz", usage="", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def quiz(self, ctx):
        pass
        
def setup(bot: commands.Bot):
    bot.add_cog(quizCog(bot))