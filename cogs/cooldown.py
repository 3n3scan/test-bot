from discord.ext import commands
from discord.commands import slash_command


class Cooldown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_command(description="Hey Command mit Cooldown")
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def hey(self, ctx):
        await ctx.respond("👋 〢 Hey!")


    @staticmethod
    def convert_time(seconds: int) -> str:
        if seconds < 60:
            return f"{round(seconds)} Sekunden"
        minutes = seconds / 60
        if minutes < 60:
            return f"{round(minutes)} Minuten"
        hours = minutes / 60
        if hours < 24:
            return f"{round(hours)} Stunden"
        days = hours / 24
        if days < 7:
            return f"{round(days)} Tage"
        months = days / 31
        if months < 12:
            return f"{round(months)} Monate"
        years = months / 12
        if years < 1:
            return f"{round(years)} Jahre"


    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            seconds = ctx.command.get_cooldown_retry_after(ctx)
            final_time = self.convert_time(seconds)

            await ctx.respond(f"⚠ 〢 Du kannst den Command wieder in {final_time} Sekunden ausführen.", ephemeral=True)


def setup(bot):
    bot.add_cog(Cooldown(bot))