import discord
from discord.ext.commands import Cog, command
import asyncio

EMOJIS = ["✅", "❌", ":grey_question:"]


class Vote(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.time = 0
        self.params = ""

    @Cog.listener()
    async def on_ready(self):
        print("Voting poll => ready")

    async def on_message(self, ctx):
        if ctx.message.content.startswith(">poll"):
            self.params = ctx.message.content
            name = self.params.split(",")[0].replace(">poll", "").strip()
            self.time = float(self.params.split(",")[1].strip()) * 60
            options = self.params.split(",")[2].strip()

            em = discord.Embed(title=f"**{name}**", description=f"{options}",
                               color=15277667)
            em.add_field(name=f"{EMOJIS[0]} Accepted", value="-")
            em.add_field(name=f"{EMOJIS[1]} Declined", value="-")
            em.add_field(name=f"{EMOJIS[2]} Tentative", value="-")
            em.set_footer(text=f"Created by {ctx.message.author.name}")
            sent = await ctx.send(embed=em)

            for index, string in enumerate(EMOJIS):
                await sent.add_reaction(EMOJIS[index])
                print(type(self.time))
                print(self.params)

        while self.time:
            await asyncio.sleep(1)
            self.time -= 1
            if self.time == 0:
                print("Done")
                return False
                # await sent.delete()
                # finished_poll = discord.Embed(title=f"**{name}**", description="", color=15277667)
                # await ctx.send(finished_poll)

    @command(name="poll")
    async def poll(self, ctx):
        await self.on_message(ctx)


async def setup(bot):
    await bot.add_cog(Vote(Cog))
