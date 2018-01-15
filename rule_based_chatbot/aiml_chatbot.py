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
        self._kernel = aiml.Kernel()
        old_path = os.getcwd()

        # TODO: fix this, not loading properly
        os.chdir(os.path.dirname(aiml_file_path))
        sys.path.insert(0, os.path.dirname(aiml_file_path))

        self._kernel.learn(aiml_file_path)
        self._kernel.respond('LOAD AIML B')

        os.chdir(old_path)

    def answer(self, question, *args, **kwargs):
        ans = self._kernel.respond(question)
        # print ('aiml ans: {}'.format(ans))
        if ans in ("", "Sorry. I didn't quite get that."):
            return None
        return ans
