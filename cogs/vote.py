import discord
from discord.ext.commands import Cog, command
from datetime import datetime
import asyncio
from discord.utils import get

EMOJIS = ["✅", "❌", "☁️"]


class Vote(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.params = ""
        self.dt = datetime
        self.role = ""
        self.sent = None
        self.user = discord.Member
        self.input_time = None

    async def get_role(self, ctx):
        self.params = ctx.message.content
        inp_role = self.params.split(",")[0].replace(">poll", "").strip()
        clear_role = inp_role.replace("<@&", "").replace(">", "")
        self.role = get(ctx.guild.roles, id=int(clear_role))
        return self.role

    async def inp_time(self):
        self.input_time = self.dt.strptime(self.params.split(" at ")[1], '%H:%M').time()
        return self.input_time

    async def embed_msg(self, ctx):
        description = (self.params.split(" at ")[0].replace(">poll", "").strip())
        options = description.split(",")[1].strip()
        em = discord.Embed(title=f"{self.role}", description=f"{options}",
                           color=15277667)
        em.add_field(name=f"{EMOJIS[0]} Accepted", value="-")
        em.add_field(name=f"{EMOJIS[1]} Declined", value="-")
        em.add_field(name=f"{EMOJIS[2]} Tentative", value="-")
        em.set_footer(text=f"Voting ends at {self.input_time}")
        self.sent = await ctx.send(embed=em)
        return self.sent

    # TODO Role interaction with user
        # if user chose one option then others will be disabled
        # At the end of the voting, the bot will send the results to the channel

    async def time_countdown(self, ctx):
        while self.input_time:
            await asyncio.sleep(0.1)
            current_time = datetime.now().time()
            if current_time > self.input_time:
                await self.sent.delete()
                em = discord.Embed(title=f"**{self.role}**", description="", color=15277667)
                em.add_field(name=f"{EMOJIS[0]} Accepted", value="-")
                em.add_field(name=f"{EMOJIS[1]} Declined", value="-")
                em.add_field(name=f"{EMOJIS[2]} Tentative", value="-")
                em.add_field(name=f"**Results**", value="-")
                em.set_footer(text=f"Voting has ended")
                await ctx.send(embed=em)

            for index, string in enumerate(EMOJIS):
                await self.sent.add_reaction(string)

    @command(name="poll")
    async def poll(self, ctx):
        await self.get_role(ctx)
        await self.inp_time()
        await self.embed_msg(ctx)
        await self.time_countdown(ctx)


async def setup(bot):
    await bot.add_cog(Vote(bot))
