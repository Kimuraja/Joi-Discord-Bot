import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = True
intents.message_content = True


def run_discord_bot():
    TOKEN = "Your Token"

    client = commands.Bot(command_prefix=">", intents=intents)
    client.remove_command("help")

    @client.group(invoke_without_command=True)
    async def help(ctx):
        em = discord.Embed(title=f"Hey, **{ctx.author}**, I am Joi", description="A Discord Music Bot With Many "
                                                                                 "Awesome Features, Buttons, Menus, "
                                                                                 "Context Menu, Support Many Sources, "
                                                                                 "Customizable Settings\n\nOver **5** "
                                                                                 "`>help <command>` Commands",
                           color=ctx.author.color)
        em.add_field(name="**Moderation**", value="`>help kick` SOON\n"
                                                  "`>help ban` SOON\n"
                                                  "`>help warn` SOON\n"
                                                  "`>help remind` SOON")
        em.add_field(name="**Fun**", value="`Music YT, Spotify` SOON\n")
        await ctx.send(embed=em)

    @help.command()
    async def kick(ctx):
        em = discord.Embed(title="**Kick**", description="Get rid of the replicant from this server using this command."
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="`>help kick <member> [reason]`")
        await ctx.send(embed=em)

    @help.command()
    async def ban(ctx):
        em = discord.Embed(title="**Ban**", description="Make sure the replicant doesn't come back using this command."
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="`>help ban <member> [reason]`")
        await ctx.send(embed=em)

    @help.command()
    async def warn(ctx):
        em = discord.Embed(title="**Warn**", description="SOON"
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="`>help warn <member> [reason]`")
        await ctx.send(embed=em)

    @help.command()
    async def remind(ctx):
        em = discord.Embed(title="**Reminder**", description="SOON"
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="`>help remind <member> [What did you want to be reminded of]`")
        await ctx.send(embed=em)

    @help.command()
    async def play(ctx):
        em = discord.Embed(title="**Reminder**", description="SOON"
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="`>help play <song>`")
        await ctx.send(embed=em)

    client.run(TOKEN)
