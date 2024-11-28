# calculul integralelor de la a la b din f(x)
# f : (a, b) -> R

# pas 1: E[f(x)] = media unei functii aleatoare
# pas 2: law of large numbers (legea nr. mari)

# X discreta => media e x1*p1 + x2*p2 + ...
# X variabila aleatoare reala continua => E[X] = integrala pe R din x * fx(x), fx(x) e pdf. X
# E[f(x)] = integrala pe R din f(x) * fx(x)

# Exemplu: integrala de la 0 la 1 din e^(-x^2)
# ea devine integrala de la 0 la 1 din e^(-x^2) * 1, unde 1 = pdf X si e uniform pe (0, 1)
# Law of large numbers: am un sir infinit de variabile aleatoare independente si identic distribuite =>
# => (x1 + x2 + ... + xn) / n -> (converge cand n tinde la infinit catre) E[x1]
# xi : omega -> E => f : E -> R, f(x1) + ... f(xn) -> (converge cand n tinde la infinit catre) E[f(x1)]
# Obs: pentru n fixat, pot sa aproximez media E[f(x1)] ~ (f(x1) + ... + f(xn)) / n (termenul din dreapta fiind
# o variabila aleatoare
# E[e^(-X^2)]

# obs: se schimba intervalul din [0, 1] => [a, b], deci am nevoie de densitatea uniformei pe [a, b]
# densitatea uniforme va fi 1 / (b - a) (deci trebuie sa inmultesc rezultatul integralei cu (b-a))
# deci va fi (b - a) * E[f(x)]

# importance sampling: sampling dupa o distributie de importanta (anumite zone sunt mai importante)

# integrala pe R din f(x) = integrala de R din (f(x) / p(x)) * p(x)
# = E[g(X)], X variabila aleatoare ~ p(x) (pdf)

# convolutia unei functii: (f STAR g)(x) = integrala pe R din f(x * y)*g(y) dy
# Fsigma^2(x) = integrala pe R din f(x - y) * p(x) dx, unde p(x) e pdf N(0, sigma^2)
# E[f(x-y)], y e o variabila aleatoare cu distributia normala N(0, sigma^2)


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# EX 1
# 0.75


def ex1(a, b, f, N, n):
    def graph(f, a, b):
        x = np.linspace(a, b, n)
        plt.plot(x, f(x))
        plt.grid()
        plt.show()

    def monte_carlo(f, a, b, N, n):
        plt.hist(((b - a) * np.mean(f(np.random.uniform(a, b, size=(N, n))), axis=1)), color='green', density=True,
                 bins=50)
        plt.grid()
        plt.show()

    graph(f, a, b)
    monte_carlo(f, a, b, N, n)


n = 3700
N = 10000
f1 = lambda x: np.exp(-(x ** 2))
f2 = lambda x: np.sin(x) / x
f3_1 = lambda x: np.sin(x ** 2)
f3_2 = lambda x: np.cos(x ** 2)
f4 = lambda x: np.exp(np.exp(x))
f5 = lambda x: 10 * np.exp(-10 * x) * (x ** 2) * np.sin(x)


ex1(0, 1, f1, N, n)
# ex1(0, 5, f1, N, n)
# ex1(0, np.pi, f2, N, n) # eroare?
# ex1(0, np.pi * 2, f3_1, N, n)
# ex1(0, np.pi * 2, f3_2, N, n)
# ex1(0, 1.5, f4, N, n)
# ex1(0, 100, f5, N, n)


def ex3():
    a, b = 0, 5
    f = lambda x: np.sin(2 * x) + 0.3 * np.cos(10 * x) + 0.05 * np.sin(100 * x)

    x = np.linspace(a, b, 1000)
    y = f(x)
    plt.plot(x, y)
    plt.show()

    def filtrul_gaussian(X, f, sigma):
        results = []
        for x in X:
            y = np.random.normal(0, sigma, size=10000)
            results.append(np.mean(f(x - y) * norm.pdf(y, scale=sigma)))
        return np.array(results)

    sigmas = [1, 0.5, 0.2, 0.1, 0.05]
    t = np.linspace(a, b, 100)
    plt.figure()
    for sigma in sigmas:
        sigma_vals = filtrul_gaussian(t, f, sigma)
        plt.plot(t, sigma_vals)

    plt.grid()
    plt.show()


ex3()
