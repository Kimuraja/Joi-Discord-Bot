import discord
from discord.ext.commands import command, has_permissions, bot_has_permissions
from discord.ext.commands import Cog
import logging
from discord_logging.handler import DiscordHandler


# class Log(Cog):
#     webhook_url = "https://discord.com/api/webhooks/1127462640592113684/BnwsQpzUKBY-PUh0IiivMGyKh3HarQqZn47tJBFRFJ_DCWWXUxvC1Npm7XQEa67TlKw0"
#     logger = logging.getLogger()
#
#     stream_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#     discord_format = logging.Formatter("%(message)s")
#
#     discord_handler = DiscordHandler(
#         "Hello World Bot",
#         webhook_url=webhook_url,
#     )
#
#     discord_handler.setFormatter(discord_format)
#     stream_handler = logging.StreamHandler()
#     stream_handler.setFormatter(stream_format)
#
#     logger.addHandler(discord_handler)
#     logger.addHandler(stream_handler)
#     logger.setLevel(logging.DEBUG)
#
#     logger.info("This is an info message")
#     logger.debug("A debug message - Usually no that intresting")
#     logger.error("Error")
#
#
# async def setup(bot):
#     await bot.add_cog(Log(bot))
