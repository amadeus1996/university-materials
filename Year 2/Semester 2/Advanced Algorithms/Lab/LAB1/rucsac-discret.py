aux = input().split()
n, C = int(aux[0]), int(aux[1])
# n, C = 3, 7

valori = [int(x) for x in input().split()[:n]]
greutati = [int(x) for x in input().split()[:n]]
# valori = [7,3,5]
# greutati = [5,3,4]

D = [[0 for _ in range(C + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, C + 1):
        D[i][j] = D[i - 1][j]
        if j - greutati[i - 1] >= 0:
            D[i][j] = max(D[i][j], valori[i - 1] + D[i - 1][j - greutati[i - 1]])
print(D[n][C])