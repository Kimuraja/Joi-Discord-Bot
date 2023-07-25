import discord
from discord.ext.commands import command
from discord.ext.commands import Cog
from datetime import datetime
import asyncio


class Remind(Cog):
    def __init__(self, bot):
        self.dt = datetime
        self.bot = bot

    @command()
    async def remind(self, ctx):
        if ctx.message.content == ">remind help":
            em = discord.Embed(color=ctx.author.color)
            em.add_field(name="**SYNTAX**",
                         value="```>remind [What did you want to be reminded of] at [Hour:Minute]```")
            await ctx.reply(embed=em)
        else:
            comm = ctx.message.content.lower()
            msg = comm.split(">remind")[1].strip()
            input_time = msg.split(" at ")
            target_time = self.dt.strptime(input_time[1], '%H:%M').time()
            current_time = self.dt.now().time()

            while current_time < target_time:
                await asyncio.sleep(10)
                current_time = datetime.now().time()

            em = discord.Embed(color=ctx.author.color)
            em.add_field(name="**Reminder**",
                         value=f"{ctx.message.author.mention} You wanted me to remind you about: {input_time[0]}")
            await ctx.send(embed=em)


async def setup(bot):
    await bot.add_cog(Remind(bot))
