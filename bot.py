import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(">> bot online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave qwq')
    
bot.run('ODg5ODA4NTEwMDYwMjI4NjI4.YUmowA.lQimB7KVNKLjZ4fVM7PIMCKasRc')