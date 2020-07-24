import asyncio
import discord
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup
from urllib import request
import urllib

class Search(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="검색")
    async def search(self, ctx, *, search_query):
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

def setup(bot):
    bot.add_cog(Search(bot))