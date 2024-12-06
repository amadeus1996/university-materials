# X aleator discret => E(X) = sum{xi*pi}
# X ~ fX(x) => E(X) = integrala pe R din x*f(x) dx

# Var(X) = E[(X-E(X))^2] (cat de tare se abate X de la medie)

# COVARIANTA: cov(X,Y) = E[((X - E(X))(Y - E(Y))]
# covarianta e nr. real

# COEFICIENT DE CORELATIE: cor(X,Y) = cov(X,Y)/(sigmaX * sigmaY), unde sigmaX = sqrt(Var(X))
# coeficientul e intre [-1, 1]

# X, Y independente => E(X * Y) = E(X) * E(Y) => cov(X, Y) = 0 => cor(X, Y) = 0
# daca cor(X, Y) != 0 => X, Y nu sunt independente

# CORELATIE = 0 NU INSEAMNA CA X, Y SUNT INDEPENDENTE!

import numpy as np
import matplotlib.pyplot as plt
import pydataset
import scipy.stats


def ex1(N=100000):
    print("EX 1")
    X = np.random.uniform(-1, 1, N)
    # Y = np.random.uniform(-1, 1, N)
    # Y = X**2
    Y = X ** 3 + X
    # Y = X
    # Y = -X

    covarianta = np.mean((X - np.mean(X)) * (Y - np.mean(Y)))
    sigma_X = np.sqrt(np.var(X))
    sigma_Y = np.sqrt(np.var(Y))
    corelatie = covarianta / (sigma_X * sigma_Y)
    print(f"Covarianta(X, Y): {covarianta}")
    print(f"Coeficient de corelatie (X,Y): {corelatie}\n")

    plt.scatter(X, Y)
    plt.show()


def ex2(N=100000):
    print("EX 2")
    t = pydataset.data('iris')
    # t = pydataset.data('trees')
    date = t.to_numpy()

    X = date[:, 0].astype('float')
    Y = date[:, 2].astype('float')

    # plt.figure()
    # plt.plot(X, '-*')
    # plt.title('Sepal length')
    #
    # plt.figure()
    # plt.plot(Y, '-*')
    # plt.title('Petal length')
    # plt.show()

    covarianta = np.mean((X - np.mean(X)) * (Y - np.mean(Y)))
    sigma_X = np.sqrt(np.var(X))
    sigma_Y = np.sqrt(np.var(Y))
    corelatie = covarianta / (sigma_X * sigma_Y)
    print(f"Covarianta(X, Y): {covarianta}")
    print(f"Coeficient de corelatie (X,Y): {corelatie}")

    alpha = scipy.stats.linregress(X, Y)[0]
    beta = scipy.stats.linregress(X, Y)[1]

    x = np.linspace(np.min(X), np.max(X), 1000)
    plt.figure()
    plt.plot(x, alpha*x+beta,label='Dreapta de regresie')
    plt.plot(X, Y, '*')
    plt.show()


# ex1()
ex2()
