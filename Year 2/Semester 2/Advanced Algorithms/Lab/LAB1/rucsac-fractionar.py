aux = input().split()
n, C = int(aux[0]), int(aux[1])
# n, C = 3, 5

valori = [int(x) for x in input().split()[:n]]
greutati = [int(x) for x in input().split()[:n]]
# valori = [7,12,15]
# greutati = [2,3,5]

obiecte = []
for i in range(n):
    obiecte.append((valori[i], greutati[i]))
obiecte.sort(key = lambda x: -(x[0]/x[1]))

valMax = 0
for obiect in obiecte:
    if C - obiect[1] >= 0:
        valMax += obiect[0]
        C -= obiect[1]
    else:
        valMax += (obiect[0] * C / obiect[1])
        break 

print(valMax)