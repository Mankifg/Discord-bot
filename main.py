from pathlib import Path
from itertools import cycle
from discord.ext import commands, tasks
import json
import os
from itertools import cycle
from dotenv import load_dotenv
import discord
import startup
import time
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext


load_dotenv()
token = os.getenv('TOKEN')

unwanted_files = ["exam.txt", "wordle.py"]

with open("configuration.json", "r") as config:
    data = json.load(config)
    prefix = data["prefix"]
    owner_id = data["owner_id"]

status = cycle(
    ["Made by Mankifg#1810", "Made by luka heric#9699", "Watching You", "m!help"])


@tasks.loop(seconds=10)
async def status_swap():
    await bot.change_presence(activity=discord.Game(next(status)))


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(
   command_prefix=commands.when_mentioned_or("m!"),
    help_command=None,
    description="Mankifg's discord bot.",
    intents=intents,
    owner_id=owner_id,
)

slash = SlashCommand(bot, sync_commands=True)

if __name__ == '__main__':
    for path in Path('./Cogs').rglob('*.py'):
        
        p = str(path)
        p = p.replace("\\",".")
        p = p.replace("/",".")
        print(p)
        bot.load_extension(f"{p[:-3]}")


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    status_swap.start()

bot.run(token)
