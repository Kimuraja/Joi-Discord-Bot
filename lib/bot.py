import asyncio
import discord
from datetime import datetime
from youtube_dl import YoutubeDL
from discord.ext import commands
from dotenv import dotenv_values
from discord.ext.commands import Bot as BotBase
from glob import glob


COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]
intents = discord.Intents().all()
config = dotenv_values("data.env")
bot = commands.Bot(command_prefix=">", intents=intents, help_command=None)


# TODO #1 Make bot play music from spotify/youtube:
# Read the documentation
# Play music

# TODO #3 Check if there is any possibility to play music from youtube one a bot:
# Check other library than youtube_dl

# TODO #5 Find out if there is any possibility to change CHATGPT into other AI:
# Check other library than ChatGPT or find sugar mommy that will pay for it

# TODO #6 Find out how to make bot working 24/7

# TODO Additional functions that can be added to bot:
# Automated Announcements
# Customizations and settings
# Polls and voting
# Role Management

class Client(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    @bot.command()
    async def help(self, ctx):
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

    @commands.Cog.listener()
    @bot.command()
    async def remind(self, ctx):
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
            await ctx.send(embed=em)

    @bot.command()
    @commands.Cog.listener()
    # Additional command access to use this command
    async def play(self, ctx):
        if not ctx.author.voice.channel:
            await ctx.send("You're not on a voice channel")
        else:
            URL = ctx.message.content
            vid_link = URL.split(">play ")[1]
            with YoutubeDL(YDL_OPTIONS) as ydl:
                voice = await ctx.author.voice.channel.connect()
                # ERROR: Unable to extract uploader id; please report this issue on https://yt-dl.org/bug . Make sure
                # you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call
                # youtube-dl with the --verbose flag and include its complete output.
                info = ydl.extract_info(vid_link, download=False)
                audio_url = info['formats'][0]['url']
                voice.play(discord.FFmpegPCMAudio(audio_url))

            return {'source': audio_url, 'title': info['title']}

    @bot.command(pass_context=True)
    # Additional command access to use this command
    async def leave(self, ctx):
        if ctx.voice_client:
            em = discord.Embed()
            em.add_field(name="JOI Music", value="```Goodbye```")
            await ctx.guild.voice_client.disconnect()
            await ctx.reply(embed=em)
        else:
            em = discord.Embed()
            em.add_field(name="JOI Music", value="```An Error occurred, I am not in a vc```")
            await ctx.reply(embed=em)

    @bot.command(pass_context=True)
    async def voting(self, ctx):
        # TODO Vote -> To be continued...
        if ctx.message.content == ">vote help":
            em = discord.Embed(color=ctx.message.author)
            em.add_field(name="**Vote system**", value="```vote syntax```")
            await ctx.reply(embed=em)
        else:
            pass

    @bot.event
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Please pass in all requirements :rolling_eyes:.')
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.reply("Error occurred")
        elif isinstance(error, discord.errors.Forbidden):
            await ctx.reply("You dont have all the requirements")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.reply("Member not found")
        elif isinstance(error, commands.MissingPermissions):
            if ctx.command.name in ['kick', 'ban', 'warn']:
                await ctx.reply("You don't have the required permissions to run this command.")
            else:
                await ctx.reply("You dont have all the requirements :angry:")


class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f" {cog} cog ready")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])


class Bot(BotBase):
    def __int__(self):
        self.ready = False
        self.cogs_ready = Ready()

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog} cog loaded")
        print("Setup complete")

    def run(self):
        self.setup()

        print("running setup...")
        self.setup()

        # with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
        #     self.TOKEN = tf.read()

        # super().run(self.TOKEN, reconnect=True)


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
