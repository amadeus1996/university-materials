import numpy as np
import matplotlib.pyplot as plt


def pct_a(niu, sigma, N):
    U1 = np.random.uniform(0, 1, N)
    U2 = np.random.uniform(0, 1, N)
    return niu + np.sqrt(-2 * sigma ** 2 * np.log(U1)) * np.cos(2 * np.pi * U2)


def pct_b(niu, sigma, N):
    U1 = np.random.uniform(0, 1, N)
    U2 = np.random.uniform(0, 1, N)
    return niu + np.sqrt(-2 * sigma ** 2 * np.log(U1)) * np.sin(2 * np.pi * U2)


def pct_c(niu, sigma, N):
    return np.random.normal(niu, sigma, N)


def f(x, niu, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-((x - niu) ** 2) / (2 * sigma ** 2))


simulari_a = pct_a(0, 1, 10000)
simulari_b = pct_b(0, 1, 10000)
simulari_c = pct_c(0, 1, 10000)

plt.figure(figsize=(12, 8))
x_vals = np.linspace(-4, 4, 10000)
functie_densitate = f(x_vals, 0, 1)

plt.hist(simulari_a, bins=50, density=True, alpha=0.6, color='blue', label="PCT A")
plt.hist(simulari_b, bins=50, density=True, alpha=0.6, color='red', label="PCT B")
plt.hist(simulari_c, bins=50, density=True, alpha=0.6, color='green', label="PCT C")
plt.plot(x_vals, functie_densitate, color='black', label="FUNCTIE DENSITATE")

plt.legend()
plt.grid()
plt.show()

print("PUNCTUL a):")
print(f"MEDIE: {np.mean(simulari_a):.4f}, VARIANTA: {np.var(simulari_a):.4f}")
print("PUNCTUL b):")
print(f"MEDIE: {np.mean(simulari_b):.4f}, VARIANTAA: {np.var(simulari_b):.4f}")
print("PUNCTUL c):")
print(f"MEDIE: {np.mean(simulari_c):.4f}, VARIANTA: {np.var(simulari_c):.4f}")
