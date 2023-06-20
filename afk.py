import discord
from discord.ext import commands

class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_users = {}  # Store AFK users and their reasons

    @commands.command()
    async def afk(self, ctx, *, reason=None):
        """Set yourself as AFK with an optional reason"""
        user = ctx.author
        self.afk_users[user.id] = reason

        await ctx.send(f'{user.mention} is now AFK.')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.author.id in self.afk_users:
            afk_reason = self.afk_users[message.author.id]
            del self.afk_users[message.author.id]
            await message.channel.send(f'{message.author.mention} is no longer AFK.')

        for mention in message.mentions:
            if mention.id in self.afk_users:
                afk_reason = self.afk_users[mention.id]
                await message.channel.send(f'{mention.mention} is AFK: {afk_reason}')
                break

def setup(bot):
    bot.add_cog(AFK(bot))
