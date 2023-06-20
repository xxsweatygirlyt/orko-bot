import discord
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        embed = discord.Embed(title=f"Avatar - {member.name}", color=discord.Color.blue())
        embed.set_image(url=member.avatar_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Avatar(bot))
