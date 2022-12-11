from discord.ext import commands, tasks
from datetime import time, timezone


class Task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.task.start()
        self.time_task.start()

    @tasks.loop(minutes=5)
    async def task(self):
        if self.task.current_loop == 0:
            return

        channel = await self.bot.fetch_channel(947094736651575316)
        await channel.send("✅ 〢 Tasks are running!")

    @tasks.loop(
        time=time(22, 0, tzinfo=timezone.utc)
    )
    async def time_task(self):
        print("⏰ 〢 Es ist 22:00 Uhr UTC")


def setup(bot):
    bot.add_cog(Task(bot))