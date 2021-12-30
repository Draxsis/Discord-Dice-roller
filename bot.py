# description : d&d dice rolling bot for use on Discord servers
# category : Tools and bots
# copyright : Copyright (c) 2021 Draxsis
# version : 1.0.0
# author : Draxsis / Mostafa Koolabadi

import os
import discord 
import d20
from d20 import roll
from d20 import SimpleStringifier
from discord import embeds 
from discord.ext import commands

#------------------------------- START --------------------------------------

client = commands.Bot (command_prefix = "$" , description="This bot will help you to roll all types of dices! ", activity = discord.Game(name="Persian D&D | $help "))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------\n Bot is Online and ready for anything ^^ \n . \n . \n .')

def is_me(m):
    return m.author == client.user
    
#------------------------------ ROLLS DICE -----------------------------------

@client.command(name='roll', aliases=['r'])
async def Roll(ctx, *, dice: str = '1d20'):
    
    dice = (dice)
    res = d20.roll(dice, stringifier= SimpleStringifier())
    out = f"{str(res)}"

    author_id = ctx.message.author.id
    myid = f'<@{author_id}>'

    await ctx.message.delete()

    embed = discord.Embed(title= (':game_die: your die result is:\n'), description= (f'Total : ** {out} **'))
    await ctx.send(myid, embed=embed)

#------------------------------ RANDCHAR -----------------------------------
@client.command(name='randchar', aliases=['rch'])
async def randchar(ctx):

    rolls = [roll("4d6kh3") for _ in range(6)]
    stats = '\n'.join(str(r) for r in rolls)
    total = sum([r.total for r in rolls])

    author_id = ctx.message.author.id
    myid = f'<@{author_id}>'

    await ctx.message.delete()

    embed = discord.Embed(title= (':game_die: Generated random stats:\n'), description= (f'\n{stats}\n\n **Total = {total}**'))
    await ctx.send(myid, embed=embed)

TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)