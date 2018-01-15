import TextProcessingWebScraping
import similarity

def raspuns (intrebare, raspunsTest, raspunsStudent):
    listaRaspunsTest = TextProcessingWebScraping.populate_lists(r"http://nlptools.info.uaic.ro/WebPosRo/", raspunsTest,
                   r"C:\Users\Reflex\Desktop\chromedriver", 1)
    listaRaspunsStudent = TextProcessingWebScraping.populate_lists(r"http://nlptools.info.uaic.ro/WebPosRo/", raspunsStudent,
                   r"C:\Users\Reflex\Desktop\chromedriver", 1)

    return similarity.similaritate(listaRaspunsTest, listaRaspunsStudent)