import discord
from discord.ext import commands


class ButtonRoleCog(commands.Cog):
    """
    A cog with a slash command for posting the message with buttons
    and to initialize the view again when the bot is restarted.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.message_command(name="Show ID")  # Creates a global message command
    async def show_id(
        ctx: discord.ApplicationContext, message: discord.Message
    ):  # Message commands give a message param
        await ctx.respond(f"{ctx.author.name}, here's the message id: {message.id}!")


def setup(bot):
    bot.add_cog(ButtonRoleCog(bot))


