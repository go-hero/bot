import os 
import discord
from discord.ext import commands
from Website.flask import keep_alive as start

import cogs

bot = commands.Bot(
  command_prefix="!"
  )
  
token = os.environ["token"]
start()
bot.run(token)