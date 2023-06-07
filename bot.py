import discord
from dotenv import dotenv_values
from discord.ext import commands

intents = discord.Intents().all()
config = dotenv_values(".env")
client = commands.Bot(command_prefix=">", intents=intents, help_command=None)

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

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")


def run_discord_bot():
    client = commands.Bot(command_prefix=">", intents=intents, help_command=None)

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
    async def kick(ctx, user: discord.Member, *, reason=None):
        if str(user) == "ŹმĹმ#0279":
            em = discord.Embed(title="**Kick**", description=f"{user} is my creator, I can't harm him",
                               color=ctx.author.color)
            await ctx.send(embed=em)
        else:
            em = discord.Embed(title="**Kick**", description=f"{user} has been kicked from the server",
                               color=ctx.author.color)
            await ctx.send(embed=em)
            await user.kick(reason=reason)

    @client.command() #TODO NEED A TEST
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, user: discord.Member, *, reason=None):
        if str(user) == "ŹმĹმ#0279":
            em = discord.Embed(title="**Kick**", description=f"{user} is my creator, I can't harm him",
                               color=ctx.author.color)
            await ctx.send(embed=em)
        else:
            em = discord.Embed(title="**Ban**", description=f"Replicant {user} has been purged", color=ctx.author.color)
            await user.ban(reason=reason)
            await ctx.reply(embed=em)

    @client.command() #TODO NEED A TEST
    @commands.has_permissions(administrator=True)
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
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
