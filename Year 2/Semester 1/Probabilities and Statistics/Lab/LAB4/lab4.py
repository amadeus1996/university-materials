# EX 1)
import numpy as np


N = 1000000
boala_poz = 0
test_poz = 0
test_neg = 0
test_neg_poz = 0
dublu_test = 0
for _ in range(N):
    if np.random.rand() <= 0.02:
        boala_poz += 1
        probBoala = np.random.rand()
        probBoala2 = np.random.rand()

        if probBoala <= 0.98:
            dublu_test += 1
            test_poz += 1
        else:
            test_neg += 1
        if probBoala2 <= 0.98:
            dublu_test += 1

        if (probBoala <= 0.98 < probBoala2) or (probBoala > 0.98 >= probBoala2):
            test_neg_poz += 1
    else:
        if np.random.rand() <= 0.05:
            boala_poz += 1

print(f"Are test pozitiv si boala B: {test_poz / boala_poz}")
print(f"Are 2 teste pozitive si boala B: {dublu_test / boala_poz}") # probabil e gresit
print(f"Are un test poz, un test neg si are boala b: {test_neg_poz / boala_poz}\n") # probabil gresit?


# EX 2)
print("EX 2:")

isSpam = 0
listaPredefSpam = 0
listaPredefNonSpam = 0
for _ in range(N):
    aux = np.random.rand()
    if np.random.rand() <= 0.2: # daca este spam
        isSpam += 1
        if aux <= 0.8: # este spam si are lista predefinita
            listaPredefSpam += 1
    else: # nu este spam
        if aux <= 0.15: # are lista predefinita
            listaPredefNonSpam += 1

print(f"Probabilitate: {listaPredefSpam / (listaPredefSpam + listaPredefNonSpam)}")


# EX 3)
# print("EX 3:")
# a)
num1 = np.random.uniform(0, 1, N)
# print(num1)

# b)
a, b = 1, 2
num2 = np.random.beta(1, 2, N)
# print(num2)

# c)


# d)
num4 = np.random.randn(N)
# print(num4)
