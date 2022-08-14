import discord
from discord.ext import commands

igralci = ['O', 'X']

numbers = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]

zero = numbers[0]
one = numbers[1]
two = numbers[2]
three = numbers[3]
four = numbers[4]
five = numbers[5]
six = numbers[6]
seven = numbers[7]
eight = numbers[8]
nine = numbers[9]

def preostalePoteze(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ' '):
                return True
    
    return False

def oceniPolozaj(board) :    
    for vrstica in range(3) :    
        if (board[vrstica][0] == board[vrstica][1] and board[vrstica][1] == board[vrstica][2]) :       
            if (board[vrstica][0] == igralci[0]) :
                return 10
            elif (board[vrstica][0] == igralci[1]) :
                return -10

    for stolpec in range(3) :
        if (board[0][stolpec] == board[1][stolpec] and board[1][stolpec] == board[2][stolpec]) :
            if (board[0][stolpec] == igralci[0]) :
                return 10
            elif (board[0][stolpec] == igralci[1]) :
                return -10

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) :
        if (board[0][0] == igralci[0]) :
            return 10
        elif (board[0][0] == igralci[1]) :
            return -10
 
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) :
        if (board[0][2] == igralci[0]) :
            return 10
        elif (board[0][2] == igralci[1]) :
            return -10

    return 0


def minimax(board, globina, jeMax):
    rezultat = oceniPolozaj(board)
    
    if (rezultat == 10 or rezultat == -10):
        return rezultat
    
    if (not preostalePoteze(board)):
        return 0
    
    if jeMax:
        naj = -1000
        for i in range(3):
            for j in range(3):
                if (board[i][j] == ' '):
                    board[i][j] = igralci[0]
                    naj = max(naj, minimax(board, globina + 1, not jeMax))
                    board[i][j] = ' '
        
    else:
        naj = 1000
        for i in range(3):
            for j in range(3):
                if (board[i][j] == ' '):
                    board[i][j] = igralci[1]
                    naj = min(naj, minimax(board, globina + 1, not jeMax))
                    board[i][j] = ' '
        
    return naj

def racunalnikPoteza(board):
    najPostavitev = [-1, -1]
    naj = -1000
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ' '):
                board[i][j] = 'O'
                tr = minimax(board, 0, False)
                if (tr > naj):
                    naj = tr
                    najPostavitev[0] = i
                    najPostavitev[1] = j

                board[i][j] = ' '
    
    board[najPostavitev[0]][najPostavitev[1]] = 'O'

def make_board(board):
    ret = ''
    for i in range(3):
        if (i != 0):
            ret = ret + '-' * 9 + '\n'
        
        for j in range(3):
            ret = ret + board[i][j]
            if (j != 2):
                ret = ret + ' | '
        
        ret = ret + '\n'

    return ret

def askforinput(user,channel,board):
    for i in range(8):
        if (board[i // 3][i % 3] == ' '):
            print(i)

class tictactoeCog(commands.Cog, name="ping command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="tictactoe", usage="", description="wip")
    @commands.cooldown(1, 2, commands.BucketType.member)

    async def tictactoe(self, ctx):
        
        gamming = True

        user = ctx.author
        channel = ctx.channel

        board = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
    
        while gamming:
            await ctx.send(make_board(board))

            ocena = oceniPolozaj(board)

            if (ocena == 10):
                await ctx.send('You loose LLL')
                return 0
            elif(ocena == -10):
                await ctx.send('You win')
                return 0
            
            if (not preostalePoteze(board)):
                await ctx.send('Draw')   
                return 0

            inp = askforinput(user,channel,board)
            j = int(inp % 3)
            i = int(inp / 3)

            board[i][j] = 'X'

            if (not preostalePoteze(board)):
                await ctx.send('Draw')
                return 0
            
            racunalnikPoteza(board)
        
        return 0



            

def setup(bot: commands.Bot):
    bot.add_cog(tictactoeCog(bot))
