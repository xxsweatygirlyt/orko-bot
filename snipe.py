import discord
from discord.ext import commands

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.deleted_messages = {}

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        self.deleted_messages[message.channel.id] = message

    @commands.command()
    async def snipe(self, ctx):
        channel = ctx.channel
        if channel.id not in self.deleted_messages:
            await ctx.send("There are no recently deleted messages.")
            return

        message = self.deleted_messages[channel.id]
        author = message.author
        content = message.content
        timestamp = message.created_at

        embed = discord.Embed(title="Sniped Message", color=discord.Color.green())
        embed.set_author(name=author.display_name, icon_url=author.avatar_url)
        embed.add_field(name="Content", value=content, inline=False)
        embed.set_footer(text=f"Deleted at {timestamp}")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Snipe(bot))
