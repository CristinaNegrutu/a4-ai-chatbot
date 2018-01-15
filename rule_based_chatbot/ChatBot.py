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
        self._nn_chatbot.initialize()

    def answer(self, question, *args, **kwargs):
        aiml_ans = self._aiml_chatbot.answer(question)

        if aiml_ans is None:
            return self._nn_chatbot.answer(question)
        else:
            return aiml_ans


AIML_FILE_PATH = 'aimls/startup.xml'
full_chatbot = None


def from_ui(user_input):
    global full_chatbot

    if full_chatbot is None:
        full_chatbot = FullChatbot()
        full_chatbot.initialize(AIML_FILE_PATH)

    return full_chatbot.answer(user_input)

if __name__ == '__main__':
    if full_chatbot is None:
        full_chatbot = FullChatbot()
        full_chatbot.initialize(AIML_FILE_PATH)

    while True:
        user_input = input('You >')
        bot_response = full_chatbot.answer(user_input)
        print(bot_response)

