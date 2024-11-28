import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


n, N = 100, 10000
pasi, prob = np.array([-2, 0, 1]), np.array([0.3, 0.4, 0.3])


def traiectorie(n):
    return np.cumsum(np.random.choice(pasi, size=n, p=prob))


def simulare_poz_finale(n, N):
    poz_finale = [np.sum(np.random.choice(pasi, size=n, p=prob)) for _ in range(N)]
    return np.array(poz_finale)


t = traiectorie(n)
plt.figure(figsize=(10, 6))
plt.plot(range(n), t)
plt.grid()
plt.show()

poz_finale = simulare_poz_finale(n, N)
plt.figure(figsize=(10, 6))
plt.hist(poz_finale, bins=50, density=True, alpha=0.6)

x = np.sum(prob * pasi)
y = np.sum(prob * (pasi - x) ** 2)
f = np.linspace(min(poz_finale), max(poz_finale), 1000)
g = norm.pdf(f, loc=n*x, scale=np.sqrt(n*y))
plt.plot(f, g)
plt.grid()
plt.show()
