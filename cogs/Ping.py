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

    @commands.command(name="핑", pass_context=True)
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(Play(bot))