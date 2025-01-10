import numpy as np
import matplotlib.pyplot as plt


# Jucatorul incepe cu suma de "m" lei si trebuie sa ajunga la "M" lei.
# Arunca 2 zaruri corecte (pot pica numere de la 1 la 6): daca insumeaza numerele care pica,
# suma minima posibila ar fi 2, cea maxima fiind 12. In cazul in care suma este un numar prim,
# jucatorul castiga acea suma in lei; altfel, pierde 5 lei.
# Runda este castigata daca ajunge la M lei; altfel, daca isi pierde toti banii, pierde runda.

def joc(m, M):
    global primes
    throws = 0
    while m > 0:
        throws += 1
        x = np.random.randint(1, 7) + np.random.randint(1, 7)
        if x in primes:
            m += x
            if m >= M:
                return 1, throws
        else:
            m -= 5
    return 0, throws


N = 10000
primes = {2, 3, 5, 7, 11}
m = 50
M = 100
count = 0
throws = []
for i in range(N):
    aux = joc(m, M)
    if aux[0]:
        count += 1
    throws.append(aux[1])
print(f"Probability of winning: {count / N}")

plt.hist(throws, bins=40, color="orange", edgecolor="black")
plt.title("Game duration (number of throws)")
plt.xlabel("Number of throws")
plt.ylabel("Number of games")
plt.show()
