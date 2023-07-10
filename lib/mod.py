import discord
from discord.ext import commands
from discord.ext.commands import Cog
from lib.bot import bot


class Mod(Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(name="kick", pass_context=True)
    @commands.has_permissions(manage_roles=True, kick_members=True)
    async def kick(self, ctx, user: discord.Member, error):
        try:
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
        finally:
            if isinstance(error, commands.errors.MissingPermissions):
                await ctx.send('MissingPermissions...')

    @commands.command(name="ban", pass_context=True)
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        if str(user) == "ŹმĹმ#0279" or str(user) == "eposito#0":
            em = discord.Embed(title="**Kick**", description=f"{user} is my creator, I can't harm him",
                               color=ctx.author.color)
            await ctx.send(embed=em)
        else:
            command = ctx.content.lower()
            msg = command.split(">ban")[1].strip()
            r = msg.split(" for ")
            em = discord.Embed(title="**Ban**", description=f"Replicant {user} has been purged",
                               color=ctx.author.color)
            await user.send(f"You've been banned for {r[1]}")
            await user.ban(reason=reason)
            await ctx.reply(embed=em)

    @commands.command(name="warn")
    @commands.has_permissions(mute_members=True)
    async def warn(self, ctx, *, user: discord.Member):
        try:
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
        except discord.ext.commands.MissingPermissions as err:
            em = discord.Embed(title="**Error**", description=f"{err}")
            await ctx.reply(embed=em)


def setup():
    bot.add_cog(Mod(bot))
