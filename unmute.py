import discord
from discord.ext import commands

class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        # Get the mute role (replace 'Muted' with your actual mute role name)
        mute_role = discord.utils.get(ctx.guild.roles, name='Muted')

        if not mute_role:
            await ctx.send("The Muted role does not exist.")
            return

        if mute_role not in member.roles:
            await ctx.send(f"{member.mention} is not muted.")
            return

        # Remove the mute role from the member
        await member.remove_roles(mute_role)
        await ctx.send(f"{member.mention} has been unmuted.")

def setup(bot):
    bot.add_cog(Unmute(bot))
