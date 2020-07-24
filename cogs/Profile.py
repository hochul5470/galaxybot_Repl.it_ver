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

    @commands.command(name="거울", pass_context=True)
    async def avatar(self, ctx, *, member: discord.Member=None):
        if not member:
            member = ctx.message.author
        userAvatar = member.avatar_url
        await ctx.send(userAvatar)

def setup(bot):
    bot.add_cog(Play(bot))