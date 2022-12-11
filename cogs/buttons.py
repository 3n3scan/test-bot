import discord
from discord.ext import commands
from discord.commands import slash_command


class Button(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(TutorialView())

    @slash_command()
    async def button1(self, ctx):
        await ctx.respond("Klicke hier", view=TutorialView())

    @slash_command()
    async def button2(self, ctx):
        button = TutorialButton("Kekse sind cool")
        view = discord.ui.View()
        view.add_item(button)

        await ctx.respond("Klicke hier", view=view)

    @slash_command()
    async def credits(self, ctx):
        button = discord.ui.Button(label="GitHub", url="https://github.com/3n3scan")
        view = discord.ui.View()
        view.add_item(button)
        
        embed = discord.Embed(
            title="Informationen über den Bot",
            description=f"Aktuelle Version: 1.2",
            color=discord.Color.orange()
        )
        embed.add_field(name="👨🏻‍💻 • Developer:", value= "3n3scan#6908", inline=True)
        embed.add_field(name="🤖 • Prefix:", value= "/ (slash_commands)", inline=False)
        embed.add_field(name="🌐 • Debug Server:", value= "3n3scan", inline=False)
        embed.add_field(name="💠 • Host:", value= "Vinorex", inline=False)
        embed.add_field(name="ℹ • Language:", value= "German", inline=False)
        embed.add_field(name="✅ • Bot Info:", value= "This Bot is Global and inviteable", inline=False)
        embed.add_field(name="🔰 • Source Code:", value= "https://github.com/3n3scan/test-bot", inline=False)



        embed.set_author(name="3n3scan", icon_url="https://cdn.discordapp.com/avatars/773514870409789471/c68359d51206ed6dbdfb691eb898b97c.png?size=1024")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/773514870409789471/c68359d51206ed6dbdfb691eb898b97c.png?size=1024")
        embed.set_footer(text=f"test-bot v1.2 created by © 3n3scan#6908", icon_url=ctx.bot.user.display_avatar.url)

        await ctx.respond(embed=embed, view=view)


def setup(bot):
    bot.add_cog(Button(bot))

## Button Colors: https://discord.com/developers/docs/interactions/message-components#button-object-button-styles

class TutorialView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
        
    ## /button1 ⤵
    @discord.ui.button(label="Keks", style=discord.ButtonStyle.primary, emoji="🍪", custom_id="keks", row=2)
    async def button_callback1(self, button, interaction):
        await interaction.response.send_message("Keks", ephemeral=True)

    @discord.ui.button(label="Pizza", style=discord.ButtonStyle.primary, emoji="🍕", custom_id="pizza", row=1)
    async def button_callback2(self, button, interaction):
        button.disabled = True

        # Alle Buttons deaktivieren
        # for child in self.children:
        #     child.disabled = True

        await interaction.response.edit_message(view=self)
    ## /button1 ⤴
    

class TutorialButton(discord.ui.Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.green)
    ## /button2
    async def callback(self, interaction):
        await interaction.response.send_message("Hey!", ephemeral=True)
