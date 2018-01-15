import os

import aiml
import sys

from rn.common.chatbot_i import IChatbot


class AimlChatbot(IChatbot):
    """
    Aiml based chatbot
    """

    def __init__(self):
        super().__init__()
        self._kernel = None

    def initialize(self, aiml_file_path):
        aiml_file_path = os.path.abspath(aiml_file_path)

        self._kernel = aiml.Kernel()
        self._kernel.learn(aiml_file_path)

        old_working_dir = os.getcwd()

        # change working directory in order to load AIML properly
        os.chdir(os.path.dirname(aiml_file_path))

        self._kernel.respond('LOAD AIML B')

        os.chdir(old_working_dir)

    def answer(self, question, *args, **kwargs):
        ans = self._kernel.respond(question)
        # print ('aiml ans: {}'.format(ans))
        if ans in ("", "Sorry. I didn't quite get that."):
            return None
        return ans
