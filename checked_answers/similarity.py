import distance
import jellyfish
import re
import math
from collections import Counter

raspunsTest = [["maduva", "NOUN", "maduva"], ["spinarii", "NOUN", "spinare"], ["este", "VERB", "fi"], ["din","ADPOSITION","din"], ["formata", "NOUN","format"],["substanta","NOUN","substanta"],["cenusie","ADJECTIVE","cenusiu"],["unde","ADVERB","unde"],["unde","ADVERB","unde"],["predomina","VERB","predomina"],["celulele", "NOUN", "celula"],["nervoase","ADJECTIVE","nervos"],["si","CONJUNCTION","si"],["substanta","NOUN","substanta"],["alba","ADJECTIVE","alb"],["aici","ADVERB","aici"],["predomina","VERB","predomina"],["prelungirile","NOUN","prelungire"],["nervoase","ADJECTIVE","nervos"],["celulelor","NOUN","celula"],["nervoase","ADJECTIVE","nervos"]]

raspunsStudent = [["Din","ADPOSITION","Din"],["substanta","NOUN","substanta"],["cenusie","ADJECTIVE","cenusiu"],["si","CONJUNCTION","si"],["substanta","NOUN","substanta"],["alba","ADJECTIVE","alb"],["aici","ADVERB","aici"],["predomina","VERB","predomina"],["prelungirile","NOUN","prelungire"],["nervoase","ADJECTIVE","nervos"],["celulelor","NOUN","celula"],["nervoase","ADJECTIVE","nervos"]]
# raspunsStudent = [["Din","ADPOSITION","Din"],["substanta","NOUN","substanta"],["cenusie","ADJECTIVE","cenusiu"],["si","CONJUNCTION","si"],["substanta","NOUN","substanta"],["alba","ADJECTIVE","alb"]]


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


def distanta_cosine(content_a, content_b):
    text1 = content_a
    text2 = content_b

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine_result = get_cosine(vector1, vector2)
    return cosine_result


def creare_propozitie_din_lista (raspuns):
    propozitie=""
    for cuvant in raspuns:
        propozitie += cuvant[2]
        propozitie += " "
    return propozitie

def similarity_cosine(raspunsTest, raspunsStudent):
    propozitieStudent=""
    propozitieTest=""

    propozitieStudent = creare_propozitie_din_lista(raspunsStudent)     # Modificarea listelor de cuvinte in
    propozitieTest = creare_propozitie_din_lista(raspunsTest)           # propozitii de cuvinte(forma din DEX)

    if distanta_cosine(propozitieTest, propozitieStudent) < 0.9:        # Verificare similaritate pe stringuri
        pass

    substantiveStudent = []
    for cuvantStudent in raspunsStudent:
        if cuvantStudent[1] == "NOUN":
            substantiveStudent.append(cuvantStudent[2])                 # Lista substantive Student
    nrSubstStudent = len(substantiveStudent)
    print(nrSubstStudent)

    substantiveTest = []
    for cuvantTest in raspunsTest:
        if cuvantTest[1] == "NOUN":
            substantiveTest.append(cuvantTest[2])                       # Lista substantive Test
    nrSubstTest = len(substantiveTest)
    print(nrSubstTest)

    print("subst stud:", substantiveStudent)
    print("subst test:", substantiveTest)
    print("\n")

    for substS in substantiveStudent.copy():
        print("de eliminat: ", substS)
        for substT in substantiveTest.copy():
            print("     de elim:", substT)
            if distance.levenshtein(substS, substT) < 2:
                print("         eliminare: ", substS)
                substantiveStudent.remove(substS)
                substantiveTest.remove(substT)
                break
    print("Nr de subst ramase in student: ", len(substantiveStudent))
    print("Substantive student ramase: ", substantiveStudent)

    print("Nr de subst ramase in test: ", len(substantiveTest))
    print("Substantive test ramase: ", substantiveTest)

    if len(substantiveTest) == 0:
        print("1:sunt similare")
    if len(substantiveTest) / nrSubstTest < 0.5 and len(substantiveStudent) / nrSubstStudent < 0.5:
        print("2:sunt similare")
    if len(substantiveStudent) / len(substantiveTest) > 0.8 and len(substantiveStudent) / nrSubstStudent < 0.5:
        print("2:sunt similare")


def functie_bigrame(cuvant):
    bigrame = []
    for index in range(len(cuvant)-1):
        bigrame.append(cuvant[index]+cuvant[index+1])
    return bigrame

def distanta_Sorensen(cuvantTest, cuvantStudent):
    bigrameCuvantStudent = []
    bigrameCuvantTest = []

    bigrameCuvantStudent = functie_bigrame(cuvantStudent)
    bigrameCuvantTest = functie_bigrame(cuvantTest)

    count = 0
    for bigrama in bigrameCuvantStudent:
        if (bigrama in bigrameCuvantTest):
            count += 1

    proportieSimilaritate = ( 2 * count ) / (len(bigrameCuvantStudent) + len(bigrameCuvantTest) )
    return proportieSimilaritate

def distanta_Jaro(cuvantTest, cuvantStudent):
    return (jellyfish.jaro_distance(cuvantTest, cuvantStudent))



similarity_cosine(raspunsTest, raspunsStudent)
