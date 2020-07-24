import asyncio
import discord
from discord.ext import commands
import random

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="차단")
    async def ban(self, ctx, user: str = None, *, reason: str = None):
        if not ctx.author.guild_permissions.ban_members:
            return await ctx.send('🚨 당신은 이 명령어를 사용 할 권한이 부족합니다. `유저 차단하기` 권한을 추가해주세요! 🚨')
        if not user:
            return await ctx.send('🚨 차단할 유저 맨션 또는 아이디를 입력해주세요. 🚨')
        if reason is None:
            reason = '사유를 적지 않음'
        try:
            member = await commands.MemberConverter().convert(ctx, user)
        except discord.ext.commands.errors.BadArgument:
            return await ctx.send(f'🚨 {user}(와)과 일치하는 유저를 찾지 못 했어요! 🚨')
        try:
            await ctx.guild.ban(member, reason=reason)
        except discord.errors.Forbidden:
            return await ctx.send('🚨 봇의 권한이 부족합니다. `관리자` 역할을 추가해주세요! 🚨')
        embed = discord.Embed(title='🚨유저 차단 완료🚨', color=0xDDEED,
                        description=f'{member.mention}님이 서버에서 차단 되셨습니다'
                                    f'\n처리자: {ctx.author.mention}'
                                    f'\n사유: {reason}')
        return await ctx.send(ctx.author.mention, embed=embed)

def setup(bot):
    bot.add_cog(Admin(bot))