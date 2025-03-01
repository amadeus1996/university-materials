#inlocuiti fiecare comentariu TODO 

class NodArbore:
    def __init__(self, _informatie, _parinte=None):
        self.informatie = _informatie
        self.parinte = _parinte

    def drumRadacina(self):
        nod = self
        l = []
        while nod:
            #adaugam nod la finalul lui l
            l.append(nod)
            #urcam cu un nivel; variabila nod devine parintele sau
            nod = nod.parinte
        return l[::-1]

    def inDrum(self,infoNod):
        nod=self
        while nod:
            #verificam daca informatia nodului nod e egala cu infoNod
            if nod.informatie == infoNod:
                return True
            #urcam cu un nivel; variabila nod devine parintele sau
            nod = nod.parinte
        return False


    def __str__(self):
        return str(self.informatie)

    #c (a->b->c)
    def __repr__(self):
        #se foloseste join cu separatorul "->" pe o lista cu informatiile nodurilor returnate de drumRadacina()
        sirDrum = "->".join([str(x) for x in self.drumRadacina()])
        return f"{self.informatie}, ({sirDrum})"

class Graf:
    def __init__(self, _matr, _start, _scopuri):
        self.matr = _matr
        self.start = _start
        self.scopuri = _scopuri

    def scop(self, informatieNod):
        # daca informatieNod se afla in lista self.scopuri
        return informatieNod in self.scopuri

    def succesori(self, nod):
        lSuccesori=[]
        for infoSuccesor in range(len(self.matr)):
            conditieMuchie = self.matr[nod.informatie][infoSuccesor] == 1 #testam ca pe linia corespunzatoare informatiei nodului si pe coloana infoSuccesor avem 1 (muchie)
            conditieNotInDrum = not nod.inDrum(infoSuccesor) #TO DO testam ca infoSuccesor nu se afla in drumul nodului nod (cu metoda inDrum)
            if conditieMuchie and conditieNotInDrum:
                nodNou = NodArbore(infoSuccesor, nod) # obiect de tip NodArbore cu informatia infoSuccesor si parintele egal cu variabila nod
                lSuccesori.append(nodNou)
        return lSuccesori



m = [
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]

def BF(gr, nsol):
    coada = [NodArbore(gr.start, None)] #o lista cuprinzand un element de tip NodArbore cu informatia de start din graful gr
    #nodul de start fiind radacina, nu va avea parinte
    while coada:
        nodCurent = coada.pop() #primul nod din coada care e sters si returnat in nodCurent (functia pop)
        if gr.scop(nodCurent.informatie):
            print("Solutie: ", end="")
            print(repr(nodCurent))
            #scadem cu 1 numarul de solutii nsol
            nsol -= 1
            #daca numarul de solutii nsol este 0
            if nsol == 0:
                return
        coada+=gr.succesori(nodCurent) #adaugam succesorii generati cu gr.succesori pentru nodCurent



def depth_first(gr, nsol=1):
    # vom simula o stiva prin relatia de parinte a nodului curent
    DF(NodArbore(gr.start), nsol)


def DF(nodCurent, nsol):
    if nsol <= 0:  
        return nsol
    #print("Stiva actuala: " + repr(nodCurent.drumRadacina()))

    if gr.scop(nodCurent.informatie):
        print("Solutie: ", end="")
        print(repr(nodCurent))
        print("\n----------------\n")

        #scadem cu 1 numarul de solutii nsol
        nsol -= 1
        #daca numarul de solutii nsol este 0
        if nsol == 0:
            return nsol
    lSuccesori = gr.succesori(nodCurent) #lista cu succesorii generati cu gr.succesori pentru nodCurent
    # pentru fiecare succesor sc din lSuccesori
    for sc in lSuccesori:
        if nsol != 0:
            nsol = DF(sc, nsol)

    return nsol


start = 0
scopuri = [5, 9]
gr=Graf(m,start,scopuri)
# BF(gr, 4)

depth_first(gr, 4)