import discord
from discord.ext import commands

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unban(self, ctx, member_id: int):
        banned_users = await ctx.guild.bans()
        member = discord.utils.get(banned_users, user__id=member_id)

        if member:
            await ctx.guild.unban(member.user)
            await ctx.send(f'{member.user.name} has been unbanned.')
        else:
            await ctx.send('User not found or not banned.')

def setup(bot):
    bot.add_cog(Unban(bot))
