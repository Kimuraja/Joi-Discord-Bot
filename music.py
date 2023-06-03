# import discord
# import wavelink
# from discord.ext import commands
#
#
# class Bot(commands.Bot):
#
#     def __init__(self) -> None:
#         intents = discord.Intents.default()
#         intents.message_content = True
#
#         super().__init__(intents=intents, command_prefix='?')
#
#     async def on_ready(self) -> None:
#         print(f'Logged in {self.user} | {self.user.id}')
#
#     async def setup_hook(self) -> None:
#         # Wavelink 2.0 has made connecting Nodes easier... Simply create each Node
#         # and pass it to NodePool.connect with the client/bot.
#         node: wavelink.Node = wavelink.Node(uri='http://localhost:2333', password='youshallnotpass')
#         await wavelink.NodePool.connect(client=self, nodes=[node])
#
#
# bot = Bot()
#
#
# @bot.command()
# async def play(ctx: commands.Context, *, search: str) -> None:
#     """Simple play command."""
#
#     if not ctx.voice_client:
#         vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
#     else:
#         vc: wavelink.Player = ctx.voice_client
#
#     track = await wavelink.YouTubeTrack.search(search, return_first=True)
#     await vc.play(track)
#
#
# @bot.command()
# async def disconnect(ctx: commands.Context) -> None:
#     """Simple disconnect command.
#
#     This command assumes there is a currently connected Player.
#     """
#     vc: wavelink.Player = ctx.voice_client
#     await vc.disconnect()
