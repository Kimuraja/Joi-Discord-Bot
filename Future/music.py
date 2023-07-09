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