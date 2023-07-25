from discord.ext.commands import Cog, command
import json
import random
import discord


class Ball(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="ask")
    async def ask(self, ctx):
        with open('./json/8ball.json') as f:
            data = json.load(f)
            answer = str(random.choice(data['answers']))
            em = discord.Embed(title="**Bot Answer**", description=f"{answer}", color=15277667)
            await ctx.send(embed=em)


async def setup(bot):
    await bot.add_cog(Ball(bot))
