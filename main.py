import discord
from discord.utils import get
from discord.ext import commands
from datetime import datetime, timedelta
import random
from song import songAPI
import json
import os
from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle





bot = commands.Bot(command_prefix='+',help_command=None)

message_lastseen = datetime.now()
message2_lastseen = datetime.now()



songsInstance = songAPI()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def type(ctx, *, par):
    await ctx.channel.send("{0}".format(par))

slash = SlashCommand(bot, sync_commands=True)


@bot.command()
async def play(ctx,* ,search: str):
    await songsInstance.play(ctx, search)
    print("play")

###########################
@bot.command()
async def stop(ctx):
    await songsInstance.stop(ctx)
    print("stop")

@slash.slash(
    name="stop",
    description="stop song",
    guild_ids=[805748064463486987]
)
async def stop(ctx):
    await songsInstance.stop(ctx)
    embed = discord.Embed(description="stop song", color=0xFF0000)
    await ctx.send(embed=embed)
    print("stop")
###################

@bot.command()
async def pause(ctx):
    await songsInstance.pause(ctx)
    print("pause")

@slash.slash(
    name="pause",
    description="pause song",
    guild_ids=[805748064463486987]
)
async def pause(ctx):
    await songsInstance.pause(ctx)
    embed = discord.Embed(description="pause song", color=0xFF0000)
    await ctx.send(embed=embed)
    print("pause")

#########################
@bot.command()
async def resume(ctx):
    await songsInstance.resume(ctx)
    print("resume")

@slash.slash(
    name="resume",
    description="resume song",
    guild_ids=[805748064463486987]
)
async def resume(ctx):
    await songsInstance.resume(ctx)
    embed = discord.Embed(description="resume song", color=0xFF0000)
    await ctx.send(embed=embed)
    print("resume")
#########################
@bot.command()
async def leave(ctx):
    await songsInstance.leave(ctx)
    print("leave")

@slash.slash(
    name="leave",
    description="leave song",
    guild_ids=[805748064463486987]
)
async def leave(ctx):
    await songsInstance.leave(ctx)
    embed = discord.Embed(description="leave song", color=0xFF0000)
    await ctx.send(embed=embed)
    print("leave")
###########################
@bot.command()
async def queue(ctx):
    await songsInstance.queue(ctx)
    print("queue")

@slash.slash(
    name="queue",
    description="queue song",
    guild_ids=[805748064463486987]
)
async def queue(ctx):
    await songsInstance.queue(ctx)
    print("queue")
#############################

@bot.command()
async def skip(ctx):
    await songsInstance.skip(ctx)
    print("skip")

@slash.slash(
    name="skip",
    description="skip song",
    guild_ids=[805748064463486987]
)
async def skip(ctx):
    await songsInstance.skip(ctx)
    embed = discord.Embed(description="skip song", color=0xFF0000)
    await ctx.send(embed=embed)
    print("skip")
################################


###############Command help en
@bot.command() 
async def help(ctx):
     
    emBed = discord.Embed(title="3/15evo", color=0x1a91ff)
    emBed.add_field(name="help", value="Get help command",inline=False)
    emBed.add_field(name="send[comming soon]", value="+text", inline=False)
    emBed.add_field(name="listen", value="Music", inline=False)
    emBed.add_field(name="random", value="random number", inline=False)
    emBed.set_thumbnail(url='https://i.imgur.com/0GkF17z.jpg')
    emBed.add_field(name="staus", value="Check server status", inline=False)
    emBed.add_field(name="language", value="`th-ไทย`,`jp-ญี่ปุ่น`", inline=False)
    emBed.set_footer(text='To get more info on a command, do +help command name', icon_url='https://i.imgur.com/0GkF17z.jpg')
    
    buttons = [
        create_button(style=ButtonStyle.URL, label="Invite BOT", url="https://discord.com/api/oauth2/authorize?client_id=865808924472377374&permissions=1644972474103&scope=bot%20applications.commands"),
        create_button(style=ButtonStyle.URL, label="Another BOT", url="https://discord.com/api/oauth2/authorize?client_id=945581746743816233&permissions=1644972474103&scope=bot%20applications.commands")

    ]
    action_row = create_actionrow(*buttons)
   
    await ctx.send(components=[action_row],embed=emBed)
    print("help")

###################help slash
@slash.slash(
    name="help",
    description="Get help command",
    guild_ids=[805748064463486987]

)
async def help(ctx):
     
    emBed = discord.Embed(title="3/15evo", color=0x1a91ff)
    emBed.add_field(name="help", value="Get help command",inline=False)
    emBed.add_field(name="send[comming soon]", value="+text", inline=False)
    emBed.add_field(name="listen", value="Music", inline=False)
    emBed.add_field(name="random", value="random number", inline=False)
    emBed.set_thumbnail(url='https://i.imgur.com/0GkF17z.jpg')
    emBed.add_field(name="staus", value="Check server status", inline=False)
    emBed.add_field(name="language", value="`th-ไทย`,`jp-ญี่ปุ่น`", inline=False)
    emBed.set_footer(text='To get more info on a command, do +help command name', icon_url='https://i.imgur.com/0GkF17z.jpg')
    await ctx.channel.send(embed=emBed) 
    print("help")
######################

@slash.slash(
    name="helpth",
    description="คำสั่งช่วยเหลือ",
    guild_ids=[805748064463486987]

)
async def helpth(ctx):
     
    emBed = discord.Embed(title="3/15evo", color=0x1a91ff)
    emBed.add_field(name="+help", value="ดูคำสั้งทั้งหมดขอบบอท",inline=False)
    emBed.add_field(name="send[comming soon]", value="+text", inline=False)
    emBed.add_field(name="listen", value="เปิดเพลง", inline=False)
    emBed.add_field(name="random", value="สุ่มตัวเลข", inline=False)
    emBed.set_thumbnail(url='https://i.imgur.com/0GkF17z.jpg')
    emBed.set_footer(text='To get more info on a command, do +help command name', icon_url='https://i.imgur.com/0GkF17z.jpg')
    emBed.add_field(name="staus", value="ตรวจสอบสถานะเซิร์ฟเวอร์", inline=False)

    await ctx.channel.send(embed=emBed) 
    print("helpth-slash")

@bot.command()
async def helpth(ctx):
     
    emBed = discord.Embed(title="3/15evo", color=0x1a91ff)
    emBed.add_field(name="+help", value="ดูคำสั้งทั้งหมดขอบบอท",inline=False)
    emBed.add_field(name="send[comming soon]", value="+text", inline=False)
    emBed.add_field(name="listen", value="เปิดเพลง", inline=False)
    emBed.add_field(name="random", value="สุ่มตัวเลข", inline=False)
    emBed.set_thumbnail(url='https://i.imgur.com/0GkF17z.jpg')
    emBed.set_footer(text='To get more info on a command, do +help command name', icon_url='https://i.imgur.com/0GkF17z.jpg')
    emBed.add_field(name="staus", value="ตรวจสอบสถานะเซิร์ฟเวอร์", inline=False)

    await ctx.channel.send(embed=emBed) 
    print("helpth")



@slash.slash(
    name="helpjp",
    description="ヘルプコマンド",
    guild_ids=[805748064463486987]

)
async def helpjp(ctx):
     
    emBed = discord.Embed(title="3/15evo", color=0x1a91ff)
    emBed.add_field(name="help", value="ヘルプコマンドを取得",inline=False)
    emBed.add_field(name="send[comming soon]", value="+text", inline=False)
    emBed.add_field(name="listen", value="音楽", inline=False)
    emBed.add_field(name="random", value="乱数", inline=False)
    emBed.set_thumbnail(url='https://i.imgur.com/0GkF17z.jpg')
    emBed.add_field(name="staus", value="サーバーのステータスを確認する", inline=False)
    await ctx.channel.send(embed=emBed)
    print("helpjp-slash")

@bot.command()
async def  helpjp(ctx):
    
    emBed = discord.Embed(title="3/15evo", color=0x1a91ff)
    emBed.add_field(name="help", value="ヘルプコマンドを取得",inline=False)
    emBed.add_field(name="send[comming soon]", value="+text", inline=False)
    emBed.add_field(name="listen", value="音楽", inline=False)
    emBed.add_field(name="random", value="乱数", inline=False)
    emBed.set_thumbnail(url='https://i.imgur.com/0GkF17z.jpg')
    emBed.add_field(name="staus", value="サーバーのステータスを確認する", inline=False)
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

@slash.slash(
    name="helpliste",
    description="see command play song",
    guild_ids=[805748064463486987,876792716514689064]

)
async def helpliste(ctx):
    
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

##########################
@bot.command() 
async def helprandom(ctx):
     
    emBed = discord.Embed(title="random", description="+givenum", color=0x1a91ff)
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
async def send(ctx):
    print(ctx.channel)
    await ctx.channel.send('hello')

@bot.event #async/await
async def on_message(message):
    global message_lastseen, message2_lastseen
    if message.content == '!user':
        await message.channel.send(str(message.author.name) + ' Hello')
    elif message.content == 'นายชื่ออะไร' and datetime.now() >= message_lastseen:
        message_lastseen = datetime.now() + timedelta(seconds=5)
        await message.channel.send('ฉันชื่อ ' + str(bot.user.name))
        #logging 
        print('{0} เรียกใช้ นายชื่ออะไร ตอน {1} และจะใช้ได้อีกทีตอน {2}'.format(message.author.name,datetime.now(),message_lastseen))
    elif message.content == 'ผมชื่ออะไร' and datetime.now() >= message2_lastseen:
        message2_lastseen = datetime.now() + timedelta(seconds=5)
        await message.channel.send('นายชื่อ ' + str(message.author.name))
    
    await bot.process_commands(message)
    
@bot.event
async def on_ready():
    activity = discord.Game(name="/help,+help|กำลังเพิ่มฝังชั่น🟡", type=3)
    #staus              
    await bot.change_presence(status=discord.Status.idle, activity=activity)
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
        embed = discord.Embed(title="❌โปรดตรวจสอบว่าหมายเลขแรกน้อยกว่าหมายเลขที่สอง.", description="🔁ฟังก์ชั่นสิ้นสุดแล้ว|+givenum เพื่อใช้อีกครั้ง", color=0xFF0000)
        await ctx.send(embed=embed)

@bot.command()
async def staus(ctx):
    embed = discord.Embed(title="Sever Staus/สถานะเซิร์ฟเวอร์", url="https://discord.com/widget?id=805748064463486987&theme=dark", description="Delay 5min/ดีเลย์ 5 นาที", color=0xFF0000)
    await ctx.channel.send(file=discord.File('Sever Staus.html'))   
    await ctx.send(embed=embed)
    return

@bot.command(help = "Prints details of Server")
async def Information(ctx):
    owner=str(ctx.guild.owner)
    region = str(ctx.guild.region)
    guild_id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    desc=ctx.guild.description
    
    embed = discord.Embed(
        title=ctx.guild.name + " -Server Information",
        description=desc,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)


@bot.command(brief="returns a list of the people in the voice channels in the server",)#Chek Clieant in voice channel
async def chek(ctx):
    #First getting the voice channels
    voice_channel_list = ctx.guild.voice_channels

    #getting the members in the voice channel
    for voice_channels in voice_channel_list:
        #list the members if there are any in the voice channel
        if len(voice_channels.members) != 0:
            if len(voice_channels.members) == 1:
                embed = discord.Embed(title=("{} member in -{}".format(len(voice_channels.members), voice_channels.name)), color=0x00FF08)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title=("{} members in -{}".format(len(voice_channels.members), voice_channels.name)), color=0x0400FF)##
                await ctx.send(embed=embed)

            for members in voice_channels.members:
                #if user does not have a nickname in the guild, send thier discord name. Otherwise, send thier guild nickname
                if members.nick == None:
                     embed = discord.Embed(description=(members.name), color=0x00FFF0)
                     await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="Member name", description=(members.nick), color=0x00FFF0)##
                    await ctx.send(embed=embed)


@bot.command()
async def button(ctx):
    
    buttons = [
        create_button(style=ButtonStyle.green, label="Hello"),
        create_button(style=ButtonStyle.URL, label="Example Invite Button", url="https://google.com")
    ]
    action_row = create_actionrow(*buttons)
   
    await ctx.send(components=[action_row])
            


























































#########################
bot.run('token')