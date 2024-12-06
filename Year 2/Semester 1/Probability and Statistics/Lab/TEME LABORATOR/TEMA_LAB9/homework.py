import numpy as np
import matplotlib.pyplot as plt


def ex2():
    # punctul a)
    def pct_a(f, a, b, dimensiune):
        t = np.random.exponential(scale=1/10, size=dimensiune)
        t = t[(t >= a) & (t <= b)]
        return np.mean(f(t) / (10 * np.exp(-10 * t)))

    f = lambda x: 10 * np.exp(-10 * x) * (x ** 2) * np.sin(x)
    a, b = 0, 100
    aproximare = pct_a(f, a, b, 10000)
    print(f"Aproximarea integralei: {aproximare}")

    # punctul b)
    dimensiuni = np.arange(100, 10001, 500)
    aproximari = []
    for x in dimensiuni:
        aproximari.append(pct_a(f, a, b, x))

    plt.figure(figsize=(10, 6))
    plt.plot(dimensiuni, aproximari)
    plt.xlabel("Nr probe")
    plt.ylabel("Aproximare")
    plt.grid()
    plt.show()


ex2()
