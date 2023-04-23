import discord
import responses

intents = discord.Intents.default()
intents.typing = True
async def send_message(message, user_msg, is_private):
    try:
        response = responses.handle_response(user_msg)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "MTA5OTY4MTMzMDI0NzIzNzY2Mg.G-Qv-y.smOXqBGx86wXtGInaRFR2Fsn0EEuZXI0FZjtIM"
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    client.run(TOKEN)
