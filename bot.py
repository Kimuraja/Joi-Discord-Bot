import discord
from discord.ext import commands
import os
import asyncio
import youtube_dl

TOKEN = "Your Token"
intents = discord.Intents().all()
# API_KEY = "Your Token"
client = commands.Bot(command_prefix=">", intents=intents, help_command=None)
voice_clients = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}


def run_discord_bot():
    @client.group()
    async def help(ctx):
        em = discord.Embed(title=f"Hey, **{ctx.author}**, I am Joi", description="```A Discord Music Bot With Many "
                                                                                 "Awesome Features, Buttons, Menus, "
                                                                                 "Context Menu, Support Many Sources, "
                                                                                 "Customizable Settings\n\nOver **5** "
                                                                                 "`>help <command>` Commands```",
                           color=ctx.author.color)
        em.add_field(name="**Moderation**", value="`>kick` SOON\n"
                                                  "`>ban` SOON\n"
                                                  "`>warn` SOON\n"
                                                  "`>remind` SOON")
        em.add_field(name="**Fun**", value="`Music YT, Spotify` SOON\n")
        await ctx.reply(embed=em)

    @client.command()
    async def kick(ctx):
        em = discord.Embed(title="**Kick**",
                           description="Get rid of the replicant from this server using this command."
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="```>kick <member> [reason]```")
        await ctx.reply(embed=em)

    @client.command()
    async def ban(ctx):
        em = discord.Embed(title="**Ban**",
                           description="Make sure the replicant doesn't come back using this command."
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="```>ban <member> [reason]```")
        await ctx.reply(embed=em)

    @client.command()
    async def warn(ctx):
        em = discord.Embed(title="**Warn**", description="SOON"
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="```>help warn <member> [reason]```")
        await ctx.reply(embed=em)

    @client.command()
    async def remind(ctx):
        em = discord.Embed(title="**Reminder**", description="SOON"
                           , color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="```>remind <member> [What did you want to be reminded of]```")
        await ctx.reply(embed=em)

    @client.command()
    async def play(ctx, msg):
        try:
            url = msg
            voice_client = await ctx.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False, extra_info={'verbose': True}))

            song = data['url']
            player = discord.FFmpegPCMAudioSource()

            voice_client.play(player)
        except Exception as err:
            print(err)

    @client.command(pass_context=True)
    async def leave(ctx):
        if ctx.voice_client:
            em = discord.Embed()
            em.add_field(name="JOI Music", value="```Goodbye```")
            await ctx.guild.voice_client.disconnect()
            await ctx.reply(embed=em)
        else:
            em = discord.Embed()
            em.add_field(name="JOI Music", value="```An Error occurred, I am not in a vc```")
            await ctx.reply(embed=em)

    # --- After paying for the ChatGPT subscription, you will have the ability
    # to use it in your bot using the code below.--- #

    # @client.command()
    # async def gpt(ctx: commands.Context, *, prompt: str):
    #     print(prompt)
    #     async with aiohttp.ClientSession() as session:
    #         payload = {
    #             "model": "text-davinci-002",
    #             "prompt": prompt,
    #             "temperature": 0.5,
    #             "max_tokens": 50,
    #             "presence_penalty": 0,
    #             "frequency_penalty": 0,
    #             "best_of": 1,
    #         }
    #         headers = {"Authorization": f"Bearer {API_KEY}"}
    #         async with session.post("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
    #             print(resp)
    #             response = await resp.json()
    #             em = discord.Embed(title="**GPT**", description=f"```{response}```"
    #                                , color=ctx.author.color)
    #             await ctx.reply(embed=em)
    client.run(TOKEN)
