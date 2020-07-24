import asyncio
import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='공지')
    async def announce(self, ctx, *, content: str = None):
        if not content:
            return await ctx.send("전송할 메시지를 입력주세요.")
        embed = discord.Embed(title='📢 서버공지 시스탬!', description=content, color=0xDDEED)
        embed.set_footer(text=f"공지 작성자 {ctx.author}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Admin(bot))
