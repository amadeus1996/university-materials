import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# EX 2
def ex2(miu, sigma, alfa, beta, N):
    X = np.random.normal(miu, sigma, N)
    Y_a = alfa + X
    Y_b = beta * X
    Y_c = alfa + beta * X

    f = np.linspace(-4, 4, 1000)
    f_1 = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-((f - (miu + alfa)) ** 2) / (2 * sigma ** 2))
    f_2 = (1 / (np.sqrt(2 * np.pi) * (beta * sigma))) * np.exp(-((f - (beta * miu)) ** 2) / (2 * (beta * sigma) ** 2))
    f_3 = (1 / (np.sqrt(2 * np.pi) * (beta * sigma))) * np.exp(-((f - (alfa + beta * miu)) ** 2) / (2 * (beta * sigma) ** 2))

    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.hist(Y_a, bins=50, density=True, alpha=0.6, color='red')
    plt.plot(f, f_1, color='red')
    plt.title("1")

    plt.subplot(1, 3, 2)
    plt.hist(Y_b, bins=50, density=True, alpha=0.6, color='blue')
    plt.plot(f, f_2, color='red')
    plt.title("2")

    plt.subplot(1, 3, 3)
    plt.hist(Y_c, bins=50, density=True, alpha=0.6, color='yellow')
    plt.plot(f, f_3, color='red')
    plt.title("3")
    plt.show()


miu = 0
sigma = 1
alfa = 2
beta = 1.5
N = 100000
ex2(miu, sigma, alfa, beta, N)


# EX 5
n, N = 100, 10000
pasi = np.array([-1 / np.sqrt(0.5), 0, 1 / np.sqrt(0.5)])
prob = np.array([0.25, 0.5, 0.25])


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
plt.hist(poz_finale, bins=50, density=True, alpha=0.6, color="b", label="Histogram of Final Positions")

x = np.sum(prob * pasi)
y = np.sum(prob * (pasi - x) ** 2)
f = norm.pdf(x, loc=n*x, scale=np.sqrt(n*y))
plt.plot(x, f, "r--")
plt.grid()
plt.show()
