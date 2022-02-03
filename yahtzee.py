from settings import *

@bot.command()
async def yahtzeefr(ctx):
    msg = f'Salut {ctx.author.mention}! Vous pouvez jouer au yahtzee ici: https://www.jeux-gratuits.com/jeu-yahtzee-multijoueur.html/\nBonne partie!'
    await ctx.send(msg)

@bot.command()
async def yahtzeeeng(ctx):
    msg = f'Hello {ctx.author.mention}! You can play yahtzee here: https://www.jeux-gratuits.com/jeu-yahtzee-multijoueur.html/\nGood game!'
    await ctx.send(msg)

@bot.command()
async def yahtzeesp(ctx):
    msg = f'Hola {ctx.author.mention}! Puedes jugar al yahtzee aquí: https://www.jeux-gratuits.com/jeu-yahtzee-multijoueur.html/\nBuen juego!'
    await ctx.send(msg)
