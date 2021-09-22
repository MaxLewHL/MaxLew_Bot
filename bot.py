import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json', 'r', encoding='utf8') as jFile:
    jData = json.load(jFile)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(">> bot online <<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'加载 {extension} 完毕。')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'取消加载 {extension} 完毕。')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'重新加载 {extension} 完毕。')



for finename in os.listdir('./cmds'):
    if finename.endswith('.py'):
        bot.load_extension(f'cmds.{finename[:-3]}')

if __name__ == "__main__":
    bot.run(jData['TOKEN'])
