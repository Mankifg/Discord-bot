import discord
from discord.ext import commands
import random

replaces = [
    (".","⬛"),
    ("0","⬜"),
    ("1","🟩"),
    ("2","🟨"),
    ("3","🟧"),
    ("4","🟥")    
]

def change(ret):
    for i in range(len(replaces)):
        ret = ret.replace(replaces[i][0],replaces[i][1])

    return ret

def nice_board(board):
    ret = ""
    ret = f"{ret}{'-'*4*len(board)}\n"
    for x in range(len(board)):
        for y in range(len(board[x])):
            ret = ret + f"| {board[x][y]} "
        ret = ret + "|"

        ret = ret + "\n"
        ret = f"{ret}{'-'*4*len(board)}\n"
    
    ret = change(ret)
    return ret
        
def generate_board(w,h,):
    board = []
    for _ in range(h):
        board.append(["."]*w)
    
    return board

def swap(board,x,y,replace):
    board[x][y] = replace
    return board

def put_mines(board, n):
    for _ in range(n):
        x = random.randint(0,len(board[0])-1)
        y = random.randint(0,len(board)-1)
        
        while True:
            x = random.randint(0,len(board[0])-1) 
            y = random.randint(0,len(board)-1) 

            if not board[y][x] == "*":
                break
        
        board = swap(board,x,y,"*")
        
    return board

def single_one(board,x,y):
    if board[x][y] == "*":
        return "*"

    pari = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

    l = []

    for i in range(len(pari)):
        new_x = x + pari[i][0]
        new_y = y + pari[i][1]
        if new_x < 0 or new_y < 0: 
            continue
        try:
            l.append(board[new_x][new_y])
        except IndexError:
            pass
    
    return str(l.count("*"))

def putnumbers(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == "\n":
                continue
            replace = single_one(board,x,y)
            
            board = swap(board,x,y,replace)

    return board

def check_user_input(player_board,master_board,px,py):
    if master_board[px][py] == "*":
        return [],False
    
    if int(master_board[px][py]) == 0:
        q = []
        player_board,q = zero_spread(player_board,px,py,master_board,q)
        return player_board,True

    else:
        player_board = swap(player_board,px,py,master_board[px][py])
        return player_board, True


def check_around(x,y,board,master_board):
    if int(master_board[x][y]) == 0:
        board = zero_spread(board,x,y,master_board)
        return board
    
    else:
        board = swap(board,x,y,master_board[x][y])
        return board


def zero_spread(board,x,y,master_board,q):
    q.append((x,y))
    board = swap(board,x,y,master_board[x][y])

    pari = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

    
    if int(master_board[x][y]) == 0:

        for i in range(len(pari)):
            new_x = x + pari[i][0]
            new_y = y + pari[i][1]
            if new_x < 0 or new_y < 0: 
                continue
            try:
                board = swap(board,new_x,new_y,master_board[new_x][new_y])
                if (new_x,new_y) not in q:

                    board,q = zero_spread(board,new_x,new_y,master_board,q)

            except IndexError:
                pass

    else:
        board = swap(board,x,y,master_board[x][y])
    
    return board,q


class mineswpCog(commands.Cog, name="mineswp command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="mineswp", usage="", description="desc",aliases=["mnswp","minesweeper"])
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def mineswp(self, ctx):
    
        h,w,mines = 9,9,10

        #! 
        mines = 5


        b = generate_board(h,w)
        b = put_mines(b,mines)
        m_board = putnumbers(b)

        hidden_board = generate_board(h,w)

        while True:
            await ctx.send(f"```{nice_board(hidden_board)}```")
            await ctx.send("Enter x and y separed with space >")
            msg = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
            msg = msg.content.lower()

            if msg in ["stop","end","kill","exit"]:
                await ctx.send("Stoped")
                break

            try:
                player_x,player_y = msg.split(" ")
            except ValueError:
                await ctx.send("Bad input")
                break

            player_x, player_y = int(player_x), int(player_y)

            hidden_board, good = check_user_input(hidden_board,m_board,player_x,player_y)

            if not good:
                await ctx.send("You died")
                break
                

        await ctx.send(m_board)



def setup(bot: commands.Bot):
    bot.add_cog(mineswpCog(bot))
