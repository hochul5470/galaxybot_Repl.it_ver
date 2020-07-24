import asyncio
import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="관리자명령어")
    @commands.has_permissions(administrator=True)
    async def mcommand(self, ctx):
            embed = discord.Embed(title="GALAXY BOT 관리자전용 명령어 목록", color=0xDDEED)
            embed.add_field(value="`맨션이 된 사람을 추방합니다 (유저 추방하기 권한 필요)`", name="?추방", inline=False)
            embed.add_field(value="`맨션이 된 사람을 차단합니다 (유저 차단하기 권한 필요)`", name="?차단", inline=False)
            embed.add_field(value="`맨션이 된 사람의 입을 막습니다`", name="?입막기", inline=False)
            embed.add_field(value="`입막기가 된 사람의 입을 풉니다`", name="?입풀기", inline=False)
            embed.add_field(value="`채팅창을 청소합니다`", name="?청소", inline=False)
            embed.add_field(value="`현제 채널에 공지를 쓸수 있습니다`", name="?공지", inline=False)
            embed.set_footer(text="GALAXY BOT")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/710514305291780097/733719518043439194/20200718_011811.jpg")        
            await ctx.send(embed=embed)
    @mcommand.error
    async def mcommand_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("당신은 관리자 명령어를 확인 할 권한이 없습니다.")

def setup(bot):
    bot.add_cog(Admin(bot))