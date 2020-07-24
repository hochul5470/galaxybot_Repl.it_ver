import asyncio
import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="입풀기")
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member=None):
        if not member:
            await ctx.send("입풀기를 지급을 원하는 사람을 맨션 해주세요!")
            return
        role = discord.utils.get(ctx.guild.roles, name="muted")
        await member.remove_roles(role)
        await ctx.send(f"> {member.mention} 님의 입막기를 풀었습니다!")
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("당신은 입풀기를 할 권한이 없습니다.")

def setup(bot):
    bot.add_cog(Admin(bot))