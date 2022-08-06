import discord
from discord.ext import commands
import random
import os

fot = []
path = os.getcwd()
path.replace("\\", "/")
with open(f"{path}/data/fot.txt", "r") as f:
    fot.append(f.read())

fot.append("Powered by Random | Made by Mankifg#1810")


class RandCog(commands.Cog, name="ping command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="rand", usage="", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def rand(self, ctx, low: int = None, high: int = None):
        if high == None:
            if low == None:
                num = random.randint(0, 1000000) / 1000000
                low = 0
                high = 1
            else:
                high = low
                low = 0
                num = random.randint(low, high)
        else:
            if low > high:
                low, high = high, low
            num = random.randint(low, high)

        q = discord.Embed(
            title="Random",
            description=f"{num}, range: {low} - {high}",
            color=discord.Color.random(),
        )
        fot[1] = fot[1].replace("{}", ctx.author.name)
        q.set_footer(text=random.choice(fot))
        await ctx.send(embed=q)


def setup(bot: commands.Bot):
    bot.add_cog(RandCog(bot))
