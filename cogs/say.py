import discord
from discord.ext import commands
from discord.commands import slash_command


class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Lass den Bot eine Nachricht senden")
    async def say(self, ctx, text: str, channel: discord.TextChannel):
        await channel.send(text)
        await ctx.respond("✅ 〢 Nachricht gesendet", ephemeral=True)


def setup(bot):
    bot.add_cog(Say(bot))
