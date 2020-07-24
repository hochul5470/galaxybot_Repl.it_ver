import asyncio
import discord
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup
from urllib import request
import urllib
import urllib.parse, urllib.request, re

class Search(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="유튜브")
    async def youtube(self, ctx, *, search):

        query_string = urllib.parse.urlencode({
            'search_query': search
        })
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string
        )
        search_results = re.findall(r'/watch\?v=(.{11})', htm_content.read().decode())
        await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])

def setup(bot):
    bot.add_cog(Search(bot))