import discord
from discord.ext.commands import command, has_permissions, bot_has_permissions
from discord.ext.commands import Cog
import asyncio


class Mod(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print('Ready !')

    @command(name="help")
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

    @command(name="kick")
    @bot_has_permissions(kick_members=True)
    @has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):  # TODO NEED A TEST
        if str(user) == "ŹმĹმ#0279" or str(user) == "eposito#0":
            em = discord.Embed(title="**Kick**", description=f"{user} is my creator, I can't harm him",
                               color=ctx.author.color)
            await ctx.send(embed=em)
        else:
            comm = ctx.message.content.lower()
            msg = comm.split(">kick")[1].strip()
            r = msg.split(" for ")
            em = discord.Embed(title="**Kick**", description=f"{user} has been kicked from the server for {r[1]}",
                               color=ctx.author.color)
            await user.kick(reason=reason)
            await user.send(f"You've been kicked from the server for {r[1]}")
            await ctx.reply(embed=em)

    @command(name="ban")
    @bot_has_permissions(ban_members=True)
    @has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):  # TODO NEED A TEST
        if str(user) == "ŹმĹმ#0279" or str(user) == "eposito#0":
            em = discord.Embed(title="**Kick**", description=f"{user} is my creator, I can't harm him",
                               color=ctx.author.color)
            await ctx.send(embed=em)
        else:
            comm = ctx.message.content.lower()
            msg = comm.split(">ban")[1].strip()
            r = msg.split(" for ")
            em = discord.Embed(title="**Ban**", description=f"Replicant {user} has been purged",
                               color=ctx.author.color)
            await user.ban(reason=reason)
            await user.send(f"You've been banned for {r[1]}")
            await ctx.reply(embed=em)

    @command(name="warn")
    @bot_has_permissions(mute_members=True)
    @has_permissions(mute_members=True)
    async def warn(self, ctx, *, user: discord.Member, mute_time: int):  # TODO NEED A TEST
        if user == "help":
            em = discord.Embed(title="**Warn**", description="SOON", color=ctx.author.color)
            em.add_field(name="**SYNTAX**", value="```>help warn <member> for [reason]```")
            await ctx.reply(embed=em)
        else:
            if str(user) == "ŹმĹმ#0279" or str(user) == "eposito#0":
                em = discord.Embed(title="**Kick**", description=f"{user.mention} is my creator, I can't harm him",
                                   color=ctx.author.color)
                await ctx.send(embed=em)
            else:
                guild = ctx.guild
                for role in guild.roles:
                    if role.name == "Muted":
                        await user.add_roles(role)
                        await ctx.send(f"{user.mention} has has been muted!")
                        await asyncio.sleep(mute_time)
                        await user.remove_roles(role)
                        await ctx.send(f"{user.mention} has been unmuted!")

    @command()
    @has_permissions(kick_members=True)
    async def unmute(self, ctx, user: discord.Member):
        guild = ctx.guild
        for role in guild.roles:
            if role.name == "Muted":
                await user.remove_roles(role)
                await ctx.send(f"{user.mention} has has been unmuted!")

    # @Cog.listener()
    # async def on_command_error(self, ctx, error):
    #     if isinstance(error, discord.ext.commands.MissingRequiredArgument):
    #         await ctx.reply('Please pass in all requirements :rolling_eyes:.')
    #     elif isinstance(error, discord.ext.commands.CommandInvokeError):
    #         await ctx.reply("Error occurred")
    #     elif isinstance(error, discord.errors.Forbidden):
    #         await ctx.reply("You don't have all the requirements")
    #     elif isinstance(error, discord.ext.commands.MemberNotFound):
    #         await ctx.reply("Member not found")
    #     elif isinstance(error, KeyboardInterrupt):
    #         print("The bot has been manually deactivated")
    #     elif isinstance(error, discord.ext.commands.MissingPermissions):
    #         if ctx.command.name in ['kick', 'ban', 'warn']:
    #             await ctx.reply("You don't have the required permissions to run this command.")
    #         else:
    #             await ctx.reply("You don't have all the requirements :angry:")


async def setup(bot):
    await bot.add_cog(Mod(bot))
