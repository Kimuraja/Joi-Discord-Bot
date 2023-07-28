import discord
from discord.ext.commands import Cog, command


class Vote(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("Voting poll => ready")

    async def on_message(self, ctx):
        if ctx.message.content.startswith(">poll"):
            msg = ctx.message.content.split(">poll")
            params = ctx.message.content.split(",")
            name = params[0].replace(">poll", "").strip()
            question = msg[1].strip().split(",")
            options = [x.strip() for x in params[1:]]
            countdown = params[3]
            em = discord.Embed(title=f"**Poll: **{name}", description=f"**{question[1]}\n {options[1:]}**",
                               color=15277667)
            sent = await ctx.message.channel.send(embed=em)

            EMOJIS = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]

            for index, string in enumerate(EMOJIS):
                await sent.add_reaction(EMOJIS[index])

    @command(name="poll")
    async def poll(self, ctx):
        await self.on_message(ctx)


async def setup(bot):
    await bot.add_cog(Vote(Cog))
