# description : d&d dice rolling bot for use on Discord servers
# category : Tools and bots
# copyright : Copyright (c) 2021 Draxsis
# version : 1.0.0
# author : Draxsis / Mostafa Koolabadi

import os
import platform
import discord
import d20
from d20 import *
from discord import embeds 
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

client = commands.Bot (command_prefix = "$" , description="This bot will help you to roll all types of dices! ", activity = discord.Game(name="Persian D&D | $help "))

@client.event
async def on_ready(): #showing the bot status
    print(f"Logged in as {client.user.name}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")

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

@client.command(name='randchar', aliases=['rch'])
async def randchar(ctx): # randomize 6 stats for character (4d6kh3 x 6)

    rolls = [roll("4d6kh3") for _ in range(6)]
    stats = '\n'.join(str(r) for r in rolls)
    total = sum([r.total for r in rolls])

    author_id = ctx.message.author.id
    myid = f'<@{author_id}>'

    embed = discord.Embed(title= (':game_die: Generated random stats:\n'), description= (f'\n{stats}\n\n **Total = {total}**'))
    await ctx.message.delete()             
    await ctx.send(myid, embed=embed)

@client.command(name='class')
async def Klass(ctx, class_name): #returning results from wikidot website and show details for each class
    
    URL = f"http://dnd5e.wikidot.com/{class_name}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    
    info = soup.select("p")[0].getText()
    hp = soup.select("p")[3].getText()
    prof = soup.select("p")[4].getText()
    equip1 = soup.select("li")[26].getText()
    equip2 = soup.select("li")[27].getText()
    equip3 = soup.select("li")[28].getText()
    equip4 = soup.select("li")[29].getText()
 
    embed=discord.Embed(title=f"{class_name} - D&D 5e edition",
                    url=f"http://dnd5e.wikidot.com/{class_name}",
                    description= info)
    embed.add_field(name="Hit Points", value=hp, inline=False)
    embed.add_field(name="Proficiencies", value=prof, inline=False)
    embed.add_field(name="Equipments", value=(f'{equip1} \n {equip2} \n {equip3} \n {equip4}'), inline=False)
    embed.set_footer(text="powered by Draxsis from dnd5e.wikidot")

    await ctx.message.delete()
    await ctx.send(embed=embed)
    
    
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
