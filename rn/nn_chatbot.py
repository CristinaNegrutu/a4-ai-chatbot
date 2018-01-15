import os
import traceback
import sys

from translate import Translator

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
        print('Loaded neural network chatbot model!')

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


class RomToRomNNChatbot(NNChatbot):
    def __init__(self):
        super().__init__()
        self._rom_to_eng = None
        self._eng_to_rom = None

    def initialize(self):
        super().initialize()
        self._rom_to_eng = Translator(from_lang='ro',to_lang='en')
        self._eng_to_rom = Translator(from_lang='en',to_lang='ro')

    def answer(self, rom_question, *args, **kwargs):
        try:
            eng_question = self._rom_to_eng.translate(rom_question)
            eng_answer   = super().answer(eng_question)
            rom_answer   = self._eng_to_rom.translate(eng_answer)
            return rom_answer

        except Exception as e:
            sys.stdout.flush()
            traceback.print_exc()
            return None