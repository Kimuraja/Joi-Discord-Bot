from random import randint


def handle_response(message) -> str:
    p_msg = message.lower()

    if p_msg == 'hello':
        return "Hey there!"

    if p_msg == 'roll':
        return str(randint(1, 6))

    if p_msg == '!help':
        return "`This is a help message that you can modify.`"
    