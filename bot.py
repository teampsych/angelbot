import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import os
import random

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

@bot.command(pass_context=True)
async def ask(ctx, question):
    if question == "Are you okay?" or question == "How are you?" or question == "Are you alright?":
        possible_responses = ["I'm doing fine, I guess...", "Well, I'd be fine if Mio _wasn't_ having her mood swing right now!", "Why are you asking me this?", "Horrible, actually. What even is reality?", "Well, I'm doing better than yesterday.", "Stop looking for rainclouds. I don't tolerate them on my server!"]
        await bot.say(random.choice(possible_responses))
    else:
        possible_responses = ["What the hell are you saying?", "Uh, I know I know programming and all, but I don't understand your question...", "Are you even speaking English?", "Sorry, I don't understand."]
        await bot.say(random.choice(possible_responses))

bot.run(os.environ.get('BOT_KEY'))
