import discord
from discord.ext.commands import Cog


class Welcome(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_list = []

    @Cog.listener()
    async def on_ready(self):
        print('Welcome => Ready!')

    async def discord_embeds(self, message):
        em1 = discord.Embed(title="What's this about?", description="This Discord server is home to a wonderful "
                                                                    "community gathered around a fascinating bot, "
                                                                    "designed to make your Discord experience even "
                                                                    "more enjoyable! Our custom bot comes equipped "
                                                                    "with a variety of useful commands to enhance "
                                                                    "your server interactions and streamline your "
                                                                    "activities.", color=15277667)

        em2 = discord.Embed(title="Discord Bot", description="Our bot is here to lend a helping hand and add some "
                                                             "fun to your server. It's a friendly and versatile "
                                                             "companion capable of performing various tasks with "
                                                             "just a few commands. Let me briefly introduce you "
                                                             "to some of the key commands:", color=15277667)

        em2.add_field(name="**>kick [user] [reason]** ", value="Kick troublesome users from the server to maintain "
                                                               "harmony and peace.")
        em2.add_field(name="**>ban [user] [reason]**", value="When all else fails, this command can help you "
                                                             "permanently remove problematic users.")
        em2.add_field(name="**>unban [user] [reason]**", value="Sometimes, second chances are deserved. Use this "
                                                               "command to lift bans and allow users back in.")
        em2.add_field(name="**>warn [user] [reason]**", value="Politely caution misbehaving members with a warning "
                                                              "message. Mention the user who needs a warning and "
                                                              "include a reason.")
        em2.add_field(name="**>unwarn [user] [reason]**", value="If someone has learned their lesson, you can remove "
                                                                "a warning with this command. Mention the user to "
                                                                "un-warn them.")
        em2.add_field(name="**>help**", value="Need assistance? This command will guide you through the bot's "
                                              "functionalities.")
        em2.add_field(name="**>gpt**", value="Unlock the power of AI-generated text with the GPT feature.")
        em2.add_field(name="**>play**", value="Start grooving by having the bot play some awesome tunes in voice "
                                              "channels.")
        em3 = discord.Embed(title="", description="We hope you have an amazing time in our server with our bot's "
                                                  "assistance. If you ever have any questions or need support, our "
                                                  "friendly community is here to help. Enjoy your stay! 🎉", color=15277667)

        self.embed_list = [em1, em2, em3]
        await message.channel.send(f"Hey {message.author.mention} 👋, welcome to **{message.guild.name}**!\n\n "
                                   f"There's more info below, or if you have more specific questions, "
                                   f"feel free to ask.\n\n", embeds=self.embed_list,)

    @Cog.listener()
    async def on_message(self, message):
        if message.type == discord.MessageType.new_member:
            await self.discord_embeds(message)


async def setup(bot):
    await bot.add_cog(Welcome(bot))
