from settings import *

@bot.command()
async def puissance4(ctx):
    msg = f'Salut {ctx.author.mention}! Vous pouvez jouer au puissance 4 ici: https://lululataupe.com/jeux-tablettes/tout-age/puissance-4/\nBonne partie!'
    await ctx.send(msg)

@bot.command()
async def connect4(ctx):
    msg = f'Hello {ctx.author.mention}! You can play connect 4 here: https://lululataupe.com/jeux-tablettes/tout-age/puissance-4/\nGood game!'
    await ctx.send(msg)

@bot.command()
async def conecta4(ctx):
    msg = f'Hola {ctx.author.mention}! Puedes jugar al conecta 4 aquí: https://lululataupe.com/jeux-tablettes/tout-age/puissance-4/\nBuen juego!'
    await ctx.send(msg)
