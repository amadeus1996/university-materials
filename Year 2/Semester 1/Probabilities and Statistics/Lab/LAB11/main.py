import numpy as np
import matplotlib.pyplot as plt
import scipy.special

A = np.load("sample_Bernoulli_1.npy")
B = np.load("sample_Bernoulli_2.npy")
C = np.load("sample_Poisson.npy")
D = np.load("sample_Exp.npy")
plt.hist(A, bins=50)
plt.title("Bernoulli 1")
plt.grid()
plt.show()
plt.hist(B, bins=50)
plt.title("Bernoulli 2")
plt.grid()
plt.show()
plt.hist(C, bins=50)
plt.title("Poisson")
plt.grid()
plt.show()
plt.hist(D, bins=50)
plt.title("Exponential")
plt.grid()
plt.show()

# Problema de estimare de parametri ai unei distributii
# Cerinta: avem un set de date (observatii independente). Stim distributia din care provin, dar nu stim
# parametrul/parametrii. Vrem sa determinam o estimare pentru parametru.

# Rezolvare: METODA VEROSIMILITATII MAXIME (Maximum likelihood).
# Avem datele x1, x2, ..., xn. Avem f(x|t) = pdf/ponderea distributiei, si vrem parametrul t.
# L(x1, x2, ..., xn, t) = product{f(xi|t) | i de la 1 la n}.
# log L = sum{log(f(xi|t)) | i de la 1 la nx}

# X ~ Poisson(t), f(x|t) = e^(-t) * ((t^x) / x!)


# EX 2
n = len(A)
suma_A = np.sum(A)
t = np.linspace(0.01, 0.99, 100)
x = np.log(t) * suma_A + np.log(1 - t) * (n - suma_A)
aux = x.argmax()
plt.title("Bernoulli 1")
plt.plot(t, x)
plt.plot(t[aux], x[aux], '*', color='red')
plt.grid()
plt.show()

suma_B = np.sum(B)
y = -n * t + np.log(t) * suma_B - np.sum(np.log(scipy.special.factorial(B)))
aux = y.argmax()
plt.title("Bernoulli 2")
plt.plot(t, y)
plt.plot(t[aux], y[aux], '*', color='red')
plt.grid()
plt.show()

suma_C = np.sum(C)
z = n * np.log(t) + np.log(1 - t) * (suma_C - n)
aux = z.argmax()
plt.title("Poisson")
plt.plot(t, z)
plt.plot(t[aux], z[aux], '*', color='red')
plt.grid()
plt.show()

suma_D = np.sum(D)
w = -n * np.log(1 / t) - t * suma_D
aux = w.argmax()
plt.title("Exponential")
plt.plot(t, w)
plt.plot(t[aux], w[aux], '*', color='red')
plt.grid()
plt.show()
