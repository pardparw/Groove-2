from http import client
from unicodedata import name
import discord
from discord.ext import commands
import os
from discord.utils import get

from dotenv import load_dotenv 
load_dotenv()                 
################################
        
bot = commands.Bot(command_prefix='+',help_command=None)#prefix


@bot.command()#TH
async def verifly(ctx):


    
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    embed = discord.Embed(title="ใส่เลขที่", color=0x28FF73)
    await ctx.send(embed=embed)
    msg1 = await bot.wait_for("message", check=check)
    embed = discord.Embed(title="ใส่เลขประจำตัว", color=0x28FF73)
    await ctx.send(embed=embed)
    msg2 = await bot.wait_for("message", check=check)
    id = int(msg2.content)
    num = int(msg1.content)
    

    user = [0, 28037, 28038, 28115, 28121, 28152, 28157, 28194, 28281, 28473, 28498, 28505, 28584, 28585, 30420, 30412, 27852, 28061, 28101, 28132, 28150, 28175, 28177, 28184, 28228, 28306, 28491, 28522, 28523, 28527, 28551, 28553, 28558, 28563, 30423, 30424, 30425]
    
    if id==user[num]:
              
        member = ctx.author
        role = get(ctx.guild.roles, name = "﻿MEMBER👨‍👩‍👦")
        await member.add_roles(role, atomic=True)
        embed = discord.Embed(title="สามารถใช้serverใด้แล้ว", color=0x1aff00)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="❌โปรดตรวจสอบว่าหมายเลขประจำตัวมเลขที่ถูก.", color=0xFF0000)
        await ctx.send(embed=embed)

bot.run(os.getenv('TOKEN'))  