import discord
from discord.ext import commands

class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="태스트")
    async def printit(self, ctx):
        await ctx.send(":) Galaxy Bot 태스트 출력 매시지.")

def setup(bot):
    bot.add_cog(Test(bot))