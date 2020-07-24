import asyncio
import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="명령어", aliases=['도움말'])
    async def command(self, ctx):
        embed = discord.Embed(title="GALAXY BOT 명령어 목록", color=0xDDEED)
        embed.add_field(value="`서버에 관한 정보를 알려줍니다`", name="?서버정보", inline=False)
        embed.add_field(value="`Team.DBMAH 서버 초대링크를 줍니다`", name="?커뮤니티", inline=False)
        embed.add_field(value="`봇 명령어를 알려줍니다`", name="?명령어", inline=False)
        embed.add_field(value="`자신의 컴퓨터의 핑을 알려줍니다`", name="?핑", inline=False)
        embed.add_field(value="`유저가 한 말을 따라합니다`", name="?따라하기 <할말>", inline=False)
        embed.add_field(value="`채팅창 매시지를 청소해줍니다`", name="?청소 <숫자>", inline=False)
        embed.add_field(value="`인터넷에 있는 정보를 검색해줍니다`", name="?검색", inline=False)
        embed.add_field(value="`유튜브 영상을 검색해줍니다`", name="?유튜브", inline=False)
        embed.add_field(value="`봇 업타임을 알려드립니다`", name="?업타임", inline=False)
        embed.add_field(value="`타이머를 자동으로 해줍니다`", name="?타이머 <숫자(1일 경우 1분)>", inline=False)
        embed.add_field(value="`유저에 관한 정보를 알려줍니다`", name="?유저정보 <맨션>", inline=False)
        embed.add_field(value="`관리자 전용 명령어를 알려줍니다 **(관리자 지급 필요!)**`", name="?관리자명령어", inline=False)
        embed.set_footer(text="GALAXY BOT")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/710514305291780097/733719518043439194/20200718_011811.jpg")        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Admin(bot))

