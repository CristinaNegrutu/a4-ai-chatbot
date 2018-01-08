Exista 2 variabile ce memoreaza fisierul din care preluam datele(input) si fisierul .aiml (output)
Se initializeaza liste cu prefixe posibile pentru intrebari ce au intelesuri asemanatoare( de exemplu, pentru definitii in lista cu prefixele acestor intrebari se afla formulari precum "Defineste ", "Ce este ", dar si "" care este prefixul pentru cazul in care utilizatorul introduce doar termenul pe care-l vrea definit.
Se initializeaza o lista cu listele de prefixe si codul aferent fiecarei liste de prefixe.
Se verifica daca .aiml-ul a fost initializat: in caz ca nu, se scriu in aiml tagurile <aiml> si </aiml>, iar intre ele se introduc intrebarile de baza
Se citeste fisierul de input linie cu linie si se extrage din fiecare linie tipul intrebarii, corpul intrebarii si raspunsul si apoi se apeleaza functia adauga_intrebare_raspuns

O linie din fisierul de input este de forma:"def^celula^unitatea de baza morfofunctionala a organizarii materiei vii
def reprezinta tipul intrebarii ( este o definitie)
celula reprezinta corpul intrebarii inainte de care se vor introduce prefixele specifice pentru o intrebare legata de definitia termenului celula
iar dupa ultimul "^" avem raspunsul la intrebare

Alte tipuri de intreburi sunt intrebari legate de localizare, cauzalitate, de descriere, in general tipurile complementelor din gramatica limbii romane
Toate listele de prefixe si codurile lor se gasesc la inceputul scriptului

Functia corecteaza_intrebare transforma un string in upper_case
Functia check_intrebare verifica daca o intrebare se afla deja in fisierul .aiml
Functia initializare_intrebari introduce in .aiml intrebarile de baza cu caracterul "*" si ca raspuns recursia ce va gasi raspunsul
Functia update introduce inca un raspuns la o intrebare existenta ce are deja un raspuns( sau un raspuns unei intrebari ce nu are niciun raspuns)
Functia adauga_intrebare_raspuns adauga in fisier o intrebare( si raspunsul ei) la care vor ajunge prin recursie toate intrebarile incepand cu fiecare prefix aferent tipului intrebarii daca intrebarea nu exista sau doar se va adauga inca un raspuns la intrebare in cazul in care ea exista 
