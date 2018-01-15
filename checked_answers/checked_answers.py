from NLP import TextProcessingWebScraping
from . import similarity

import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMEDRIVER_PATH = os.path.join(BASE_PATH, 'NLP', 'chromedriver.exe')

def raspuns(intrebare, raspunsTest, raspunsStudent):
    listaRaspunsTest = TextProcessingWebScraping.populate_lists(r"http://nlptools.info.uaic.ro/WebPosRo/", raspunsTest,
                                                                CHROMEDRIVER_PATH)
    listaRaspunsStudent = TextProcessingWebScraping.populate_lists(r"http://nlptools.info.uaic.ro/WebPosRo/",
                                                                   raspunsStudent,
                                                                   CHROMEDRIVER_PATH)

    return similarity.similaritate(listaRaspunsTest, listaRaspunsStudent)
