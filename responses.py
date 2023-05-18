from random import randint
#TODO #1 Create documentation for user -> List of available commands (!help*),
#TODO #2 Create simple commands/games e.g. (Rock Paper Scissors, Roll a Dice, Ping members, Reminder)


def handle_response(message) -> str:
    msg = message.lower()

    if msg == '.hello':
        return "Hey there!"

    if msg == '.roll':
        return str(randint(1, 6))

    if msg == '!help':
        return f"```\nHello Im Joi.\n\nIm an AI designed by Zala to cater to the desires of customers, telling " \
               f"them what to want to hear.```" \
               f"```css\nOver 5 Commands!\n" \
               f".roll\n" \
               f"...```\n"
