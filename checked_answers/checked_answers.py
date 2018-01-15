from NLP import TextProcessingWebScraping
from . import similarity


def raspuns(intrebare, raspunsTest, raspunsStudent):
    listaRaspunsTest = TextProcessingWebScraping.populate_lists(r"http://nlptools.info.uaic.ro/WebPosRo/", raspunsTest,
                                                                r"/usr/bin/chromedriver")
    listaRaspunsStudent = TextProcessingWebScraping.populate_lists(r"http://nlptools.info.uaic.ro/WebPosRo/",
                                                                   raspunsStudent,
                                                                   r"/usr/bin/chromedriver")

    return similarity.similaritate(listaRaspunsTest, listaRaspunsStudent)
