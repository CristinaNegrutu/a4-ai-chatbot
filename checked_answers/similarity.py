import subprocess
import distance
import re
import math
from collections import Counter
from collections import defaultdict

#raspunsTest = [["măduva", "NOUN", "măduva"], ["spinării", "NOUN", "spinare"], ["este", "VERB", "fi"], ["din","ADPOSITION","din"], ["formată", "NOUN","format"],["substanță","NOUN","substanță"],["cenușie","ADJECTIVE","cenușiu"],["unde","ADVERB","unde"],["unde","ADVERB","unde"],["predomină","VERB","predomina"],["celulele", "NOUN", "celulă"],["nervoase","ADJECTIVE","nervos"],["și","CONJUNCTION","și"],["substanța","NOUN","substanță"],["albă","ADJECTIVE","alb"],["aici","ADVERB","aici"],["predomină","VERB","predomina"],["prelungirile","NOUN","prelungire"],["nervoase","ADJECTIVE","nervos"],["celulelor","NOUN","celulă"],["nervoase","ADJECTIVE","nervos"]]

#raspunsStudent = [["Din","ADPOSITION","Din"],["substanță","NOUN","substanță"],["cenușie","ADJECTIVE","cenușiu"],["și","CONJUNCTION","și"],["substanță","NOUN","substanță"],["albă","ADJECTIVE","alb"],["aici","ADVERB","aici"],["predomină","VERB","predomina"],["prelungirile","NOUN","prelungire"],["nervoase","ADJECTIVE","nervos"],["celulelor","NOUN","celulă"],["nervoase","ADJECTIVE","nervos"]]


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    word = re.compile(r'\w+')
    words = word.findall(text)
    return Counter(words)

def scor_cosine(content_a, content_b):
    text1 = content_a
    text2 = content_b

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine_result = get_cosine(vector1, vector2)
    return cosine_result

def listaCuvinteDex(lista):
    listaDex = []
    for sublista in lista:
        listaDex.append(sublista[2])
    return listaDex

def propozitie_din_lista(lista):
    propozitie = ""
    for cuvant in lista:
        propozitie += cuvant
        propozitie += " "
    return propozitie

def cuvinte_relevante(lista):
    lista_noua = []
    for element in lista:
        if element[1].upper() in ("ADPOSITION", "ARTICLE", "CONJUNCTION", "ADVERB", "PRONOUN"):
            pass
        else:
            lista_noua.append(element[2])
    return lista_noua

def eliminare_levenshtein(listaTest, listaStudent):
    for cuvantStudent in listaStudent.copy():
        for cuvantTest in listaTest.copy():
            if distance.levenshtein(cuvantStudent, cuvantTest) < 2:
                listaStudent.remove(cuvantStudent)
                listaTest.remove(cuvantTest)
                break
    return (listaTest, listaStudent)

def functie_bigrame(cuvant):
    bigrame = []
    for index in range(len(cuvant)-1):
        bigrame.append(cuvant[index]+cuvant[index+1])
    return bigrame

def distanta_Sorensen(cuvantTest, cuvantStudent):                           #asemanare Sorensen
    bigrameCuvantStudent = functie_bigrame(cuvantStudent)
    bigrameCuvantTest = functie_bigrame(cuvantTest)

    count = 0
    for bigrama in bigrameCuvantStudent:
        if (bigrama in bigrameCuvantTest):
            count += 1

    proportieSimilaritate = (2 * count) / (len(bigrameCuvantStudent) + len(bigrameCuvantTest))
    return proportieSimilaritate

def eliminare_Sorensen(listaTest, listaStudent):                        #eliminare cuvinte asemanatoare Sorensen
    for cuvantStudent in listaStudent.copy():
        for cuvantTest in listaTest.copy():
            if distanta_Sorensen(cuvantStudent, cuvantTest) > 0.8:
                listaStudent.remove(cuvantStudent)
                listaTest.remove(cuvantTest)
                break
    return (listaTest, listaStudent)

def distanta_Jaro(cuvantTest, cuvantStudent):
    return (jellyfish.jaro_distance(cuvantTest, cuvantStudent))

def eliminare_Jaro(listaTest, listaStudent):                        #eliminare cuvinte asemanatoare Sorensen
    for cuvantStudent in listaStudent.copy():
        for cuvantTest in listaTest.copy():
            if distanta_Jaro(cuvantStudent, cuvantTest) > 0.8:
                listaStudent.remove(cuvantStudent)
                listaTest.remove(cuvantTest)
                break
    return (listaTest, listaStudent)

def eliminare_sinonime_neblocant(listaTest, listaStudent):
    sinonime = defaultdict(list)
    for cuvantTest in listaTest:
        arediacritice = 0
        for i in cuvantTest:
            if i in ['ă', 'î', 'ș', 'ț', 'â']:
                arediacritice = 1
        if arediacritice == 0:
            variableNamePython = subprocess.Popen(["java", "-jar", "sinonim.jar", cuvantTest],stdout=subprocess.PIPE)
            JavaVariableReturned = variableNamePython.stdout.read().decode(encoding='utf-16')
            listaSinonime = (re.findall("(\w+)", JavaVariableReturned))
            for sinonim in listaSinonime:
                sinonime[cuvantTest].append(sinonim)
    for cuvantTest in listaTest:
        for cuvantStudent in listaStudent:
            if cuvantStudent in sinonime[cuvantTest]:
                listaStudent.remove(cuvantStudent)
                listaTest.remove(cuvantTest)
                break
    return (listaTest, listaStudent)

def eliminare_sinonime_blocant(raspunsTest, raspunsStudent):
    variableNamePython = subprocess.Popen(["java", "-jar", "C:\\Users\\botez\\Desktop\\sinonim.jar", cuvant], stdout=pout)
    JavaVariableReturned = variableNamePython.stdout.read()
    while True:
        s = os.read(pin, 1000).decode("UTF-16")
        print(s)

def similaritate(raspunsTest, raspunsStudent):
    listaCuvinteDexTest = listaCuvinteDex(raspunsTest)
    listaCuvinteDexStudent = listaCuvinteDex(raspunsStudent)

    if sorted(listaCuvinteDexTest) == sorted(listaCuvinteDexStudent):                       #raspunsuri identice
        return 1

    propozitieTest = propozitie_din_lista(listaCuvinteDexTest)
    propozitieStudent = propozitie_din_lista(listaCuvinteDexStudent)

    if scor_cosine(propozitieTest, propozitieStudent) > 0.85:                               #raspunsuri asemanatoare
        return 1

    listaRelevantaStudent = cuvinte_relevante(raspunsStudent)
    listaRelevantaTest = cuvinte_relevante(raspunsTest)
    if scor_cosine(propozitie_din_lista(listaRelevantaStudent), propozitie_din_lista(listaRelevantaTest)) > 0.90: #dupa eliminarea cuvintelor irelevante, listele trebuie sa fie si mai similare
        return 1                                                            #raspunsuri fara cuvinte irelevante asemanatoare

    for cuvantTest in listaRelevantaTest:
        for cuvantStudent in listaRelevantaStudent:
            if cuvantTest == cuvantStudent:
                listaRelevantaTest.remove(cuvantTest)
                listaRelevantaStudent.remove(cuvantStudent)                 #eliminare cuvinte identice
                break
    #au ramas in lista de teste acele cuvinte care nu s-au regasit in raspunsul studentului
    #aplicam intai sinonime sau functiile de distanta?!?!
    #aplican intai distantele de similaritate pentru ca preluarea sinonimelor este foarte inceata

    listaRelevantaTest, listaRelevantaStudent = eliminare_levenshtein(listaRelevantaTest, listaRelevantaStudent)        #eliminare cuvinte asemanatoare

    listaRelevantaTest, listaRelevantaStudent = eliminare_Sorensen(listaRelevantaTest, listaRelevantaStudent)

    listaRelevantaTest, listaRelevantaStudent = eliminare_Jaro(listaRelevantaTest, listaRelevantaStudent)

    listaRelevantaTest, listaRelevantaStudent = eliminare_sinonime_neblocant(listaRelevantaTest, listaRelevantaStudent)

    if ( len(listaRelevantaTest) == 0 and (len(listaRelevantaStudent) / len(cuvinte_relevante(raspunsStudent))) <=  0.2 ):
        return True
    else:
        if( (len(listaRelevantaTest) / len(cuvinte_relevante(raspunsTest)) ) <= 0.2 and (len(listaRelevantaStudent) / len(cuvinte_relevante(raspunsStudent)) ) <=  0.2 ):
            return True
    return False



#print(similaritate(raspunsTest,raspunsStudent))