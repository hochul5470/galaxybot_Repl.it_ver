import discord
from discord.ext import commands

class Play(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="서버정보")
    async def serverinfo(self, ctx, guild: discord.Guild = None):
        guild = ctx.guild if not guild else guild
        embed = discord.Embed(title=f"{guild} 서버 정보", timestamp =ctx.message.created_at, color=discord.Color.blue())
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="**체널 갯수**", value= len(guild.channels))
        embed.add_field(name="**역할 갯수**", value=len(guild.roles))
        embed.add_field(name="**서버 부스터 수**", value= guild.premium_subscription_count,)
        embed.add_field(name="**서버 생성일**", value=guild.created_at)
        embed.add_field(name="**서버 최대 이모지 갯수**", value=guild.emoji_limit)
        embed.add_field(name="**서버 주인**", value=guild.owner)
        embed.set_footer(text=f"{guild} 서버 정보")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Play(bot))