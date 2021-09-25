import discord
from discord import channel
from discord.ext import commands
import json
import os
import datetime

with open('setting.json', 'r', encoding='utf8') as jFile:
    jData = json.load(jFile)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='M//', intents=intents)

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help Centre", description="use M//help <command> for command description", color=0x001eff, 
    timestamp=datetime.datetime.now())
    embed.set_author(name="Maxlew", url="https://discord.gg/TeDkjm9KFC")
    embed.add_field(name="Command prefix:", value="```M//```is the command prefix")
    embed.add_field(name="Bot_command", value="help, load, unload, reload")
    embed.add_field(name="Main_command", value="ping, hi, repeat, clean")
    embed.add_field(name="React_command", value="picture, web_picture")
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    channel = bot.get_channel(int(jData['hi_channel']))
    await channel.send('------------------------------\n\nBot已上线\n\n------------------------------')
    print('>> Bot is online <<')

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

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
from python.testbot.core.classes import Cog_Extension
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):
        
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title="Ping", description="result", color=0x001eff, 
        timestamp=datetime.datetime.now())
        embed.set_author(name="Maxlew", url="https://discord.gg/TeDkjm9KFC")
        embed.add_field(name="Bot Lantency:", value=f"{round(self.bot.latency*1000)} (ms)\nWeSocket: Error404(no do")
        await ctx.send(embed=embed)

    @commands.command()
    async def hi(self, ctx):
        await ctx.send(f'hi')
    
    @commands.command()
    async def repeat(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def clean(self, ctx, num: int):
        limit=num+1
        await ctx.channel.purge(limit=num+1)
        await ctx.send(f"成功删除 {limit} 条讯息！")

def setup(bot):
    bot.add_cog(Main(bot))
