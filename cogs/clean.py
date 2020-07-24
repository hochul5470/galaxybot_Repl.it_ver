import asyncio
import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="청소", pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, *, amount=5):
        await ctx.channel.purge(limit=amount)
        await ctx.send("채팅이 청소가 되였습니다.")
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("당신은 차단 할 권한이 없습니다.")

def setup(bot):
    bot.add_cog(Admin(bot))