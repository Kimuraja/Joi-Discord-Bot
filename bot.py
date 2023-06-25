import asyncio
import discord
from datetime import datetime
import youtube_dl
from dotenv import dotenv_values
from discord.ext import commands
# from discord import Member
# from discord.ext.commands import has_permissions, MissingPermissions

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
intents = discord.Intents().all()
config = dotenv_values("data.env")
client = commands.Bot(command_prefix=">", intents=intents, help_command=None)


# TODO #1 Make bot play music from spotify/youtube:
# Read the documentation
# Make connection
# Find music
# Play music
# TODO #3 Check if there is any possibility to play music from youtube one a bot:
# Check other library than youtube_dl
# TODO #5 Find out if there is any possibility to change CHATGPT into other AI:
# Check other library than ChatGPT or find sugar mommy that will pay for it
# TODO #6 Find out how to make bot working 24/7


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("Error occurred")
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send("You dont have all the requirements")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("Member not found")


def run_discord_bot():
    client = commands.Bot(command_prefix=">", intents=intents, help_command=None)

    @client.group()
    async def help(ctx):
        em = discord.Embed(title=f"Hey, **{ctx.message.author.name}**, I am Joi",
                           description="```A Discord Music Bot With Many "
                                       "Awesome Features, Buttons, Menus, "
                                       "Context Menu, Support Many Sources, "
                                       "Customizable Settings\n\nOver 5 Commands```",
                           color=ctx.author.color)
        em.add_field(name="**Moderation**", value="`>kick`\n"
                                                  "`>ban`\n"
                                                  "`>warn` SOON\n"
                                                  "`>remind`")
        em.add_field(name="**Fun**", value="`Music YT, Spotify` SOON\n")
        await ctx.reply(embed=em)

    @client.command(name="kick", pass_context=True)
    @commands.has_permissions(manage_roles=True, kick_members=True)
    async def kick(ctx, user: discord.Member):
        if str(user) == "ŹმĹმ#0279" or str(user) == "eposito#0":
            em = discord.Embed(title="**Kick**", description=f"{user} is my creator, I can't harm him",
                               color=ctx.author.color)
            await ctx.send(embed=em)
        else:
            command = ctx.message.content.lower()
            msg = command.split(">kick")[1].strip()
            r = msg.split(" for ")
            em = discord.Embed(title="**Kick**", description=f"{user} has been kicked from the server for {r[1]}",
                               color=ctx.author.color)
            await ctx.send(embed=em)
            if commands.has_permissions(administrator=True):
                await user.send(f"You've been kicked from the server for {r[1]}")
                await user.kick(reason=None)
            else:
                await ctx.send("You don't have permission")

    @client.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, user: discord.Member, *, reason=None):
        if str(user) == "ŹმĹმ#0279" or str(user) == "eposito#0":
            em = discord.Embed(title="**Kick**", description=f"{user} is my creator, I can't harm him",
                               color=ctx.author.color)
            await ctx.send(embed=em)
        else:
            command = ctx.message.content.lower()
            msg = command.split(">ban")[1].strip()
            r = msg.split(" for ")
            em = discord.Embed(title="**Ban**", description=f"Replicant {user} has been purged", color=ctx.author.color)
            await user.send(f"You've been banned for {r[1]}")
            await user.ban(reason=reason)
            await ctx.reply(embed=em)

    @client.command()
    @commands.has_permissions(warn_members=True)
    async def warn(ctx, *, user: discord.Member):
        if user == "help":
            em = discord.Embed(title="**Warn**", description="SOON", color=ctx.author.color)
            em.add_field(name="**SYNTAX**", value="```>help warn <member> for [reason]```")
            await ctx.reply(embed=em)
        else:
            if str(user) == "ŹმĹმ#0279" or str(user) == "eposito#0":
                em = discord.Embed(title="**Kick**", description=f"{user} is my creator, I can't harm him",
                                   color=ctx.author.color)
                await ctx.send(embed=em)
            else:
                print("Bug")
                # await user.timeout(datetime.utcnow(), reason=None)
                # await user.send(f"You've been warned for violating the rules")

    @client.command()
    async def remind(ctx):
        if ctx.message.content == ">remind help":
            em = discord.Embed(color=ctx.author.color)
            em.add_field(name="**SYNTAX**",
                         value="```>remind [What did you want to be reminded of] at [Hour:Minute]```")
            await ctx.reply(embed=em)
        else:
            comm = ctx.message.content.lower()
            msg = comm.split(">remind")[1].strip()
            input_time = msg.split(" at ")
            target_time = datetime.strptime(input_time[1], '%H:%M').time()
            current_time = datetime.now().time()

            while current_time < target_time:
                await asyncio.sleep(30)
                current_time = datetime.now().time()

            em = discord.Embed(color=ctx.author.color)
            em.add_field(name="**Reminder**",
                         value=f"{ctx.message.author.mention} You wanted me to remind you about: {input_time[0]}")
            await ctx.reply(embed=em)

    @client.command()
    async def play(ctx):

        if ctx.voice_client:
            em = discord.Embed()
            em.add_field(name="JOI Music", value="```I'm on vc```")
            await ctx.reply(embed=em)
        else:
            url = ctx.message.content
            ydl_opts = {'format': 'bestaudio'}
            vid_link = url.split(">play ")[1]
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(vid_link, download=False)
                URL = info['formats'][0]['url']
            voice = await ctx.author.voice.channel.connect()
            voice.play(discord.FFmpegPCMAudio(URL))

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

    client.run(config["TOKEN"])


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
