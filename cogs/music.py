# import discord
# import asyncio
# from datetime import datetime
from discord.ext.commands import Cog, command
from youtube_dl import YoutubeDL


class Music(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = {}
        self.YTDL_OPTIONS = {'format': 'bestaudio', 'nonplaylist': 'True'}
        self.FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }

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

    # async def search_yt(self, ctx):
    #     with YoutubeDL(self.YTDL_OPTIONS) as ydl
    #         ydl.

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
        await self.join_vc(ctx)


async def setup(bot):
    await bot.add_cog(Music(bot))