import discord
from discord.ext import commands

class Lockdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.locked = False

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lockdown(self, ctx):
        if self.locked:
            await ctx.send("The server is already in lockdown.")
        else:
            self.locked = True
            for channel in ctx.guild.channels:
                if isinstance(channel, discord.TextChannel):
                    await channel.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.send("The server is now in lockdown. Only administrators can send messages.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx):
        if not self.locked:
            await ctx.send("The server is not in lockdown.")
        else:
            self.locked = False
            for channel in ctx.guild.channels:
                if isinstance(channel, discord.TextChannel):
                    await channel.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.send("The server lockdown has been lifted. Normal operations have resumed.")

def setup(bot):
    bot.add_cog(Lockdown(bot))
