import discord
from discord.ext import commands
from functions import *
import os
from supabase import create_client, Client
import supabase

url: str = os.environ.get("SUPA_URL")
key: str = os.environ.get("SUPA_KEY")

supabase: Client = create_client(url, key)

TABLE = "main"
FIX_LEN = 30

def get_bank_data():
    response = supabase.table(TABLE).select("*").execute()
    response = dict(response)
    response = response.get("data")
    return response

def account_with_id_exists(id: int):
    query = supabase \
        .from_(TABLE) \
        .select('*', count='exact') \
        .eq('user id', id)

    result = dict(query.execute())

    return result.get('count') == 1


def create_account(id: int = -1):
    if account_with_id_exists(id):
        # exists
        return True
    else:
        data = {
            "user id": id,
            "money": 0,
            "bank": 0,
            "backpack": {},
        }
        response = supabase.from_(TABLE).insert(data).execute()


def get_account_data(id):
    create_account(id)

    query = supabase.from_(TABLE).select('*', count='exact').eq('user id', id)
    result = dict(query.execute())

    return result.get('data')[0]


class economyCog(commands.Cog, name="economy command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="bal", usage=" @username", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def bal(self, ctx, check: discord.Member = None):
        id = ctx.author.id
        create_account(id)

        user_data = get_account_data(id)
        print(user_data)
        
        '''if check == None:
            user = users[str(ctx.author.id)]
            q = discord.Embed(title=f"{ctx.author.name}'s Balance {int(user['wallet']) + int(user['bank'])}", color=discord.Color.random())
            
        else:
            create_account(check.id)
            user = users[str(check.id)]
            q = discord.Embed(title=f"{check.name}'s balance {int(user['wallet']) + int(user['bank'])}", color=discord.Color.random())

        q.add_field(name="Wallet", value=user['wallet'], inline=True)
        q.add_field(name="Bank", value=user['bank'], inline=True)'''

        # await ctx.send(embed=q)


def setup(bot: commands.Bot):
    bot.add_cog(economyCog(bot))
