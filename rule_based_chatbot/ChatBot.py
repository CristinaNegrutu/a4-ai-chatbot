import sys
import traceback

from rn.common.chatbot_i import IChatbot
from rn.nn_chatbot import RomToRomNNChatbot
from rule_based_chatbot.aiml_chatbot import AimlChatbot


class FullChatbot(IChatbot):
    def __init__(self):
        super().__init__()
        self._aiml_chatbot = None
        self._nn_chatbot = None

    def initialize(self, aiml_file_path, *args, **kwargs):
        self._aiml_chatbot = AimlChatbot()
        self._aiml_chatbot.initialize(aiml_file_path)

        self._nn_chatbot = RomToRomNNChatbot()
        self._nn_chatbot.initialize(debug=False)

    def answer(self, question, *args, **kwargs):
        try:
            aiml_ans = self._aiml_chatbot.answer(question)

            if aiml_ans is None:
                return self._nn_chatbot.answer(question)
            else:
                return aiml_ans

        except Exception:
            sys.stdout.flush()
            traceback.print_exc()
            return None

AIML_FILE_PATH = 'aimls/startup.xml'

chatbot = FullChatbot()
chatbot.initialize(AIML_FILE_PATH)


def from_ui(user_input):
    return chatbot.answer(user_input)

if __name__ == '__main__':
    while True:
        user_input = input('You >')
        bot_response = chatbot.answer(user_input)
        print(bot_response)

