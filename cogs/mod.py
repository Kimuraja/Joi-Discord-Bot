import discord
from discord.ext.commands import command, has_permissions, bot_has_permissions
from discord.ext.commands import Cog
from datetime import timedelta


class Mod(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print(f'Ready -> Logged in as {self.bot.user}')

    @command(name="help")
    async def help(self, ctx):
        em = discord.Embed(title="Discord Bot", description="Let me briefly introduce you to some of the key commands:",
                           color=15277667)

        em.add_field(name="**>kick [user] [reason]** ", value="Kick troublesome users from the server to maintain "
                                                              "harmony and peace.")
        em.add_field(name="**>ban [user] [reason]**", value="When all else fails, this command can help you "
                                                            "permanently remove problematic users.")
        em.add_field(name="**>unban [user] [reason]**", value="Sometimes, second chances are deserved. Use this "
                                                              "command to lift bans and allow users back in.")
        em.add_field(name="**>warn [user] [reason]**", value="Politely caution misbehaving members with a warning "
                                                             "message. Mention the user who needs a warning and "
                                                             "include a reason.")
        em.add_field(name="**>unwarn [user] [reason]**", value="If someone has learned their lesson, you can remove "
                                                               "a warning with this command. Mention the user to "
                                                               "un-warn them.")
        em.add_field(name="**>help**", value="Need assistance? This command will guide you through the bot's "
                                             "functionalities.")
        # em.add_field(name="**>gpt**", value="Unlock the power of AI-generated text with the GPT feature.")
        # em.add_field(name="**>play**", value="Start grooving by having the bot play some awesome tunes in voice "
        #                                      "channels.")
        em.add_field(name="**>ask [question]**", value="ask [question] Need answers? Ask the bot anything, and it "
                                                       "will respond in a mysterious and magical manner. Just pose "
                                                       "your question, and the bot will use its mystical powers to "
                                                       "give you an answer.")
        await ctx.reply(embed=em)

    @command(name="kick")
    @bot_has_permissions(kick_members=True)
    @has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, reason):
        if user.id == "317374704027566091" or str(user) == "eposito#0":
            em = discord.Embed(title="**Kick**", description=f"{user.mention} is my creator, I can't harm him",
                               color=15277667)
            await ctx.send(embed=em)
        else:
            em = discord.Embed(title="**Kick**",
                               description=f"{user.mention} has been kicked from the server for {reason}",
                               color=15277667)
            await ctx.reply(embed=em)
            await user.kick(reason=reason)
            await user.send(f"You've been kicked from the server for {reason}")

    @command(name="ban")
    @bot_has_permissions(ban_members=True)
    @has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, reason):
        if user.id == "317374704027566091" or str(user) == "eposito#0":
            em = discord.Embed(title="**Kick**", description=f"{user} is my creator, I can't harm him", color=15277667)
            await ctx.send(embed=em)
        else:
            em = discord.Embed(title="**Ban**", description=f"Replicant {user} has been purged", color=15277667)
            await ctx.reply(embed=em)
            await user.ban(reason=reason)
            await user.send(f"You've been banned for {reason}")

    @command(name="warn")
    @bot_has_permissions(kick_members=True)
    @has_permissions(kick_members=True)
    async def warn(self, ctx, user: discord.Member, reason):
        if user.id == "317374704027566091" or str(user) == "eposito#0":
            em = discord.Embed(title="**Kick**", description=f"{user.mention} is my creator, I can't harm him",
                               color=15277667)
            await ctx.send(embed=em)
        else:
            await user.timeout(timedelta(minutes=15))
            await ctx.send(f"{user.mention} has been muted because {reason}", color=15277667)
            await user.send(f"You've been muted for {reason}")

    @command(name="unwarn")
    @bot_has_permissions(kick_members=True)
    @has_permissions(kick_members=True)
    async def unwarn(self, ctx, user: discord.Member):
        await user.timeout(timedelta(minutes=0))
        await ctx.send(f"{user.mention} has been unmuted", color=15277667)


async def setup(bot):
    await bot.add_cog(Mod(bot))
