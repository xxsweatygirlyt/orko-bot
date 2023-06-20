import discord
from discord.ext import commands

class Untimeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def untimeout(self, ctx, member: discord.Member):
        # Remove the timeout role from the member
        timeout_role = discord.utils.get(ctx.guild.roles, name="Timeout")
        if timeout_role in member.roles:
            await member.remove_roles(timeout_role)
            await ctx.send(f"{member.mention} has been untimeouted.")
        else:
            await ctx.send(f"{member.mention} is not currently timeouted.")

def setup(bot):
    bot.add_cog(Untimeout(bot))
