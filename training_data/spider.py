from bs4 import BeautifulSoup
import urllib.request
import re

with open("medbot2.aiml", 'w') as file:
    file.write("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n<aiml version=\"1.0\">\n")
    alphabet = "nopqrstuvwxyz"
    for chr in alphabet:
        with urllib.request.urlopen('http://www.sfatulmedicului.ro/dictionar-medical_'+chr) as response:
            html = response.read()

        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.findAll("ul", {"class": "lista-buletata"})
        for i in range(len(ul)):
            for li in ul[i]:
                if li.find("a") != -1:
                    url = li.find("a").attrs["href"]
                    try:
                        with urllib.request.urlopen(url) as response:
                            html_dictionary = response.read()
                    except:
                        continue
                    dicationary_page = BeautifulSoup(html_dictionary, 'html.parser')
                    word = dicationary_page.find("h1", {"class": "titlu-pagina"})
                    question = word.text
                    question = question.upper()
                    answer = dicationary_page.find("div", {"class": "content-articol"})
                    try:
                        if answer.find("p") != None:
                            answer = answer.find("p").text
                            if answer[-1] == '\n':
                                answer[-1] = ''
                        else:
                            answer = answer.find("div").text
                            if answer[-1] == '\n':
                                answer[-1] = ''
                    except:
                        continue
                    if "(" in question:
                        question = question[0:question.index("(")]
                    question ="* "+ question
                    data = []
                    data.append('\t<category>\n')
                    data.append("\t\t<pattern>" + question + "</pattern>\n")
                    data.append("\t\t<template> " + answer + " </template>\n")
                    data.append("\t</category>\n")
                    data.append("\n")
                    file.writelines(data)
                    print(word.text)

                    # <h1 class="titlu-pagina">Abandon</h1>