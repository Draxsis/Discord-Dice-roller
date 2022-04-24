# category : Tools and bots
# copyright : Copyright (c) 2021 Draxsis
# version : 1.0.1
# author : Draxsis / Mostafa Koolabadi

import os
import platform
import discord
import d20
from d20 import *
from discord import embeds 
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL

load_dotenv()
client = commands.Bot (command_prefix = "$" ,
                        description="This bot will help you to roll all types of dices! ",
                        activity = discord.Game(name="Persian D&D | $help "))

players = {}

@client.event
async def on_ready(): #showing the bot status
    print(f"Logged in as {client.user.name}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")

#---

@client.command(name='roll', aliases=['r'])
async def Roll(ctx, *, dice: str = '1d20'): #main dice roller
    
    dice = (dice)
    res = d20.roll(dice, stringifier= SimpleStringifier())
    out = f"{str(res)}"

    author_id = ctx.message.author.id
    myid = f'<@{author_id}>'

    await ctx.message.delete()

    embed = discord.Embed(title= (':game_die: your die result is:\n'), description= (f'Total : ** {out} **'))
    await ctx.send(myid, embed=embed)

#---

@client.command(name='randchar', aliases=['rch'])
async def randchar(ctx): # randomize 6 stats for character (4d6kh3 x 6)

    rolls = [roll("4d6kh3") for _ in range(6)]
    stats = '\n'.join(str(r) for r in rolls)
    total = sum([r.total for r in rolls])

    author_id = ctx.message.author.id
    myid = f'<@{author_id}>'

    embed = discord.Embed(title= (':game_die: Generated random stats:\n'),
                         description= (f'\n{stats}\n\n **Total = {total}**'))

    await ctx.message.delete()             
    await ctx.send(myid, embed=embed)

#---

@client.command(name='Join')
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

#---

@client.command(name='play')
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Bot is playing')

    else:
        await ctx.send("Bot is already playing")
        return

#--

@client.command(name='resume')
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Bot is resuming')

#--

@client.command(name='pause')
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Bot has been paused')

#--

@client.command(name='stop')
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Stopping...')

client.run(os.getenv('DISCORD_TOKEN'))
