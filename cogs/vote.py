import discord
from discord.ext.commands import Cog, command
from datetime import datetime
import asyncio
from discord.utils import get

EMOJIS = ["✅", "❌", ":grey_question:"]


class Vote(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.input_time = 0
        self.params = ""
        self.dt = datetime

    @Cog.listener()
    async def on_ready(self):
        print("Voting poll => ready")

    async def on_message(self, ctx):
        self.params = ctx.message.content

        inp_role = self.params.split(",")[0].replace(">poll", "").strip()
        clear_role = inp_role.replace("<@&", "").replace(">", "")
        role = get(ctx.guild.roles, id=int(clear_role))

        self.input_time = self.dt.strptime(self.params.split(" at ")[1], '%H:%M').time()
        current_time = self.dt.now().time()
        description = (self.params.split(" at ")[0].replace(">poll", "").strip())
        options = description.split(",")[1].strip()

        await ctx.message.delete()
        em = discord.Embed(title=f"{role}", description=f"{options}",
                           color=15277667)
        em.add_field(name=f"{EMOJIS[0]} Accepted", value="-")
        em.add_field(name=f"{EMOJIS[1]} Declined", value="-")
        em.add_field(name=f"{EMOJIS[2]} Tentative", value="-")
        em.set_footer(text=f"Created by {ctx.message.author.name}")
        sent = await ctx.send(embed=em)

        # --- new def --- #

        while current_time < self.input_time:
            await asyncio.sleep(0.1)
            current_time = datetime.now().time()
            if current_time > self.input_time:
                await sent.delete()
                finished_poll = discord.Embed(title=f"**{role}**", description="", color=15277667)
                await ctx.send(finished_poll)

        for index, string in enumerate(EMOJIS):
            await sent.add_reaction(EMOJIS[index])

    @command(name="poll")
    async def poll(self, ctx):
        await self.on_message(ctx)


async def setup(bot):
    await bot.add_cog(Vote(bot))
