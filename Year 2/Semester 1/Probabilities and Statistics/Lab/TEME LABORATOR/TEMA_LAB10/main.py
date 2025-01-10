import numpy as np
import matplotlib.pyplot as plt
from pydataset import data
import scipy.stats


def ex3():
    t = data('trees')
    t = t.to_numpy()
    X = t[:, 0].astype('float')
    Y = t[:, 2].astype('float')
    alpha = scipy.stats.linregress(X, Y)[0]
    beta = scipy.stats.linregress(X, Y)[1]

    print("Punctul a)")
    print(t)
    print()

    print("Punctul b)")
    covarianta = np.mean((X - np.mean(X)) * (Y - np.mean(Y)))
    sigma_X = np.sqrt(np.var(X))
    sigma_Y = np.sqrt(np.var(Y))
    corelatie = covarianta / (sigma_X * sigma_Y)
    print(f"Covarianta(X, Y): {covarianta}")
    print(f"Coeficient de corelatie (X, Y): {corelatie}\n")

    # c) si d)
    x = np.linspace(np.min(X), np.max(X), 1000)
    plt.figure()
    plt.plot(x, alpha * x + beta, label='Dreapta de regresie')
    plt.scatter(X, Y)
    plt.show()

    print("Punctul e)")
    indici = np.random.permutation(len(X))
    aux = int(0.8 * len(X))
    X1, X2 = X[indici[:aux]], X[indici[aux:]]
    Y1, Y2 = Y[indici[:aux]], Y[indici[aux:]]
    regresie_aux = scipy.stats.linregress(X1, Y1)
    alfa_aux = regresie_aux.slope
    beta_aux = regresie_aux.intercept
    predictie = alfa_aux * X2 + beta_aux
    comparatii = np.column_stack((Y2, predictie))
    print("VALORI REALE, VALORI PREZISE:\n", comparatii)
    print()
    medie = np.mean((Y2 - predictie) ** 2)
    print(f"EROARE DE MEDIE: {medie:.4f}")


ex3()
