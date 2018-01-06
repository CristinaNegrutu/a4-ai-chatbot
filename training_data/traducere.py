# Comanda pentru a instala modulul:
# pip install translate



from translate import Translator

#from_lang -> limba care se doreste a fi tradusa
#to_lang -> limba in care se traduce

translator = Translator(from_lang='ro',to_lang='en')

translation = translator.translate("Care din urmatoarele patologii nu constituie posibile complicatii ale stenozei aortice?")

print(translation) #Output: Which of the following pathologies are not possible complications of aortic stenosis?
