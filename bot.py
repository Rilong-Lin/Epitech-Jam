# from settings import *
from tictactio import *
import asyncio
from controller import HangmanGame
from music import *
from chess import *
from connect4 import *
from hangman import *
from yahtzee import *

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if message.content.startswith('?1'):
        text = ["Wanna play rock paper scissors ? (?pfs)",
        "Envie de jouer a pierre feuille sciseaux ? (?pfs)",
        "¿Quieres jugar piedra, papel, tijeras ? (?pfs)"]
        await message.channel.send(text[settings.Language])
    if message.content.startswith('?2'):
        text = [["Wanna play tic tac toe ? (?pfs)",
        "Envie de jouer aux morpions ? (?pfs)",
        "¿Quieres jugar tresenlinea ? (?pfs)"],
        ["Or maybe play yazty ? (?yahtzeeen)",
        "Ou faire un yahtzy ? (?yahtzeefr)",
        "Para jugado yahtzy ? (?yahtzeesp)"]]

        await message.channel.send(text[0][settings.Language])
        await asyncio.sleep(3)
        await message.channel.send(text[1][settings.Language])
    if message.content.startswith('?3'):
        text = ["Wanna play mattel ?", "Envies de jouer aux scrabble ?", "Para jugado scrabble ?"]
        await message.channel.send(text[settings.Language])
    if message.content.startswith('?4'):
        text = ["Wanna do a quizz ?", "Envies de ce faire un quizz ?", "Quiero hacer un quizz ?"]
        await message.channel.send(text[settings.Language])
    if message.content.startswith('?5'):
        text = ["Wanna do a hangman game ?", "Envies de ce faire un pendu ?", "Para juego del ahorcado ?"]
        await message.channel.send(text[settings.Language])
    await bot.process_commands(message)

@bot.command()
async def pfs(ctx, user_choice):
    rpsGame = ['rock', 'pierre', 'piedra', 'paper', 'papier', 'papel', 'scissors','ciseaux', 'tijeras']
    choice = [['rock', 'pierre', 'piedra'], ['paper', 'papier', 'papel'], ['scissors','ciseaux', 'tijeras']]
    # 0 == win bot, 1 == player win, 2 == draw
    win = 0

    if user_choice.lower() in rpsGame:
        bot_choice = random.choice(choice)[settings.Language]
        user_choice = user_choice.lower()
#        bot_emote = ":rock:"
#        if bot_choice in choice[1]:
#            bot_emote = ":newspaper2:"
#        elif bot_choice in choice[2]:
#            bot_emote = ":scissors:"
        # draw
        if user_choice in choice[0] and bot_choice in choice[0]:
            win = 2
        elif user_choice in choice[1] and bot_choice in choice[1]:
            win = 2
        elif user_choice in choice[2] and bot_choice in choice[2]:
            win = 2
        # pierre Win Conditions #
        if user_choice in choice[0] and bot_choice in choice[2]:
            win = 1
        # feuille Win Conditions #
        elif user_choice in choice[1] and bot_choice in choice[0]:
            win = 1
        # Scissor Win Conditions #
        elif user_choice in choice[2] and bot_choice in choice[1]:
            win = 1

        if settings.Language == 0:
            await ctx.send(f'Your choice: `{user_choice}`\nEinstein\'s choice: `{bot_choice}`')
        elif settings.Language == 1:
            await ctx.send(f'Votre Choix: `{user_choice}`\nChoix de Einstein: `{bot_choice}`')
        elif settings.Language == 2:
            await ctx.send(f'Tu elección: `{user_choice}`\nLa elección de Einstein: `{bot_choice}`')

        if win == 0:
            if settings.Language == 0:
                await ctx.send("I win!")
            elif settings.Language == 1:
                await ctx.send("J'ai gagné!")
            elif settings.Language == 2:
                await ctx.send("Yo gano!")
        elif win == 2:
            if settings.Language == 0:
                await ctx.send("It's a draw!")
            elif settings.Language == 1:
                await ctx.send("Égalité!")
            elif settings.Language == 2:
                await ctx.send("Es un empate!")
        else:
            if settings.Language == 0:
                await ctx.send("You win!")
            elif settings.Language == 1:
                await ctx.send("Vous avez gagné!")
            elif settings.Language == 2:
                await ctx.send("Tú ganas!")

@bot.command()
async def games(ctx):
    msg = f'Salut {ctx.author.mention}! Puis-je savoir combien vous êtes?'
    await ctx.send(msg)

@bot.command()
async def hello(ctx):
    """Says Hello World"""
    Hello = ["Hello!", "Salut!", "Hola!"]
    await ctx.send(Hello[Language])

@bot.command()
async def setlang(ctx, tag):
#    global Language
    Text = ["The language have been changed!", "la langue a été changée!", "El lenguaje ha cambiado!"]

    if tag is None:
        await ctx.send("Choose your language !: \n:flag_us: (EN) :flag_fr: (FR), :flag_es: (ES)")
    else:
        if tag == "EN" or tag == "en":
            settings.Language = 0
            await ctx.send(Text[settings.Language])
        elif tag == "FR" or tag == "fr":
            settings.Language = 1
            await ctx.send(Text[settings.Language])
        elif tag == "ES" or tag == "es":
            settings.Language = 2
            await ctx.send(Text[settings.Language])
        else:
            if settings.Language == 0:
                await ctx.send("Error!\nUnknow language tag!")
            elif settings.Language == 1:
                await ctx.send("Erreur!\nTag non reconue")
            elif settings.Language == 2:
                await ctx.send("¡Error!\n¡Etiqueta de idioma sin saberlo!")

def check_serie(img):
    series = ['https://tenor.com/view/prison-break-gif-19902337', 'https://tenor.com/view/stranger-things-stranger-things-netflix-original-gif-6173270',
                'https://tenor.com/view/wandavision-marvel-marvel-studios-marvel-entertainment-disney-gif-19961468', 'https://tenor.com/view/national-sunglasses-day-international-womens-day-bad-ass-mae-whitman-retta-gif-11299463',
                'https://tenor.com/view/laughing-raymond-reddington-james-spader-the-blacklist-happy-gif-16816911', 'https://tenor.com/view/milf-gif-4484779',
                'https://tenor.com/view/naruto-wink-smile-happy-sarcastic-gif-7551863', 'https://tenor.com/view/scandal-gladiators-kerry-washington-gif-9201351', 'https://tenor.com/view/cheers-narcos-pablo-escobar-gif-13646037',
                'https://tenor.com/view/friends-flex-squad-gif-4389959', 'https://tenor.com/view/simpsons-dance-ghostbusters-bart-marge-gif-3999446']

    if img == 'prisonbreak':
        return series[0]
    if img == 'simpson':
        return series[10]
    if img == 'narcos':
        return series[8]
    if img == 'scandal':
        return series[7]
    if img == 'desperatehousewives':
        return series[5]
    if img == 'naruto':
        return series[6]
    if img == 'blacklist':
        return series[4]
    if img == 'goodgirls':
        return series[3]
    if img == 'friends':
        return series[9]
    if img == 'strangerthings':
        return series[1]
    if img == 'wandavision':
        return series[2]

@bot.command()
async def hm(ctx, guess: str):
    player_id = ctx.author.id
    hangman_instance = HangmanGame()
    game_over, won = hangman_instance.run(player_id, guess)

    if game_over:
        game_over_message = "You did not win"
        if won:
            game_over_message = "Congrats you won!!"

        game_over_message = game_over_message + \
            " The word was %s\n" % hangman_instance.get_secret_word() + check_serie(hangman_instance.get_secret_word())

        await ctx.send(game_over_message)
        await hangman_instance.reset(player_id)

    else:
        await ctx.send("Progress: %s" % hangman_instance.get_progress_string())
        await ctx.send("Guess so far: %s" % hangman_instance.get_guess_string())

@bot.command()

async def rickroll(ctx):
    await ctx.send("https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983")

bot.run(TOKEN)
