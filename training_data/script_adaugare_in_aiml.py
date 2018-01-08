output="test.aiml"
input_file="date.txt"
q=list()
definitii=["DEFINESTE","DEFINITI","DEFINITIE","CE INSEAMNA","LA CE SE REFERA","LA CE SE REFERA PRIN","CE REPREZINTA","CE ESTE","EXPLICA",
           "EXPLICATI","EXPLICA-MI","EXPLICATI-MI",""]
cauzalitate=["DIN CE CAUZA","CAUZA","CE PROVOACA","DIN CE CAUZA APARE","DIN CE CAUZA EXISTA","DE CE APARE","DE CE EXISTA","DE CE APAR","DIN CE CAUZA APAR","CARE ESTE CAUZA"]
locatie=["UNDE ESTE","UNDE SE AFLA","UNDE SUNT","UNDE SE GASESTE","UNDE APARE","UNDE SE GASESC","UNDE APAR","UNDE ESTE LOCALIZAT",
         "UNDE SUNT LOCALIZATI","UNDE SUNT LOCALIZATE","UNDE SE ITALNESTE","UNDE SE INTALNESC","UNDE"]
direct=["PE CINE","CE"]
de_cine=["DE CINE", "DE CE"]
care=["CARE","PE CARE"]
cu_care=["CU CARE","CU CE","CU CINE"]
descriere=["DESCRIERE","DESCRIE","DESCRIETI","CUM ARATA","CE FORMA ARE","CU CE ADUCE","A CE ARATA","CU CE SEAMANA","CUM PARE"]
indirect=["CUI","CAREI","CARUI","CAROR"]
mod=["CUM"]
timp=["IN CAT TIMP","CAT TIMP","PENTRU CAT TIMP","CAT DUREAZA","CAT TIMP NECESITA","DE CAT TIMP ESTE NEVOIE CA SA","CAT TIMP DUREAZA","CAT TINE","CAT NECESITA",
      "CAND"]
q.append((definitii,"def"))
q.append((cauzalitate,'c'))
q.append((locatie,'l'))
q.append((direct,'d'))
q.append((de_cine,'dc'))
q.append((care,'care'))
q.append((cu_care,'cc'))
q.append((descriere,'des'))
q.append((indirect,'i'))
q.append((mod,'m'))
q.append((timp,'t'))

def corecteaza_intrebare(intrebare):
    intrebare_buna = ""
    for i in intrebare:
        if i.isalnum() or i==" ":
            intrebare_buna+=i.upper()
    return intrebare_buna

def check_intrebare(filename, intrebare):
    file=open(filename,'r')
    buffer=file.read()
    file.close()
    lungime=len(intrebare)
    for i in range(39,len(buffer)):
        if buffer[i:i+lungime]==intrebare.upper() and buffer[i-1]==">" and buffer[i+lungime]=="<" :
            file = open(filename, 'w')
            file.write(buffer)
            file.close()
            return True
    return False

def initializare_intrebari(filename):
    file = open(filename, 'r')
    buffer = file.read()
    file.close()

    new_buffer = buffer[:-7]
    for pattern in q:

        for l in pattern[0]:
            new_buffer += "\n<category>\n"
            new_buffer += "\t<pattern>"

            new_buffer += l + " * "
            new_buffer += "</pattern>\n"
            new_buffer += "\t<template>"
            new_buffer += "\n\t\t<srai>\n"
            if pattern[1] == "def":
                new_buffer += "\t\t\tDEFINESTE <star index=\"1\"/>"
            elif pattern[1] == "d":
                new_buffer += "\t\t\tCE <star index=\"1\"/>"
            elif pattern[1] == "c":
                new_buffer += "\t\t\tCAUZA <star index=\"1\"/>"
            elif pattern[1] == "l":
                new_buffer += "\t\t\tUNDE <star index=\"1\"/>"
            elif pattern[1] == "t":
                new_buffer += "\t\t\tCAND <star index=\"1\"/>"
            elif pattern[1] == "m":
                new_buffer += "\t\t\tCUM <star index=\"1\"/>"
            elif pattern[1] == "i":
                new_buffer += "\t\t\tCUI <star index=\"1\"/>"
            elif pattern[1] == "des":
                new_buffer += "\t\t\tDESCRIE <star index=\"1\"/>"
            elif pattern[1] == "dc":
                new_buffer += "\t\t\tDE CE <star index=\"1\"/>"
            elif pattern[1] == "cc":
                new_buffer += "\t\t\tCU CE <star index=\"1\"/>"
            elif pattern[1] == "care":
                new_buffer += "\t\t\tPE CARE <star index=\"1\"/>"
            new_buffer += "\n\t\t</srai>\n"
            new_buffer += "\t</template>\n"
            new_buffer += "</category>\n"
    new_buffer += '\n'
    new_buffer += buffer[-7:]
    file = open(filename, 'w')
    file.write(new_buffer)
    file.close()


def update(filename,intrebare,raspuns,flag):
    file=open(filename,'r')
    buffer=file.read()
    file.close()
    file=open(filename,'w')
    lungime=len(intrebare)
    for i in range(39,len(buffer)-lungime):
        if buffer[i:i+lungime]==intrebare.upper():
            if flag==1:
                new_buffer=buffer[:i+lungime+22]+"\n<random><li>"+raspuns+"</li></random>"+buffer[i+lungime+22:]
                file.write(new_buffer)
                return
            else:
                for j in range(i,len(buffer)-lungime):
                    if buffer[j:j+len("</random>")]=="</random>":
                        new_buffer = buffer[:j] + "\t<li>" + raspuns + "</li>\n\t" + buffer[j:]
                        file.write(new_buffer)
                        return


is_initialized=True

if not is_initialized:
    file=open(output,'w')
    buffer="<aiml version=\"1.0.1\" encoding=\"UTF-8\">\n</aiml>"
    file.write(buffer)
    file.close()
    initializare_intrebari(output)
def adauga_intrebare_raspuns(filename,intrebare,raspuns,tip):
    file = open(filename, 'r')
    buffer = file.read()
    file.close()
    new_buffer = buffer[:-7]
    new_buffer += "\n<category>\n"
    new_buffer += "\t<pattern>"
    if tip=="def":
        if check_intrebare(filename,"DEFINESTE " + intrebare):
            update(filename,"DEFINESTE " + intrebare,raspuns,0)
            return
        else:
            new_buffer += "DEFINESTE "+intrebare

    elif tip=="d":
        if check_intrebare(filename,"CE " + intrebare):
            update(filename,"CE " + intrebare,raspuns,0)
            return
        else:
            new_buffer += "CE " + intrebare

    elif tip=="c":
        if check_intrebare(filename,"CAUZA " + intrebare):
            update(filename,"CAUZA " + intrebare,raspuns,0)
            return
        else:
            new_buffer += "CAUZA " + intrebare

    elif tip=="l":
        if check_intrebare(filename,"UNDE " + intrebare):
            update(filename,"UNDE " + intrebare,raspuns,0)
            return
        else:
            new_buffer += "UNDE " + intrebare

    elif tip=="t":
        intrebari=timp
        if check_intrebare(filename,"CAND " + intrebare):
            update(filename,"CAND " + intrebare,raspuns,0)
            return
        else:
            new_buffer += "CAND " + intrebare

    elif tip=="m":
        if check_intrebare(filename,"CUM " + intrebare):
            update(filename,"CUM " + intrebare,raspuns,0)
            return
        else:
            new_buffer += "CUM " + intrebare

    elif tip == "i":
        if check_intrebare(filename,"CUI " + intrebare):
            update(filename,"CUI " + intrebare,raspuns,0)
            return
        else:
            new_buffer += "CUI " + intrebare

    elif tip == "des":
        if check_intrebare(filename,"DESCRIE " + intrebare):
            update(filename,"DESCRIE " + intrebare,raspuns,0)
            return
        else:
            new_buffer += "DESCRIE " + intrebare

    elif tip == "dc":

        if check_intrebare(filename,"DE CE " + intrebare):
            update(filename,"DE CE " + intrebare,raspuns,0)
            return
        else:
            new_buffer += "DE CE " + intrebare

    elif tip == "cc":
        if check_intrebare(filename,"CU CE " + intrebare):
            update(filename,"CU CE " + intrebare,raspuns,0)
            return
        else:
            new_buffer += "CU CE " + intrebare

    elif tip == "care":
        if check_intrebare(filename,"PE CARE " + intrebare):
            update(filename,"PE CARE " + intrebare,raspuns,0)
            return
        else:
            new_buffer += "PE CARE " + intrebare
    new_buffer += "</pattern>\n"
    new_buffer += "\t<template>"
    new_buffer += "\n\t\t<random>"+"\n\t\t\t<li>"+raspuns+"</li>\n\t\t</random>"
    new_buffer += "\n\t</template>\n"
    new_buffer += "</category>\n"
    new_buffer += '\n'
    new_buffer += buffer[-7:]
    file = open(filename, 'w')
    file.write(new_buffer)
    file.close()




lines = [line.rstrip('\n') for line in open(input_file)]
for line in lines:
    args=line.split('^')
    adauga_intrebare_raspuns(output,corecteaza_intrebare(args[1]),corecteaza_intrebare(args[2]),args[0])

# fisier_valeh="datenoi.txt"
# file=open(fisier_valeh,'r')
# buffer=file.read()
# buffer=buffer.replace("def^","_")
#
# questions=set(buffer.split("_"))
# questions.remove("")
# print(questions)
#
# for x in questions:
#     print(x)
#     aux=x.split("^")
#     adauga_intrebare_raspuns(output,aux[0],aux[1],"def")
# file.close()
# file=open(fisier_valeh,'w')
# file.write(buffer)
# file.close()