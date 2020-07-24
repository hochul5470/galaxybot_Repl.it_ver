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

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="업타임")
    async def uptime(self, ctx):
        uptime = str(Uptime.uptime()).split(":")
        hours = uptime[0]
        minitues = uptime[1]
        seconds = uptime[2].split(".")[0]
        await ctx.send(f"{hours}시간 {minitues}분 {seconds}초 `(Galaxy Bot은 호스팅 안정화 및 봇 안정화를 하루에 1번씩 리붓 됩니다!)`")


def setup(bot):
    bot.add_cog(Admin(bot))