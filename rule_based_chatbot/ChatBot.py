import sys
import os

from rn.common.chatbot_i import IChatbot
from rn.nn_chatbot import NNChatbot
from rule_based_chatbot.aiml_chatbot import AimlChatbot
#
# sys.path.append(r'.')
# os.chdir(r'aimls')
# import aiml

class FullChatbot(IChatbot):
    def __init__(self):
        super().__init__()
        self._aiml_chatbot = None
        self._nn_chatbot = None

    def initialize(self, aiml_file_path, *args, **kwargs):
        self._aiml_chatbot = AimlChatbot()
        self._aiml_chatbot.initialize(aiml_file_path)

        self._nn_chatbot = NNChatbot()
        self._nn_chatbot.initialize()

    def answer(self, question, *args, **kwargs):
        aiml_ans = self._aiml_chatbot.answer(question)

        if aiml_ans is None:
            return self._nn_chatbot.answer(question)
        else:
            return aiml_ans

if __name__ == '__main__':

    AIML_FILE_PATH = 'aimls/startup.xml'

    chatbot = FullChatbot()
    chatbot.initialize(AIML_FILE_PATH)

    while True:
        user_input = input('You >')
        bot_response = chatbot.answer(user_input)
        print(bot_response)

