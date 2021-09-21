import discord
from discord.ext import commands
from discord.flags import Intents

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', intents = intents)

@bot.event
async def on_ready():
    print(">> bot online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(882177143411449900)
    await channel.send(f'{member} 加入了本伺服器！')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(882778508013756427)
    await channel.send(f'{member} 离开了本伺服器qwq')
