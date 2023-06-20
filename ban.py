import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} has been banned.')
        except discord.Forbidden:
            await ctx.send("I don't have the permission to ban members.")
        except discord.HTTPException:
            await ctx.send('Banning failed. Please try again.')

def setup(bot):
    bot.add_cog(Ban(bot))
