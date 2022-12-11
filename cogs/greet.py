import discord
from discord.ext import commands
from discord.commands import slash_command


class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Grüße einen User")
    async def greet(self, ctx):
        await ctx.respond(f"Hey {ctx.author.mention} 👋")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            title="Willkommen",
            description=f"Hey {member.mention} 👋",
            color=discord.Color.orange()
        )

        channel = await self.bot.fetch_channel(947094779370561587)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Greet(bot))
