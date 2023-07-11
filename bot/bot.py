import os
import discord
from discord.ext import commands
from dotenv import dotenv_values


intents = discord.Intents().all()
config = dotenv_values("data.env")
bot = commands.Bot(command_prefix=">", intents=intents, help_command=None)


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    await load()
    await bot.start(config["TOKEN"])
