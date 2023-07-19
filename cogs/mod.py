import discord
from discord.ext.commands import command, has_permissions, bot_has_permissions
from discord.ext.commands import Cog
from datetime import timedelta


class Mod(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print('Moderation -> Ready !')

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
    async def kick(self, ctx, user: discord.Member, reason):
        if user.id == "317374704027566091" or str(user) == "eposito#0":
            em = discord.Embed(title="**Kick**", description=f"{user} is my creator, I can't harm him",
                               color=ctx.author.color)
            em.set_image(url=None)
            em.set_footer(text="Text here")
            await ctx.send(embed=em)
        else:
            em = discord.Embed(title="**Kick**", description=f"{user} has been kicked from the server for {reason}",
                               color=ctx.author.color)
            await ctx.reply(embed=em)
            await user.send(f"You've been kicked from the server for {reason}")
            await user.kick(reason=reason)

    @command(name="ban")
    @bot_has_permissions(ban_members=True)
    @has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, reason):
        if user.id == "317374704027566091" or str(user) == "eposito#0":
            em = discord.Embed(title="**Kick**", description=f"{user} is my creator, I can't harm him",
                               color=ctx.author.color)
            await ctx.send(embed=em)
        else:
            em = discord.Embed(title="**Ban**", description=f"Replicant {user} has been purged",
                               color=ctx.author.color)
            await ctx.reply(embed=em)
            await user.send(f"You've been banned for {reason}")
            await user.ban(reason=reason)

    @command(name="warn")
    async def warn(self, ctx, user: discord.Member, reason):
        if user.id == "317374704027566091" or str(user) == "eposito#0":
            em = discord.Embed(title="**Kick**", description=f"{user.mention} is my creator, I can't harm him",
                               color=ctx.author.color)
            await ctx.send(embed=em)
        else:
            print("Work")
            await user.timeout(timedelta(minutes=15))
            await ctx.send(f"{user.mention} has been muted because {reason}")

    @command()
    async def unwarn(self, ctx, user: discord.Member):
        await user.timeout(timedelta(minutes=0))
        await ctx.send(f"{user.mention} has been unmuted")

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
