import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ext.pages import Paginator, Page


class Paginator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def page(self, ctx):
        pages = [
            Page(embeds=[discord.Embed(title="Seite 1", color=discord.Color.yellow())]),
            Page(content="Seite 2")
        ]
        paginator = Paginator(pages=pages, author_check=True, disable_on_timeout=True)
        # paginator.remove_button("first")
        # paginator.remove_button("last")

        await paginator.respond(ctx.interaction)

    @slash_command()
    async def memberlist(self, ctx):
        members = ctx.guild.members
        pages = []
        description = ""

        for index, member in enumerate(members):
            description += f"`{index + 1}.` {member}\n"

            if (index + 1) % 10 == 0 or index == len(members) - 1:
                embed = discord.Embed(title="Member List", description=description, color=discord.Color.green())
                if ctx.guild.icon:
                    embed.set_thumbnail(url=ctx.guild.icon.url)
                pages.append(embed)
                description = ""

        paginator = Paginator(pages=pages)
        await paginator.respond(ctx.interaction)


def setup(bot):
    bot.add_cog(Paginator(bot))