import discord
import asyncio
from discord.ext import commands, tasks


TOKEN = 'MTAwNjIzNjc2ODE3MDkzNDQwOA.G5kkV4.eWawMsquaEbqcPw9Ph1PrgUg0LFVTgY1IPXeGI'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents) 
@bot.command()
async def ping(ctx):
    print(ctx.bot)
    await ctx.send('pong')

@bot.event
async def on_ready():
    change_status.start()

@tasks.loop(hours=2)
async def change_status():
    channel = bot.get_channel(1139294659814899754)
    await channel.send("kirill down")


bot.run(TOKEN)