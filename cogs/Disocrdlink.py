import asyncio
import discord
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup
from urllib import request
import urllib

class Play(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="커뮤니티")
    async def helpdiscord(self, ctx):
            embed = discord.Embed(title="Team.KDB 커뮤니티 초대링크", color=0xDDEED)
            embed.add_field(value="https://discord.gg/tCKxyEZ", name="Team. KDB디스코드", inline=False)
            embed.add_field(value="http://team-kdb.na.to", name="공식 Team. KDB 깃북사이트", inline=False)
            embed.add_field(value="`Team.DBMAH 커뮤니티에서는 봇 코딩에 관한 질문, 민원 신고와 디스코드 관련 봇 코드 질문 등을 할수가 있습니다.`", name="커뮤니티 이용안내", inline=False)
            embed.set_footer(text="GALAXY BOT")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/710514305291780097/733719518043439194/20200718_011811.jpg")        
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Play(bot))