import os 
import discord
from discord.ext import commands
from Website.flask import keep_alive as start

bot = commands.Bot(
  command_prefix="!"
  )
  
if __name__ == "__bot__":
  token = os.environ["token"]
  start()
  bot.run()