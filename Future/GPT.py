from discord.ext.commands import Cog, command
from dotenv import dotenv_values
import openai

config = dotenv_values("data.env")
openai.api_key = config["ACCESS_TOKEN"]


class GPT(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="gpt")
    async def gpt(self, ctx):
        msg = ctx.message.content.split(">gpt ")
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=msg[1],
                max_tokens=100
            )
            print(response)
            await ctx.send(response['choices'][0]['text'])
        except Exception as e:
            print("An error occurred:", e)
            await ctx.send("Please check your plan and billing details")


async def setup(bot):
    await bot.add_cog(GPT(bot))
