#inlocuiti fiecare comentariu TODO 

class NodArbore:
    def __init__(self, _informatie, _parinte=None):
        self.informatie = _informatie
        self.parinte = _parinte

    def drumRadacina(self):
        # Return the path from the root to the current node
        nod = self
        l = []
        while nod:
            l.append(nod.informatie)
            nod = nod.parinte
        return l[::-1]

    def inDrum(self, infoNod):
        # Check if a node is in the path from the root to the current node
        nod = self
        while nod:
            if nod.informatie == infoNod:
                return True
            nod = nod.parinte
        return False

    def __str__(self):
        return str(self.informatie)

    def __repr__(self):
        # Return a string representation of the node and its path
        sirDrum = "->".join(map(str, self.drumRadacina()))
        return f"{self.informatie}, ({sirDrum})"

class Graf:
    def __init__(self, _start, _scopuri):
        self.start = _start
        self.scopuri = _scopuri

    def scop(self, informatieNod):
        # Check if a node is a goal node
        return informatieNod in self.scopuri

        # ex 1, pct b)
        # crearea unui obiect??
        # return informatieNod == stare_scop # (0, 0, 0)

    def succesori(self, nod):
        def testConditie(m, c):
            return m == 0 or m >= c

        lSuccesori = []
        # mal curent = mal cu barca
        if nod.informatie[2] == 1:
            misionariMalCurent = nod.informatie[1]
            canibaliMalCurent  = nod.informatie[0]
            misionariMalOpus   = Graf.N - nod.informatie[1]
            canibaliMalOpus    = Graf.N - nod.informatie[0]
        else:
            misionariMalOpus   = nod.informatie[1]
            canibaliMalOpus    = nod.informatie[0]
            misionariMalCurent = Graf.N - nod.informatie[1]
            canibaliMalCurent  = Graf.N - nod.informatie[0]
        nrMaxMisionari = min(misionariMalCurent, Graf.M)
        nrMinMisionari = 0

        for misionariBarca in range(nrMinMisionari, nrMaxMisionari + 1):
            if misionariBarca == 0:
                minCanibaliBarca = 1 
                maxCanibaliBarca = min(canibaliMalCurent, Graf.M)
            else:
                minCanibaliBarca = 0
                maxCanibaliBarca = min(Graf.M - misionariBarca, canibaliMalCurent, misionariBarca)
            
            for canibaliBarca in range(minCanibaliBarca, maxCanibaliBarca + 1):
                misionariMalCurentNou = misionariMalCurent - misionariBarca 
                canibaliMalCurentNou  = canibaliMalCurent - canibaliBarca 
                misionariMalOpusNou   = misionariMalOpus + misionariBarca 
                canibaliMalOpusNou    = canibaliMalOpus + canibaliBarca 
            
            if not testConditie(misionariMalCurentNou, canibaliMalCurentNou):
                continue 
            if not testConditie(misionariMalOpusNou, canibaliMalOpusNou):
                continue 

            if (nod.informatie[2] == 1):
                infoSuccesor = (canibaliMalCurentNou, misionariMalCurentNou, 0)
            else:
                infoSuccesor = (canibaliMalOpusNou, misionariMalOpusNou, 1)

            if not nod.inDrum(infoSuccesor):
                nodNou = NodArbore(infoSuccesor, nod)
                lSuccesori.append(nodNou)

        return lSuccesori

def BF(gr, nsol):
    # Breadth-First Search algorithm
    coada = [NodArbore(gr.start)]
    while coada:
        nodCurent = coada.pop(0)
        if gr.scop(nodCurent.informatie):
            print("Solutie: ", end="")
            print(repr(nodCurent))
            nsol -= 1
            if nsol == 0:
                return
        coada += gr.succesori(nodCurent)

def depth_first(gr, nsol=1):
    # Depth-First Search algorithm
    return DF(NodArbore(gr.start), nsol)

def DF(nodCurent, nsol):
    # Recursive Depth-First Search helper function
    if nsol <= 0:
        return nsol

    if gr.scop(nodCurent.informatie):
        print("Solutie: ", end="")
        print(repr(nodCurent))
        print("\n----------------\n")
        nsol -= 1
        if nsol == 0:
            return nsol

    lSuccesori = gr.succesori(nodCurent)
    for sc in lSuccesori:
        if nsol != 0:
            nsol = DF(sc, nsol)

    return nsol


def DF_Non_Recursive(gr, nsol):
    # Non-Recursive Depth-First Search algorithm
    stack = [NodArbore(gr.start)]
    while stack:
        nodCurent = stack.pop()
        if gr.scop(nodCurent.informatie):
            print("Solutie: ", end="")
            print(repr(nodCurent))
            nsol -= 1
            if nsol == 0:
                return
        stack.extend(gr.succesori(nodCurent)[::-1])

with open("input.txt") as f:
    aux = f.readline().split()
Graf.N = int(aux[0]) # propr. statice
Graf.M = int(aux[1])

# stare = (nr_canibali_mal_init, nr_misionari_mal_init, poz_barca)
# poz_barca: 1=mal_init, 0=mal_fin
start = (Graf.N, Graf.N, 1)
scopuri = [(0, 0, 0)]


# start = 0
# scopuri = [5, 9]

gr = Graf(start, scopuri)
BF(gr, 1)

# depth_first(gr, 4)
# DF_Non_Recursive(gr, 4)
