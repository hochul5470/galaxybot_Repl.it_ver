import asyncio
import discord
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup
import urllib.parse, urllib.request, re
import urllib
import time
from urllib import request
from discord import guild, member, user
import os
import json
from Dtime import Uptime
 
async def bt(games):
    await bot.wait_until_ready()

    while not bot.is_closed():
        for g in games:
            await bot.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(10)

bot = commands.Bot(command_prefix='?')
Uptime.uptimeset()

token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcxMzE4ODgwNTcxNjIxMzc3MSIsImlhdCI6MTU5NTMwMDA5OSwiZXhwIjoxNjI2ODU3Njk5fQ.R7Z1mD3w1Op5zpljZn09mLuMQkaEaYxgnd6CjuR_YTDkCQPVPnjtckh1pt-EeAn_faQbqZzXKqJaRfMUfmBI5_dIunPKdB3K4089DFlgbXae3kkssoTacYTLX3cMYpjXnsO_SsWwAzw8iBHmxH9w2xtST4VZXsiU7CceuFrWAn0"
calcResult = 0

@bot.event
async def on_ready():
    print("team.DBMAH GALAXY BOT 봇")
    await bt(["GALAXY BOT 입니다! (made by 호철Hochul)", "본 메시지는 10초에 1번씩 봐꿔저요!", "?명령어를 이용해 명령어 확인해주세요!", "http://dbmah.na.co"])
    await asyncio.sleep(1800)
    os.system("start main_discord_bot.py")

@bot.listen()
async def on_message(message):
    if message.content == '?업타임':
        uptime = str(Uptime.uptime()).split(":")
        hours = uptime[0]
        minitues = uptime[1]
        seconds = uptime[2].split(".")[0]
        await message.channel.send(f"{hours}시간 {minitues}분 {seconds}초 `(Galaxy Bot은 호스팅 안정화 및 봇 안정화를 하루에 1번씩 리붓 됩니다!)`")

    if message.content == '?hellothisisverification':
        await message.channel.send("호철Hochul#9017 님이 봇을 제작 했습니다!")

@bot.command(name="따라하기", pass_context=True)
async def _saySame(ctx, *, args):
    await ctx.send(args)

@bot.command(name="검색")
async def _search_blog(ctx, *, search_query):
    temp = 0
    url_base = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="
    url = url_base + urllib.parse.quote(search_query)
    title = ["", "", "", "", "", "", "", "", "", "", ""]
    link = ["", "", "", "", "", "", "", "", "", "", ""]
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
    result = soup.find_all('a', "sh_blog_title _sp_each_url _sp_each_title")
    embed = discord.Embed(title="검색 결과 내용", description=" ", color=0xDDEED)
    for n in result:
        if temp == 10:
            break
        title[temp] = n.get("title")
        link[temp] = n.get("href")
        embed.add_field(name=title[temp], value=link[temp], inline=False)
        temp+=1
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/710514305291780097/733719518043439194/20200718_011811.jpg")
    embed.set_footer(text="GALAXY BOT 검색 완료!")
    await ctx.send(embed=embed)

@bot.command(name="유튜브")
async def youtube(ctx, *, search):

    query_string = urllib.parse.urlencode({
        'search_query': search
    })
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string
    )
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])

@bot.command(name="핑", pass_context=True)
async def ping(ctx):
   await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command(name="프사", pass_context=True)
async def avatar(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

@bot.command(name="서버정보")
async def serverinfo(ctx, guild: discord.Guild = None):
    guild = ctx.guild if not guild else guild
    embed = discord.Embed(title=f"{guild} 서버 정보", timestamp =ctx.message.created_at, color=discord.Color.blue())
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="**체널 갯수**", value= len(guild.channels))
    embed.add_field(name="**역할 갯수**", value=len(guild.roles))
    embed.add_field(name="**서버 부스터 수**", value= guild.premium_subscription_count,)
    embed.add_field(name="**서버 생성일**", value=guild.created_at)
    embed.add_field(name="**서버 최대 이모지 갯수**", value=guild.emoji_limit)
    embed.add_field(name="**서버 주인**", value=guild.owner)
    embed.set_footer(text=f"{guild} 서버 정보")
    await ctx.send(embed=embed)

@bot.command(name="커뮤니티")
async def helpdiscord(ctx):
        embed = discord.Embed(title="Team.KDB 커뮤니티 초대링크", color=0xDDEED)
        embed.add_field(value="https://discord.gg/tCKxyEZ", name="Team. KDB디스코드", inline=False)
        embed.add_field(value="http://team-kdb.na.to", name="공식 Team. KDB 깃북사이트", inline=False)
        embed.add_field(value="`Team.DBMAH 커뮤니티에서는 봇 코딩에 관한 질문, 민원 신고와 디스코드 관련 봇 코드 질문 등을 할수가 있습니다.`", name="커뮤니티 이용안내", inline=False)
        embed.set_footer(text="GALAXY BOT")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/710514305291780097/733719518043439194/20200718_011811.jpg")        
        await ctx.send(embed=embed)

@bot.command(name="명령어")
async def command(ctx):
        embed = discord.Embed(title="GALAXY BOT 명령어 목록", color=0xDDEED)
        embed.add_field(value="`서버정보를 알려줍니다`", name="?서버정보", inline=False)
        embed.add_field(value="`Team.DBMAH 서버 초대링크를 줍니다`", name="?커뮤니티", inline=False)
        embed.add_field(value="`봇 명령어를 알려줍니다`", name="?명령어", inline=False)
        embed.add_field(value="`자신의 컴퓨터의 핑을 알려줍니다`", name="?핑", inline=False)
        embed.add_field(value="`유저가 한 말을 따라합니다`", name="?따라하기 <할말>", inline=False)
        embed.add_field(value="`채팅창 매시지를 청소해줍니다`", name="?청소 <숫자>", inline=False)
        embed.add_field(value="`인터넷에 있는 정보를 검색해줍니다`", name="?검색", inline=False)
        embed.add_field(value="`유튜브 영상을 검색해줍니다`", name="?유튜브", inline=False)
        embed.add_field(value="`서버 컴퓨터 사양을 알려줍니다`", name="?사양", inline=False)
        embed.add_field(value="`봇 업타임을 알려드립니다`", name="?업타임", inline=False)
        embed.add_field(value="`관리자명령어를 알려줍니다`", name="?관리자명령어", inline=False)
        embed.set_footer(text="GALAXY BOT")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/710514305291780097/733719518043439194/20200718_011811.jpg")        
        await ctx.send(embed=embed)

@bot.command(name="관리자명령어")
@commands.has_permissions(administrator=True)
async def mcommand(ctx):
        embed = discord.Embed(title="GALAXY BOT 관리자전용 명령어 목록", color=0xDDEED)
        embed.add_field(value="`맨션이 된 사람을 추방합니다`", name="?추방", inline=False)
        embed.add_field(value="`맨션이 된 사람을 차단합니다`", name="?차단", inline=False)
        embed.add_field(value="`맨션이 된 사람의 입을 막습니다`", name="?입막기", inline=False)
        embed.add_field(value="`입막기가 된 사람의 입을 풉니다`", name="?입풀기", inline=False)
        embed.add_field(value="`채팅창을 청소합니다`", name="?청소", inline=False)
        embed.set_footer(text="GALAXY BOT")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/710514305291780097/733719518043439194/20200718_011811.jpg")        
        await ctx.send(embed=embed)
@mcommand.error
async def mcommand_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("당신은 관리자 명령어를 확인 할 권한이 없습니다.")

@bot.command(name="추방")
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("추방을 원하는 사람을 맨션 해주세요!")
        return
    await member.kick()
    await ctx.send(f"> {member.mention} 님께서 서버추방 되셨습니다")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("당신은 추방를 할 권한이 없습니다.")

@bot.command(name="입막기")
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("입막기를 지급을 원하는 사람을 맨션 해주세요!")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    await ctx.send(f"> {member.mention} 님의 입을 막았습니다!")
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("당신은 입풀기를 할 권한이 없습니다.")

@bot.command(name="입풀기")
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("입풀기를 지급을 원하는 사람을 맨션 해주세요!")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)
    await ctx.send(f"> {member.mention} 님의 입막기를 풀었습니다!")
@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("당신은 입풀기를 할 권한이 없습니다.")

@bot.command(name="차단")
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("차단 할사람의 맨션을 해주세요!")
        return
    await member.ban()
    await ctx.send(f"> {member.mention} 님이 서버에서 차단 되셨습니다.")
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("당신은 차단 할 권한이 없습니다.")

@bot.command(name="청소", pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, *, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("채팅이 청소가 되였습니다.")
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("당신은 차단 할 권한이 없습니다.")


bot.run(token)
