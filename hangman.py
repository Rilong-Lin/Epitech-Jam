from settings import *

@bot.command()
async def pendu(ctx):
    msg = f'Salut {ctx.author.mention}! Vous pouvez jouer au pendu ici: https://motsbleus.pages-informatique.com/jeu-pendu.html\nBonne partie!'
    await ctx.send(msg)

@bot.command()
async def hangman(ctx):
    msg = f'Hello {ctx.author.mention}! You can play hangman here: https://motsbleus.pages-informatique.com/jeu-pendu.html\nGood game!'
    await ctx.send(msg)

@bot.command()
async def ahorcado(ctx):
    msg = f'Hola {ctx.author.mention}! Puedes jugar al ahorcado aquí: https://motsbleus.pages-informatique.com/jeu-pendu.html\nBuen juego!'
    await ctx.send(msg)
