import discord
from discord.utils import get
from discord.ext import commands
import datetime
import random
from song import songAPI
from discord import Game
from discord.ext.commands import Bot
from discord import *
import asyncio
import os



from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from dotenv import load_dotenv

load_dotenv()




    


    
bot = commands.Bot(command_prefix='+',help_command=None)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command() 
async def help(ctx):
     
    emBed = discord.Embed(title="3/15evo", color=0x1a91ff)
    emBed.add_field(name="+help", value="Get help command",inline=False)
    emBed.add_field(name="send[comming soon]", value="+text", inline=False)
    emBed.add_field(name="+listen", value="Music", inline=False)
    emBed.add_field(name="+random", value="random number", inline=False)
    emBed.add_field(name='clear', value='+clear [number] deleat message', inline=False)
    emBed.set_thumbnail(url='https://i.imgur.com/0GkF17z.jpg')
    emBed.add_field(name="staus", value="Check status", inline=False)
    emBed.add_field(name="language", value="`th-ไทย`,`jp-ญี่ปุ่น`", inline=False)


    emBed.set_footer(text='To get more info on a command, do +help command name', icon_url='https://i.imgur.com/0GkF17z.jpg')
    
    buttons = [
        create_button(style=ButtonStyle.URL, label="Invite BOT", url="https://discord.com/api/oauth2/authorize?client_id=865808924472377374&permissions=1644971949303&scope=bot%20applications.commands")
        
    ]
    action_row = create_actionrow(*buttons)
   
    await ctx.send(components=[action_row],embed=emBed)
    print("help")
###################help slash

@bot.command()
async def helpth(ctx):
     
    emBed = discord.Embed(title="3/15evo", color=0x1a91ff)
    emBed.add_field(name="+help", value="ดูคำสั้งทั้งหมดขอบบอท",inline=False)
    emBed.add_field(name="send[comming soon]", value="+text", inline=False)
    emBed.add_field(name="listen", value="เปิดเพลง", inline=False)
    emBed.add_field(name="random", value="สุ่มตัวเลข", inline=False)
    emBed.set_thumbnail(url='https://i.imgur.com/0GkF17z.jpg')
    emBed.set_footer(text='หากต้องการข้อมูลเพิ่มเติมเกี่ยวกับคำสั่ง ให้ +help ชื่อคำสั่ง', icon_url='https://i.imgur.com/0GkF17z.jpg')
    emBed.add_field(name="staus", value="ตรวจสอบสถานะเซิร์ฟเวอร์", inline=False)

    await ctx.channel.send(embed=emBed) 
    print("helpth")






@bot.command()
async def  helpjp(ctx):
    
    emBed = discord.Embed(title="3/15evo", color=0x1a91ff)
    emBed.add_field(name="help", value="ヘルプコマンドを取得",inline=False)
    emBed.add_field(name="send[comming soon]", value="+text", inline=False)
    emBed.add_field(name="listen", value="音楽", inline=False)
    emBed.add_field(name="random", value="乱数", inline=False)
    emBed.set_thumbnail(url='https://i.imgur.com/0GkF17z.jpg')
    emBed.add_field(name="+chekstaus", value="サーバーのステータスを確認する", inline=False)
    emBed.set_footer(text='コマンドの詳細については、+ helpコマンド名を使用してください。', icon_url='https://i.imgur.com/0GkF17z.jpg')

    await ctx.channel.send(embed=emBed)
    print("helpjp")
    


#################
@bot.command() 
async def helpliste(ctx):
     
    emoji = '\N{Reversed Hand with Middle Finger Extended}'
    await ctx.message.add_reaction(emoji)  
    emBed = discord.Embed(title="listen", color=0x1a91ff)
    emBed.add_field(name="+play", value="🎵+play <YT Link> or song name", inline=False)
    emBed.add_field(name="+pause", value="⏸️pause music", inline=False)
    emBed.add_field(name="+resume", value="▶️resume music", inline=False)
    emBed.add_field(name="+stop", value="⏹️stop music", inline=False)
    emBed.add_field(name="+skip", value="⏭️skip song", inline=False)
    emBed.add_field(name="+queue", value="⭐chek queue", inline=False)
    emBed.add_field(name="+leave", value="❌BOT leave channel", inline=False)
    emBed.set_thumbnail(url='https://i.imgur.com/0GkF17z.jpg')
    emBed.set_footer(text='thank for used BOT', icon_url='https://i.imgur.com/0GkF17z.jpg')
    await ctx.channel.send(embed=emBed) 
    print("helplisten")

####
@bot.command() 
async def helprandom(ctx):
     
    emBed = discord.Embed(title="random", description="`+givenum`,`+givenumth`", color=0x1a91ff)
    await ctx.channel.send(embed=emBed) 
    print("helprandom")

####
@bot.command() 
async def helpsend (ctx):
     
    emBed = discord.Embed(title="text", description="+text[number]", color=0x1a91ff)
    await ctx.channel.send(embed=emBed) 
    print("helpsend")

########################################
@bot.command() 
async def helpstaus(ctx):
     
    emBed = discord.Embed(title="3/15evo", color=0x1a91ff)
    emBed.add_field(name="staus", value="`+info`,`+staus`,`+time`,`+chek`",inline=False)
    await ctx.channel.send(embed=emBed) 
##########################################################################




    
@bot.event
async def on_ready():
    activity = discord.Game(name="+help", type=3)
    #staus              
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"Logged in as {bot.user}")

@bot.command()#EN
async def givenum(ctx):

    
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    embed = discord.Embed(title="Type a number", color=0x28FF73)
    await ctx.send(embed=embed)
    msg1 = await bot.wait_for("message", check=check)
    embed = discord.Embed(title="Type a second, larger number", color=0x28FF73)
    await ctx.send(embed=embed)
    msg2 = await bot.wait_for("message", check=check)
    x = int(msg1.content)
    y = int(msg2.content)
    if x < y:
        value = random.randint(x,y)
        embed = discord.Embed(title=f"you got {value}", color=0x28FF73)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="❌Please ensure the first number is smaller than the second number.", description="🔁function is ending|+givenum to use again", color=0xFF0000)
        await ctx.send(embed=embed)
#####################
@bot.command()#TH
async def givenumth(ctx):

    
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    embed = discord.Embed(title="ใส่ตัวเลข", color=0x28FF73)
    await ctx.send(embed=embed)
    msg1 = await bot.wait_for("message", check=check)
    embed = discord.Embed(title="ใส่ตัวเลขที่มากขึ้น", color=0x28FF73)
    await ctx.send(embed=embed)
    msg2 = await bot.wait_for("message", check=check)
    x = int(msg1.content)
    y = int(msg2.content)
    if x < y:
        value = random.randint(x,y)
        embed = discord.Embed(title=f"คุณใด้เลข {value}", color=0x28FF73)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="❌โปรดตรวจสอบว่าหมายเลขแรกน้อยกว่าหมายเลขที่สอง.", description="🔁ฟังก์ชั่นสิ้นสุดแล้ว|+givenumth เพื่อใช้อีกครั้ง", color=0xFF0000)
        await ctx.send(embed=embed)

#@bot.command()
#async def staus(ctx):
    #embed = discord.Embed(title="Sever Staus/สถานะเซิร์ฟเวอร์", url="https://discord.com/widget?id=805748064463486987&theme=dark", description="Delay 5min/ดีเลย์ 5 นาที", color=0xFF0000)
    #await ctx.channel.send(file=discord.File('Sever Staus.html'))   
    #await ctx.send(embed=embed)
    #return


@bot.command(brief="returns a list of the people in the voice channels in the server",)#Chek Clieant in voice channel
async def chek(ctx):
    #First getting the voice channels
    voice_channel_list = ctx.guild.voice_channels

    #getting the members in the voice channel
    for voice_channels in voice_channel_list:
        #list the members if there are any in the voice channel
        if len(voice_channels.members) != 0:
            if len(voice_channels.members) == 1:
                embed1 = discord.Embed(title=("{} member in -{}".format(len(voice_channels.members), voice_channels.name)), color=0x00FF08)#1member
                await ctx.send(embed=embed1)
            else:
                embed = discord.Embed(title=("{} members in -{}".format(len(voice_channels.members), voice_channels.name)), color=0x0400FF)#1<member
                await ctx.send(embed=embed)

            for members in voice_channels.members:
                #if user does not have a nickname in the guild, send thier discord name. Otherwise, send thier guild nickname
                if members.nick == None:
                     embed = discord.Embed(title="Member name", description=(members.name), color=0x00FFF0)
                     await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="Member nick name", description=(members.nick), color=0x00FFF0)##
                    await ctx.send(embed=embed)


    

@bot.command()
async def info(ctx):
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title=f"{ctx.guild.name}", description="Sever Staus", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
    embed.add_field(name="Member Count", value=memberCount, inline=True)


    await ctx.send(embed=embed)

@bot.command()
async def time(ctx):
    embed = discord.Embed(title=f"Time  at now", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    await ctx.send(embed=embed)
    return

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.CommandNotFound):
        embed = discord.Embed(description="Command not found", color=0xFF0000)
        await ctx.send(embed=embed)
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)


  
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Command not found", color=0xFF0000)
        await ctx.send(embed=embed)
    if PermissionError(error):
        embed = discord.Embed(title='❌your permission can,t use this command ', description='need **`manage message`** to **`clear message`**', color=0xFF0000)
        await ctx.send(embed=embed)
@bot.command()
async def ping(ctx):
    embed = discord.Embed(description=(f'🏓pong__``{round (bot.latency * 1000)}``__ms'), timestamp=datetime.datetime.utcnow(), color=0x1a91ff)
    await ctx.send(embed=embed)
    
        
     
#########################
bot.run(os.getenv('TOKEN'))