import discord
import os
import asyncio
import youtube_dl
from bot import client, intents

voice_client = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}

@client.event
async def on_msg(msg):
    if msg.content.startwith(">play"):
        try:
            url = msg.content.split()[1]

            voice_client = await msg.author.voice.channel.connect()
            voice_client[voice_client.id] = voice_client

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

            voice_client.play(player)
        except Exception as err:
            print(err)