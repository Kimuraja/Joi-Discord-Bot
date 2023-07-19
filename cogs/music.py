from discord.ext.commands import Cog, command
from dotenv import dotenv_values
# import spotify
import discord

config = dotenv_values("data.env")


class Music(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = {}
        self.player = None
        self.id = config["CLIENT_ID"]
        self.secret = config["CLIENT_SECRET"]
        self.audio = None
        self.queue = []
        self.is_playing = False
        self.clear = None
        self.URL = None
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                               'options': '-vn'}

    @Cog.listener()
    async def on_ready(self):
        print("Music -> Ready")
        for guild in self.bot.guilds:
            ID = int(guild.id)
            self.vc[ID] = None

    async def join_vc(self, ctx):
        channel = ctx.author.voice.channel
        ID = int(ctx.guild.id)
        if self.vc[ID] is None or not self.vc[ID].is_connected():
            self.vc[ID] = await channel.connect()
        else:
            await self.vc[ID].move_to(channel)

    async def search(self, ctx):
        discord.opus.load_opus("opus")
        if self.is_playing and self.clear is not None:
            await self.add_queue()
        else:
            comm = ctx.message.content
            url = comm.split(" ")[1]
            self.URL = url
            self.audio = url.split("/")[-1].split("?")[0]

    async def add_queue(self):
        pass

    async def is_playing(self):
        pass

    async def clear(self):
        pass

    @command(
        name="leave",
        pass_context=True
    )
    async def leave(self, ctx):
        await ctx.guild.voice_client.disconnect()

    @command(
        name="play",
        pass_conetxt=True
    )
    async def play(self, ctx):
        ID = int(ctx.guild.id)
        await self.join_vc(ctx)
        await self.search(ctx)
        self.is_playing = True
        self.vc[ID].play(discord.FFmpegPCMAudio(self.URL, **self.FFMPEG_OPTIONS))


async def setup(bot):
    await bot.add_cog(Music(bot))
