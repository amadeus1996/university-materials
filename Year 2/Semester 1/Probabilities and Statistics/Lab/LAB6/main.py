# X ~ Bin(n, p) -> modeleaza nr. de succese din n aruncari, succesul avand probabilitate p
# P(X=k) = p(k) = C de n cate k * p^k * (1-p)^(n-k)

import numpy as np
import matplotlib.pyplot as plt
import math as m

# EX 1
n = 100
p = 0.4
N = 100000


def ex1(n, p, N=10000):
    simulari = []
    for _ in range(N):
        simulari.append(sum(np.random.rand() <= p for _ in range(n)))
    return simulari


simulari = ex1(n, p)
plt.figure(figsize=(35, 10))
plt.hist(simulari, bins=range(n + 2), color='orange', edgecolor='black')
plt.xticks(range(n + 1))
plt.show()


# EX 2
def ex2(n, k, p):
    return m.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

n = 10
k = 5
p = 0.3
s = 0
for i in range(k, n + 1):
    s += ex2(n, i, p)
print(s)


# EX 4
#X ~ Geom(p) => modeleaza aparitia primului succes, stiind ca succesul
# are probabilitate p
def ex4(p):
    U = np.random.rand()
    return int(np.log(U) / np.log(1 - p))


simulari = [ex4(p) for _ in range(N)]
plt.figure(figsize=(14, 6))
plt.hist(simulari, bins=range(1, max(simulari) + 1), density=True, color='skyblue', edgecolor='black')
plt.show()


# EX 5
print((1-p)**k)