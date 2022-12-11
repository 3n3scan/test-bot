from discord.ext import commands
from discord.commands import slash_command, Option
from discord import option
import discord

from datetime import datetime
import asyncio


class Purge(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Löscht eine bestimmte Anzahl an Nachrichten")
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, amount: Option(int)):
        amount = amount+1
        if amount > 101:
            await ctx.respond("`❌ 〢 Ich kann nicht mehr als 100 Nachrichten Löschen!`", ephemeral=True)
        else:
            deleted = await ctx.channel.purge(limit=amount)
            await ctx.respond('`✅ 〢 Erfolgreich {} Message(s) Nachrichten gelöscht!'.format(len(deleted)), delete_after=3, ephemeral=True)


def setup(bot):
     bot.add_cog(Purge(bot))