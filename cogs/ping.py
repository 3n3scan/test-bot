from discord.ext import commands
from discord.commands import slash_command

## Change Template to the name of the Cog you want to create
class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @slash_command(description="Ping Command")
    async def ping(self, ctx):
        await ctx.respond(f"🏓 〢 Pong! `{round(self.bot.latency * 1000)}ms`")


def setup(bot):
    bot.add_cog(Ping(bot))
    ## change Template to the name of the Cog you want to create