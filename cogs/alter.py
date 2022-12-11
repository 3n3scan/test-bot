import discord
from discord.ext import commands
from discord.commands import slash_command


class Alter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="userinfo", description="Zeige Infos über einen User")
    async def info(self, ctx, alter: int, user: discord.Member = None):
        if user is None:
            user = ctx.author

        embed = discord.Embed(
            title=f"Infos über {user.name}",
            description=f"Hier siehst du alle Details über {user.mention}",
            color=discord.Color.blue()
        )

        time = discord.utils.format_dt(user.created_at, "R")

        embed.add_field(name="Account erstellt", value=time, inline=False)
        embed.add_field(name="Discord User ID", value=user.id)
        embed.add_field(name="Alter", value=alter)

        embed.set_author(name=user.name, icon_url=user.avatar.url)
        embed.set_thumbnail(url=user.avatar.url)
        embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.display_avatar.url)

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Alter(bot))
