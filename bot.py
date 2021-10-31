import random
import discord
import asyncio
from discord.ext import commands

client = commands.Bot (command_prefix = "$" , activity = discord.Game(name=" your activity here ! ")) 


@client.command()
async def roll_1d4(ctx):
    
    n = (f"**{random.randint(1, 4)}**")
    
    embed = discord.Embed(title= (':game_die: your result for 1d4 is : ')+(n)) 
    await ctx.send(embed=embed)

@client.command()
async def roll_1d6(ctx):
    
    n = (f"**{random.randint(1, 6)}**")
    
    embed = discord.Embed(title= (':game_die: your result for 1d6 is : ')+(n)) 
    await ctx.send(embed=embed)

@client.command()
async def roll_1d8(ctx):
    
    n = (f"**{random.randint(1, 8)}**")
    
    embed = discord.Embed(title= (':game_die: your result for 1d8 is : ')+(n)) 
    await ctx.send(embed=embed)

@client.command()
async def roll_1d10(ctx):
    
    n = (f"**{random.randint(1, 10)}**")
    
    embed = discord.Embed(title= (':game_die: your result for 1d10 is : ')+(n)) 
    await ctx.send(embed=embed)

@client.command()
async def roll_1d12(ctx):
    
    n = (f"**{random.randint(1, 12)}**")
    
    embed = discord.Embed(title= (':game_die: your fresult for 1d12 is : ')+(n)) 
    await ctx.send(embed=embed)

@client.command()
async def roll_1d20(ctx):
    
    n = (f"**{random.randint(1, 20)}**")
    
    embed = discord.Embed(title= (':game_die: your result for 1d20 is : ')+(n)) 
    await ctx.send(embed=embed)

@client.command()
async def roll_1d100(ctx):
    
    n = (f"**{random.randint(1, 100)}**")
    
    embed = discord.Embed(title= (':game_die: your result for 1d100 is : ')+(n)) 
    await ctx.send(embed=embed)

client.run('your Token here !')
