from settings import *
import settings

@bot.command()
async def help(ctx):
    if settings.Language == 1:
        await aide(ctx)
        return
    if settings.Language == 2:
        await ayudar(ctx)
        return
    msg = "\
    > Help Command\n\
    > **Games **\n\
    > `?tictactoe @player1 @player2:` To play tic tac toe.\n\
    > \tTo place a written symbol `?place position`. \n\
    > \tThe first player to line up 3 identical symbols wins the round\n\
    > `?pfs choice:` To play rock paper scissors.\n\
    > `?hm letter:` To play the hangman game\n\
    > \tThe game is about to find the title of a serie but if the hangman is complete you lose\n\
    > **Fun commands**\n\
    > `?rickroll:` To rick roll.\n\
    "
    await ctx.send(msg)

@bot.command()
async def aide(ctx):
    if settings.Language == 0:
        await help(ctx)
        return
    if settings.Language == 2:
        await ayudar(ctx)
        return
    msg = "\
    > Commande d'aide\n\
    > **Jeux**\n\
    > `?morpion @joueur1 @joueur2:` Pour jouer au morpion.\n\
    > \tPour posez un symbole écrivez `?place position`. \n\
    > \tLe premier joueur a aligner 3 symboles identiques l'emporte\n\
    > `?pfs choix:` Pour jouer à pierre feuille ciseaux .\n\
    > `?hm lettre:` Pour jouer au pendu.\n\
    > \tLe jeu consiste à trouver le titre d'une série, mais si le pendu est complet, vous perdez. \n\
    > **Commande fun**\n\
    > `?rickroll:` Pour rick roll.\n\
    "
    await ctx.send(msg)

@bot.command()
async def ayudar(ctx):
    if settings.Language == 0:
        await help(ctx)
        return
    if settings.Language == 1:
        await aide(ctx)
        return
    msg = "\
    >  El comando ayudar\n\
    > **La partida**\n\
    > `?tresenlinea @jugador1 @jugador2:` Para jugar  a tresenlinea.\n\
    > \tPara colocar un símbolo escribe `?place posición`. \n\
    > \tEl primer jugador que alinee 3 símbolos idénticos gagna la partida\n\
    > `?pfs Eleccion:` Para jugar tijeras de hoja de piedra.\n\
    > \tEl juego consiste en encontrar el titulo de una serie pero si el ahorcado está completo usted pierde\n\
    > `?hm carta:` Para Jugar al juego del ahorcado.\n\
    > **Divertido comando**\n\
    > `?rickroll:` A rick roll.\n\
    "
    await ctx.send(msg)
