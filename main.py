from time import sleep
import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True

status = discord.Status.dnd
activity = discord.Activity(type=discord.ActivityType.watching, name="die Wartungsarbeiten an...")

bot = discord.Bot(
    intents=intents,
    debug_guilds=[947093176508895252],
    status=status,
    activity=activity
)


@bot.event
async def on_ready():
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔄 〢 Logging in...")
    print(f"✅ 〢 Logged in as {bot.user}.")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔄 〢 Cogs Loading...")
    print(f"✅ 〢 {len(bot.cogs)} Cogs Loaded!")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔄 〢 Commands Loading...")
    print(f"✅ 〢 {len(bot.commands)} Commands Loaded!")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔄 〢 Connecting to Guild...")
    print(f"✅ 〢 {len(bot.guilds)} Guilds Loaded!")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔄 〢 Loading User...")
    print(f"✅ 〢 {len(bot.users)} Users Loaded!")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🆙 〢 Bot is ready!")
    print(f"🆙 〢 Current Status: {status}")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🌐 〢 Console Logs:")
    

if __name__ == "__main__":
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

load_dotenv()
bot.run(os.getenv("TOKEN"))
