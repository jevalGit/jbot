#imports
import discord
from discord.ext import commands
import os 
from dotenv import load_dotenv

load_dotenv() 
bot = discord.Bot()
#test-bot
@bot.event
async def on_ready():
    print(f"{bot.user} está operativo")

@bot.slash_command(name = "saludo", description = "Hola")
async def hello(ctx):
    await ctx.send(f"Hola {ctx.author} ")
#comandos-de-ejemplo

#

bot.run(os.getenv('TOKEN')) 