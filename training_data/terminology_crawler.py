# Script pentru preluarea datelor de pe medikal.ro
# Acestea sunt de forma " termen = definite "

import bs4 as bs
import urllib.request
import string


def get_data_from_medikalro_and_generate_aiml(aiml_write_file):
    with open(aiml_write_file, "w") as aiml_file:
        for ii in string.ascii_uppercase[10:]:
            for j in range(1, 25):
                source = urllib.request.urlopen(
                    "http://www.medikal.ro/dictionar-medical.html?lit=" + ii + "&pag=" + str(j)).read()

                soup = bs.BeautifulSoup(source, 'lxml')
                data = [tags.text for tags in soup.find_all('div', {'class': 'dictionar_rs'})]
                words = [w.replace('\n', '') for w in data]

                for word in words:
                    definition = word.split('                  ')

                    word = definition[0]
                    meaning = definition[1]

                    print(word + " " + meaning)

                    aiml_def1 = "<category>\n <pattern> * " + word.upper() + " </pattern>\n<template>" + meaning + "</template>\n</category>\n \n "
                    aiml_def2 = "<category>\n <pattern> " + word.upper() + " </pattern>\n<template>" + meaning + "</template>\n</category>\n \n "
                    aiml_def3 = "<category>\n <pattern> " + word.upper() + " * </pattern>\n<template>" + meaning + "</template>\n</category>\n \n "

                    aiml_file.write(str(aiml_def1))
                    aiml_file.write(str(aiml_def2))
                    aiml_file.write(str(aiml_def3))


get_data_from_medikalro_and_generate_aiml("../rule_based_chatbot/aimls/terminology.aiml")
