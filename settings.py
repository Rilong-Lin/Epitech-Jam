import discord
from discord.ext import commands
import random

TOKEN = 'ODI1NDEwMzE0Nzk5NTQ2Mzg4.YF9hQg.IaRWTvBtlPf3EwL3aI9xjHRD8Es'

description = '''Bot Python'''

bot = commands.Bot(command_prefix='?', description=description)
bot.remove_command("help")

Language = 0

from help import *
