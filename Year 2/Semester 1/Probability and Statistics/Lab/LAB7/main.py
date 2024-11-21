import numpy as np
import matplotlib.pyplot as plt


N = 1000000


def ex1():
    n = 10000
    lambda_val = 30

    simulari_pois = np.random.binomial(n, lambda_val / n, N)
    medie = np.sum(simulari_pois) / N
    print("E(X):", medie)
    print("VAR(X):", (np.sum(np.square(simulari_pois)) / N) - np.square(np.sum(simulari_pois) / N))
    print()

    plt.hist(simulari_pois, bins=100, density=True)
    plt.xlabel("Valori")
    plt.ylabel("Frecventa")
    plt.show()


def ex2():
    lambda_val = 150
    samples = np.random.poisson(lambda_val, N)
    print(np.mean(samples > lambda_val))
    print()


def ex4():
    lambda_val = 50
    U = np.random.uniform(0, 1, N)
    nums = (-1 / lambda_val) * np.log(U)

    plt.hist(nums, bins=100, density=True)
    plt.show()


def ex5():
    lambda_val_1 = 2.5
    lambda_val_2 = 5
    sample_1 = np.random.exponential(scale=lambda_val_1, size=N)
    sample_2 = np.random.exponential(scale=lambda_val_2, size=N)
    print(f"TELEFON 1 >= 2.5 ANI: {1 - np.mean(sample_1 <= lambda_val_1)}")
    print(f"TELEFON 1 >= 5 ANI: {1 - np.mean(sample_1 <= lambda_val_2)}")
    print(f"TELEFON 2 >= 2.5 ANI: {1 - np.mean(sample_2 <= lambda_val_1)}")
    print(f"TELEFON 2 >= 5 ANI: {1 - np.mean(sample_2 <= lambda_val_2)}")


ex1()
ex2()
ex4()
ex5()
