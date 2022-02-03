from settings import *

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

@bot.command()
async def tictactoe(ctx, p1 : discord.Member, p2 : discord.Member):
    global player1
    global player2
    global turn
    global gameOver
    global count

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                ":white_large_square:", ":white_large_square:", ":white_large_square:",
                ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        text = ["It's <@", "C'est le tour de <@", "Es el turno de <@"]
        #print board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]
        
        #determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            if settings.Language == 0:
                await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
            else:
                await ctx.send(text[settings.Language] + str(player1.id) + ">")
        elif num == 2:
            turn = player2
            if settings.Language == 0:
                await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
            else:
                await ctx.send(text[settings.Language] + str(player2.id) + ">")
    else:
        text = ["A game is already in progress! Finish it before starting a new one.",
        "Une partie est en cours! Veuillez terminer la partie précédente!",
        "Ya hay un juego en curso! Termine antes de comenzar uno nuevo."]
        await ctx.send(text[settings.Language])

@bot.command()
async def place(ctx, pos : int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    win_text = ["wins!", "a gagné!", "ganas!"]
    tie_text = ["It's a tie!", "Égalité!", "Es un empate!"]
    arg_error = [
    "Be sure to choose an integer between 1 and 9 (inclusive) and un unmarked tile.",
    "Veillez à choisir un chiffre entre 1 et 9 (inclus) et une tuile non-marqué.",
    "Asegúrese de elegir un número entero entre 1 y 9 (inclusive) y un mosaico sin marcar."]
    turn_error = [
    "It's not your turn yet! Please wait.",
    "Ce n'est encore votre tour. Veuillez patienter.",
    "¡Aún no es tu turno! Espere por favor."]
    restart_text = [
    "Please start a new game using the ?tictactoe command.",
    "Veuillez utiliser la commande ?tictactoe afin de commence une nouvelle partie. ",
    "Inicie un nuevo juego con el comando ?tictactoe."]

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]
                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + win_text[settings.Language])
                elif count >= 9:
                    gameOver = True
                    await ctx.send(tie_text[settings.Language])
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send(arg_error[settings.Language])
        else:
            await ctx.send(turn_error[settings.Language])
    else:
        await ctx.send(restart_text[settings.Language])

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

# @tictactoe.error
# async def tictactoe_error(ctx, error):
#     print(error)
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("Please mention 2 players for this command.")
#     elif isinstance(error, commands.BadArgument):
#         await ctx.send("Please make sure to mention/ping players.")

# @place.error
# async def place_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("Please enter a position you would like to mark.")
#     elif isinstance(error, commands.BadArgument):
#         await ctx.send("Please make sure to enter an integer.")
