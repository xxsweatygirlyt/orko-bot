import discord
from discord.ext import commands

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')  # Replace 'Muted' with your desired muted role name

        if not muted_role:
            # If the muted role doesn't exist, create it
            muted_role = await ctx.guild.create_role(name='Muted')

            # Set the permissions for the muted role (adjust as needed)
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, speak=False, send_messages=False)

        await member.add_roles(muted_role)
        await ctx.send(f'{member.mention} has been muted.')

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions to use this command.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please mention a member to mute.')

def setup(bot):
    bot.add_cog(Mute(bot))
