from NLP import TextProcessingWebScraping
from . import similarity

def raspuns(intrebare, raspunsTest, raspunsStudent):
    listaRaspunsTest = TextProcessingWebScraping.populate_lists(r"http://nlptools.info.uaic.ro/WebPosRo/", raspunsTest,
                                                                1)
    listaRaspunsStudent = TextProcessingWebScraping.populate_lists(r"http://nlptools.info.uaic.ro/WebPosRo/",
                                                                   raspunsStudent,
                                                                   0)

    return similarity.similaritate(listaRaspunsTest, listaRaspunsStudent)