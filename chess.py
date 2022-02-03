from settings import *

@bot.command()
async def echecs(ctx):
    msg = f'Salut {ctx.author.mention}! Vous pouvez jouer aux echecs ici: https://www.chess.com/fr\nBonne partie!'
    await ctx.send(msg)

@bot.command()
async def chess(ctx):
    msg = f'Hello {ctx.author.mention}! You can play chess here: https://www.chess.com/fr\nGood game!'
    await ctx.send(msg)

@bot.command()
async def ajedrez(ctx):
    msg = f'Hola {ctx.author.mention}! Puedes jugar al ajedrez aquí: https://www.chess.com/fr\nBuen juego!'
    await ctx.send(msg)
