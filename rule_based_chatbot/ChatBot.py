import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


def from_console():
    sys.path.append(r'.')
    os.chdir(r'aimls')
    import aiml
    chat_bot = aiml.Kernel()

    chat_bot.learn('startup.xml')

    chat_bot.respond('load aiml b')

    while True:
        user_input = input('You >')
        bot_response = chat_bot.respond(user_input)

        if bot_response == "Sorry. I didn't quite get that.":
            # Use the neural network to generate a response
            pass
        else:
            print(bot_response)


def from_ui(user_input):
    from .aiml import Kernel
    chat_bot = Kernel()

    chat_bot.learn('startup.xml')

    chat_bot.respond('load aiml b')

    bot_response = chat_bot.respond(user_input)

    if bot_response == "Sorry. I didn't quite get that.":
        # Use the neural network to generate a response
        pass
    else:
        return bot_response


if __name__ == '__main__':
    from_console()
