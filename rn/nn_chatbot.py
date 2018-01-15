import os
import traceback
import sys

from rn.common.chatbot_i import IChatbot
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'nmt-chatbot'))
from inference import inference

class NNChatbot(IChatbot):
    """
    Chatbot based on NMT neural network
    """

    def __init__(self):
        super().__init__()

    def initialize(self):
        inference('initialize') # any text will do, first inference loads the model

    def answer(self, question, *args, **kwargs):
        try:
            answers = inference(question, False)
        except Exception as e:
            sys.stdout.flush()
            traceback.print_exc()
            return None

        return self._choose_best_answer(answers)

    def _choose_best_answer(self, answers):
        best_idx = answers['best_index']
        return answers['answers'][best_idx]
