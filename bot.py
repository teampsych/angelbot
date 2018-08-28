import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="p.")

@bot.event
async def on_ready():
    print("Running")
    await bot.change_presence(game=discord.Game(name='Pizza... | v0.0'))
    for channel in member.server.channels:
        if channel.name == 'general' or channel.name == 'breakroom' or channel.name == 'announcements'
            await bot.send_message(channel, "Hi, guys! There is no commands for me yet, I'm more like a useless piece of furniture for now, ehehe~!")
    
@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

bot.run('NDgzODM1NTgyMzE4MTE2ODY2.DmbUtQ.uHK9jLrtrGLT12q9ONdcSIhijGg')
