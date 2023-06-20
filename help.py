import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='Help Menu', description='List of available commands:', color=discord.Color.blue())

        for command in self.bot.commands:
            embed.add_field(name=command.name, value=command.help, inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
