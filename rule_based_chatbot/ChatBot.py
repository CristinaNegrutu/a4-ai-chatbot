import sys
import os
sys.path.append(r'.')
os.chdir(r'aimls')
import aiml

if __name__ == '__main__':
    
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

