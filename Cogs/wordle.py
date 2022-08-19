import discord
from discord.ext import commands
import random

fot = []
with open("./data/fot.txt","r") as f:
    fot = f.read().splitlines()

green = "🟩"
yellow = "🟨" 
gray = ""
LEN = 5

class wordleCog(commands.Cog, name="ping command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="wordle", usage="", description="")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def wordle(self, ctx):
        fot[0] = fot[0].replace("{}", ctx.author.name)
        fot[1] = fot[1].replace('{}', ctx.author.name)

        p = ctx.author.name
        word = "abcde"
        output = ["_ _ _ _ _ ",""
                "_ _ _ _ _ ", ""
                "_ _ _ _ _ ", ""
                "_ _ _ _ _ ", ""
                "_ _ _ _ _ ",""
                "_ _ _ _ _ ",""]

        round = 1
        player = ''
        saved = '' 
        a = 0 
        while True:
            

            if round == 6:
                await ctx.send(f"You lose, the word was {word}.")
                break


            display = ''
            for x in range(len(output)):
                display = display + " " + output[x] + "\n"

            display = f"```{display}```"

            embed = discord.Embed(title=f"Wordle - Round {round}")
            embed.add_field(name= "Wordle", value=f"{display}",inline=False)
            embed.add_field(name='Enter world',value=p,inline=False)
            embed.set_footer(text=random.choice(fot))
            await ctx.send(embed=embed)
            
            msg = await self.bot.wait_for('message', 
            check=lambda m: m.author == ctx.author)

            player = msg.content.lower()
            
            if player == word:
                await ctx.send(f"You win, the word was {word}.")
                break
            
            if not len(player) == 5:
                await ctx.send(f"{player} is not a valid word.")
                continue
            colors = ["","","","",""]
            out = ''
            ponavljanje = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
            if len(player) == 5:
                for i in range(len(player)):
                    if player[i] == word[i]:
                        colors[i] = 'g'
                        out[i] = green(player[i]) + " "
                        ponavljanje[player[i]] += 1

                for i in range(len(player)):
                    if player[i] in word and ponavljanje[player[i]] < word.count(player[i]):
                        colors[i] = 'y'
                        out[i] = yellow(player[i]) + " "
                    elif player[i] != word[i]:
                        colors[i] = 'r'
                        out[i] = player[i] + " "

            
                save = ''


                for i in range(len(colors)):
                    if colors[i] == "g":
                        save = save + green + " "
                    elif colors[i] == "y":
                        save = save + yellow + " "
                    else:
                        save = save + gray + " "

                await ctx.send(save)
                a = a + 2
            else:
                pass

                        
def setup(bot: commands.Bot):
    bot.add_cog(wordleCog(bot))