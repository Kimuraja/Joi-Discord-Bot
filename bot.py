import discord
from discord.ext import commands
import os
import youtube_dl

TOKEN = "Your Token"
intents = discord.Intents().all()


def run_discord_bot():
    client = commands.Bot(command_prefix=">", intents=intents, help_command=None)

    @client.group()
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

    @client.command()
    async def kick(ctx):
        em = discord.Embed(title="**Kick**",
                           description="Get rid of the replicant from this server using this command."
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="`>help kick <member> [reason]`")
        await ctx.send(embed=em)

    @client.command()
    async def ban(ctx):
        em = discord.Embed(title="**Ban**",
                           description="Make sure the replicant doesn't come back using this command."
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="`>help ban <member> [reason]`")
        await ctx.send(embed=em)

    @client.command()
    async def warn(ctx):
        em = discord.Embed(title="**Warn**", description="SOON"
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="`>help warn <member> [reason]`")
        await ctx.send(embed=em)

    @client.command()
    async def remind(ctx):
        em = discord.Embed(title="**Reminder**", description="SOON"
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="`>help remind <member> [What did you want to be reminded of]`")
        await ctx.send(embed=em)

    @client.command(pass_context=True)
    async def play(ctx):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You're not in a voice channel, you must be in a vc to run this command")

    @client.command(pass_context=True)
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
            await ctx.send("Goodbye")
        else:
            await ctx.send("I am not in a vc")

    client.run(TOKEN)
