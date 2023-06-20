import discord
from discord.ext import commands


class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def timeout(self, ctx, member: discord.Member, duration: int):
        # Add your timeout logic here
        # For example, you can assign a timeout role to the member for the given duration
        # Make sure to handle any errors that may occur during the timeout process
        try:
            # Assuming you have a timeout role named "Timeout" in your server
            timeout_role = discord.utils.get(ctx.guild.roles, name="Timeout")
            await member.add_roles(timeout_role)

            await ctx.send(f"{member.mention} has been timed out for {duration} seconds.")
            await asyncio.sleep(duration)
            await member.remove_roles(timeout_role)
            await ctx.send(f"{member.mention} has been un-timed out.")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")


def setup(bot):
    bot.add_cog(Timeout(bot))
