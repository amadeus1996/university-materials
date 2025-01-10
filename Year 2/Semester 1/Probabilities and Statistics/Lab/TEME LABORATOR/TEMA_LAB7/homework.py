import math

print("EX 3")


# Exemplu real-life
# Intr-o ploaie de meteoriti, se vad in medie 3 stele cazatoare la 10 minute.
# Care este probabilitatea sa vedem cel putin 5 stele cazatoare in 10 minute?

# Rezolvare: calculam probabilitatea de a vedea exact 0, 1, ..., 4 stele cazatoare.
# Adunam probabilitatile.
# Probabilitatea de a vedea macar 5 stele cazatoare este (1 - p).

def ex3(nr_stele, avg):
    return (math.exp(-avg) * (avg ** nr_stele)) / math.factorial(nr_stele)


p = sum(ex3(i, 3) for i in range(5))
print(f"{1 - p}")

print("EX 6")


# Exemplu real-life
# Un anumit model de adidasi de alergat poate sa reziste pentru 1000km.
# Care e sansa sa reziste pentru mai mult de 1250km?
def ex6(d, avg):
    return math.exp(-avg * d)


print(ex6(1200, 1 / 1000))
