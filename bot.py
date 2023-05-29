import aiohttp
import discord
from discord.ext import commands
# import os
# import youtube_dl
import openai

TOKEN = ""
intents = discord.Intents().all()
API_KEY = ""

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
        em.add_field(name="**Moderation**", value="`>kick` SOON\n"
                                                  "`>ban` SOON\n"
                                                  "`>warn` SOON\n"
                                                  "`>remind` SOON")
        em.add_field(name="**Fun**", value="`Music YT, Spotify` SOON\n")
        await ctx.send(embed=em)

    @client.command()
    async def kick(ctx):
        em = discord.Embed(title="**Kick**",
                           description="Get rid of the replicant from this server using this command."
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="`>kick <member> [reason]`")
        await ctx.send(embed=em)

    @client.command()
    async def ban(ctx):
        em = discord.Embed(title="**Ban**",
                           description="Make sure the replicant doesn't come back using this command."
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="`>ban <member> [reason]`")
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
        em.add_field(name="**SYNTAX**", value="`>remind <member> [What did you want to be reminded of]`")
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

    #TODO 1 Read the documentation and make bot response with Chat GPT answer for a given question
    @client.command()
    async def gpt(ctx: commands.Context, *, prompt: str):
        print(prompt)
        async with aiohttp.ClientSession() as session:
            payload = {
                "model": "text-davinci-003",
                "prompt": prompt,
                "temperature": 0.5,
                "max_tokens": 50,
                "presence_penalty": 0,
                "frequency_penalty": 0,
                "best_of": 1,
            }
            headers = {"Authorization": f"Bearer {API_KEY}"}
            async with session.post("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
                response = await resp.json()
                em = discord.Embed(title="**GPT**", description=f"```{response}```"
                                   , color=ctx.author.color)
                await ctx.reply(embed=em)
    client.run(TOKEN)
