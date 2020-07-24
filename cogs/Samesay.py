import asyncio
import discord
from discord.ext import commands

class Play(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="따라하기", pass_context=True)
    async def samesay(self, ctx, *, args):
        await ctx.send(args)

def setup(bot):
    bot.add_cog(Play(bot))