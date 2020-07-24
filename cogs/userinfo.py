import discord
import asyncio
from discord.ext import commands

class Play(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='유저정보')
    async def profile(self, ctx, u: str = None):
        if not u:
            user = ctx.author
        else:
            try:
                user = await commands.MemberConverter().convert(ctx, u)
            except discord.ext.commands.errors.BadArgument:
                return await ctx.send(f'🚨 {u}님과 관련한 정보를 찾을 수 없습니다. 🚨')
        embed = discord.Embed(title=f'{user.name}의 정보', color=user.color)
        embed.add_field(name='유저 닉네임', value=user.mention)
        embed.add_field(name='유저 ID', value=user.id)
        embed.add_field(name='최고 보유 역할', value=user.top_role.mention)
        embed.add_field(name='현재 상태', value=user.status)
        joined_at = user.joined_at.strftime("%Y-%m-%d")
        embed.add_field(name='서버 접속 일자', value=joined_at)
        embed.set_thumbnail(url=user.avatar_url)
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Play(bot))