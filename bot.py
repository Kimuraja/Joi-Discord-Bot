import discord
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import dotenv_values
from discord.ext import commands

config = dotenv_values(".env")
# API_KEY = "Your Token"
TOKEN = "Your Token"
intents = discord.Intents().all()
client = commands.Bot(command_prefix=">", intents=intents, help_command=None)

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=config['CLIENT_ID'], client_secret=config['CLIENT_SECRET']))
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}


# TODO #1 Make bot play music from spotify:
# Read the documentation
# Make connection
# Find music
# Play music
# TODO #2 Make bot warn/kick/ban/ping user:
# Ping user
# Then Warn user with a reason
# Kick
# Ban
# TODO #3 Check if there is any possibility to play music from youtube one a bot:
# Check other library than youtube_dl
# TODO #5 Find out if there is any possibility to change CHATGPT into other AI:
# Check other library than ChatGPT or find sugar mommy that will pay for it

"""Below are the functional commands used by users to interact with the bot."""


def run_discord_bot():
    @client.command()
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
    async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        if ctx.message == "help":
            em = discord.Embed(title="**Kick**", description="To kick replicant you need to use this command: "
                                                             ">kick `[user]` `[reason]`")
            await ctx.reply(embed=em)
        else:
            await user.kick(reason=reason)
            await ctx.message.delete()
            em = discord.Embed(title="**Kick**", description=f"{user} Has been kicked from the server")
            await ctx.send(embed=em)

    @client.command()
    async def ban(ctx):
        em = discord.Embed(title="**Ban**",
                           description="Make sure the replicant doesn't come back using this command.",
                           color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="```>ban <member> [reason]```")
        await ctx.reply(embed=em)

    @client.command()
    async def warn(ctx):
        em = discord.Embed(title="**Warn**", description="SOON",
                           color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="```>help warn <member> [reason]```")
        await ctx.reply(embed=em)

    @client.command()
    async def remind(ctx):
        em = discord.Embed(title="**Reminder**", description="SOON",
                           color=ctx.author.color)
        em.add_field(name="**SYNTAX**", value="```>remind <member> [What did you want to be reminded of]```")
        await ctx.reply(embed=em)

    @client.command()
    async def play(ctx, prompt):
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
        track_url = prompt
        track_info = spotify.track(track_url)
        if track_info:
            track_preview_url = track_info['album']['external_urls']['spotify']
            if track_preview_url:
                voice_client.play(discord.FFmpegOpusAudio(track_preview_url))

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

    client.run(TOKEN)


"""After paying for the ChatGPT subscription, you will have the ability to use it in your bot using the code below"""
# @client.command()
# async def gpt(ctx: commands.Context, *, prompt: str):
#     print(prompt)
#     async with aiohttp.ClientSession() as session:
#         payload = {
#             "model": "text-davinci-003",
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
