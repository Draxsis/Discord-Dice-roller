# copyright : Copyright (c) 2021 Mostafa koolabadi
# version : 1.0.1
# author : Draxsis / Mostafa Koolabadi

import random
import discord 
import asyncio 
from discord.ext import commands

client = commands.Bot (command_prefix = "$" , description="This bot will help you to roll all types of die! ", activity = discord.Game(name="YOUR SERVER ACTIVITY")) 

def is_me(m):
    return m.author == client.user

def is_num(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def roll_basic(a, b, modifier, hold):
    results = ""
    base = random.randint(int(a), int(b))
    if (base + modifier) >= hold:
        if modifier != 0:
            if modifier > 0:
                results += "({}) + ({}) = {}".format(base, modifier, (base + modifier), hold)
            else:
                results += "({}) ({}) = {} ".format(base, modifier, (base + modifier), hold)
        else:
            results += "{}".format(base)
    else:
        if modifier != 0:
            if modifier > 0:
                results += "({}) + ({}) = {}".format(base, modifier, (base + modifier))
            else:
                results += "({}) ({}) = {}".format(base, modifier, (base + modifier))
        else:
            results += "{}".format(base)
    return results

def roll_hit(num_of_dice, dice_type, hit, modifier, hold):
    results = ""
    total = 0
    for x in range(0, int(num_of_dice)):
        y = random.randint(1, int(dice_type))
        if (int(hit) > 0):
            if (y >= int(hit)):
                results += "**{}** ".format(y)
                total += 1
            else:
                results += "{} ".format(y)
        else:
            results += "{} ".format(y)
            total += y
    total += int(modifier)
    if modifier != 0:
        if modifier > 0:
            results += "+ ({}) = {}".format(modifier, total)
        else:
            results += "= ({})".format(modifier, total)
    else:
        results += "= ({})".format(total)
    if hold != 0:
        if total >= hold:
            results += "({})".format(hold)
        else:
            results += "({})".format(hold)
    return results

@client.command(pass_context=True)
@asyncio.coroutine
def roll(ctx, roll : str):
    a, b, modifier, hit, num_of_dice, hold, dice_type = 0, 0, 0, 0, 0, 0, 0
    
    author = ctx.message.author
    if (roll.find('+') != -1):
        roll, modifier = roll.split('+')
    if (roll.find('d') != -1):
        num_of_dice, dice_type = roll.split('d')
    elif (roll.find('-') != -1):
        a, b = roll.split('-')
    else:
        a = 1
        b = roll

    if (modifier != 0):
        if (is_num(modifier) is False):
            raise ValueError("Modifier value format error. Proper usage 1d4+1, please try again.")
            return
        else:
            modifier = int(modifier)
    if (num_of_dice != 0):
        if (is_num(num_of_dice) is False):
            raise ValueError("Number of dice format error. Proper usage 3d6, please try again.")
            return
        else:
            num_of_dice = int(num_of_dice)
    if (num_of_dice > 200):
        raise ValueError("Too many dice. Please limit to 200 or less, please try again.")
        return
    if (dice_type != 0):
        if (is_num(dice_type) is False):
            raise ValueError("Dice type format error. Proper usage 4d6, please try again.")
            return
        else:
            dice_type = int(dice_type)
    if (a != 0):
        if (is_num(a) is False):
            raise ValueError("Error: Minimum must be a number. Proper usage 1-50, please try again.")
            return
        else:
            a = int(a)
    if (b != 0):
        if (is_num(b) is False):
            raise ValueError("Error: Maximum must be a number. Proper usage 1-50 or 50, please try again.")
            return
        else:
            b = int(b)
    if (hold != 0):
        if (is_num(hold) is False):
            raise ValueError("Error: hold must be a number. Proper usage 1-100>30, please try again.")
            return
        else:
            hold = int(hold)
    if (dice_type != 0 and hit != 0):
        if (hit > dice_type):
            raise ValueError("Error: Hit value cannot be greater than dice type, please try again.")
            return
        elif (dice_type < 0):
            raise ValueError("Dice type cannot be a negative number, please try again.")
            return
        elif (num_of_dice < 0):
            raise ValueError("Number of dice cannot be a negative number, please try again.")
            return

    if a != 0 and b != 0:
        yield from ctx.send(embed = discord.Embed(title= (':game_die: your die result is  '), description= ("** Total: ** ({}-{}) = ** `{}` **".format(a, b, roll_basic(a, b, modifier, hold)))))
    else:
        yield from ctx.send(embed = discord.Embed(title= (':game_die: your die result is  '), description= ("** Total: ** ({}d{}) ** `{}` **".format(num_of_dice, dice_type, roll_hit(num_of_dice, dice_type, hit, modifier, hold)))))

client.run('TOKEN')
