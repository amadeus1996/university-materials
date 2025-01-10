import numpy as np
import matplotlib.pyplot as plt


def ex1():
    # Punctul a)
    t = np.load("sample_Normal 1.npy")
    plt.hist(t, bins=20, edgecolor='black')
    plt.title("Normal")
    plt.grid()
    plt.show()


def ex2():
    # Punctul a)
    A = np.load("sample_NegativBinom.npy")
    B = np.load("sample_Gamma.npy")
    plt.hist(A, bins=20, edgecolor='black')
    plt.title("NegativBinom")
    plt.grid()
    plt.show()
    plt.hist(B, bins=20, edgecolor='black')
    plt.title("Gamma")
    plt.grid()
    plt.show()


ex1()
ex2()
