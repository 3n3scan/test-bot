import discord
from discord.ext import commands
from discord.commands import slash_command, Option


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_command(description="Kicke einen User aus dem Server")
    @discord.default_permissions(administrator=True, kick_members=True)
    @discord.guild_only()
    async def kick(self, ctx, member: Option(discord.Member, "Wähle den User aus, den du kicken willst"), reason: Option(str, "Gib einen Grund an, warum du den User kicken willst")):
        try:
            await member.kick(reason=reason)
        except (discord.Forbidden, discord.HTTPException) as e:
            print(e)
            await ctx.respond("⛔ 〢 Ich habe keine Berechtigung, diesen User zu kicken!", ephemeral=True)
            return
        await ctx.respond(f"✅ 〢 {member.mention} wurde gekickt! Grund: ```{reason}```", ephemeral=True)


    @slash_command(description="👋 〢 Hallo!")
    @commands.has_permissions(administrator=False)
    @commands.has_role("Member")
    async def hallo(self, ctx):
        await ctx.respond("👋 〢 Hallo!")


    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.respond("⛔ 〢 Du hast keine Berechtigung, diesen Command auszuführen!", ephemeral=True)
            return
        
        await ctx.respond(f"⚠️ 〢 Es ist ein Fehler aufgetreten:```{error}```", ephemeral=True) 
        raise error


def setup(bot):
    bot.add_cog(Admin(bot))