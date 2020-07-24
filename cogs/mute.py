import asyncio
import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="입막기")
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member=None):
        if not member:
            await ctx.send("입막기를 지급을 원하는 사람을 맨션 해주세요!")
            return
        role = discord.utils.get(ctx.guild.roles, name="muted")
        await member.add_roles(role)
        await ctx.send(f"> {member.mention} 님의 입을 막았습니다!")
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("당신은 입풀기를 할 권한이 없습니다.")

def setup(bot):
    bot.add_cog(Admin(bot))