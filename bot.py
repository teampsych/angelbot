import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import os

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print("Running")
    await bot.change_presence(game=discord.Game(name='Doki Doki: The Angel Returns'))
    for channel in member.server.channels:
        if channel.name == 'general' or channel.name == 'breakroom':
            await bot.send_message(channel, "Hi, guys! I'm just getting everything warmed up here, ehehe~!")
    

@bot.event
async def on_member_join(member: discord.Member):
    for channel in member.server.channels:
        if channel.name == 'general' or channel.name == 'breakroom':
            await bot.send_message(channel, "Welcome to my studio, \@{}!".format(member.name))

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("STAHP IT!")

bot.run(os.environ.get('BOT_KEY'))
