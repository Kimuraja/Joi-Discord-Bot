import discord
import responses


async def send_message(message, user_msg, is_private):
    try:
        response = responses.handle_response(user_msg)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA5OTY4MTMzMDI0NzIzNzY2Mg.GAvrfD.vIrVCk4zFaOB2Aq7IDN7cKwC_Uxf86H5L3Mqzo'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is no running!')

    client.run(TOKEN)
