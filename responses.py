# from random import randint
# import discord
# from discord.ext import commands
#
# intents = discord.Intents.default()
# intents.typing = True
# intents.message_content = True
#
#
# def message():
#     client = commands.Bot(command_prefix=">", intents=intents)
#     client.remove_command("help")
#
#     @client.group(invoke_without_command=True)
#     async def help(ctx):
#         em = discord.Embed(title="Help", description="Use >help <command>", color=ctx.author.color)
#         em.add_field(name="Moderation", value="kick,ban,warn")
#         em.add_field(name="Fun", value="8ball,reverse")
#         await ctx.send(embed=em)
#
#     @help.command()
#     async def kick(ctx):
#         em = discord.Embed(title="Ping", description="Kick a member", color=ctx.author.color)
#         em.add_field(name="**SYNTAX**", value=">kick <member> [reason]")
#         await ctx.send(embed=em)
#
#     @help.command()
#     async def ban(ctx):
#         em = discord.Embed(title="Ban", description="Ban a member", color=ctx.author.color)
#         em.add_field(name="**SYNTAX**", value=">ban <member> [reason]")
#         await ctx.send(embed=em)
#
#     client.run(TOKEN)
