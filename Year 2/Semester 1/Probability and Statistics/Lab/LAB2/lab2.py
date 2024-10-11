import numpy as np
import matplotlib.pyplot as plt


# EX 1
# punctul a)

def aruncare_corecta():
    return True if np.random.rand() <= 0.5 else False


# punctul b)
def aruncare_gresita():
    return True if np.random.rand() <= 0.7 else False


# punctul c)
count_corect = 0
count_masluit = 0
p1_corect = []
p2_corect = []
error = []
for i in range(10000):
    if aruncare_corecta():
        count_corect += 1
    if aruncare_gresita():
        count_masluit += 1
    p1_corect.append(count_corect / (i + 1))
    error.append(abs(0.5 - (count_corect / (i + 1))))
    p2_corect.append(count_masluit / (i + 1))

print(f"{count_corect / 10000}\n{count_masluit / 10000}\n")


# punctul d)
plt.plot(range(10000), p1_corect)
plt.plot(range(10000), p2_corect)
# plt.figure()
# plt.loglog(error)
plt.grid()
plt.show()

# for x in error:
#     print(x, end = " ")


# EX 2
# punctul a)
def zar_corect():
    n = np.random.rand()
    if n >= 5/6:
        return 1
    elif n >= 4/6:
        return 2
    elif n >= 3/6:
        return 3
    elif n >= 2/6:
        return 4
    elif n >= 1/6:
        return 5
    else:
        return 6


# punctul b)
def zar_gresit():
    n = np.random.rand()
    if n > 0.75:
        return 1
    elif n > 0.5:
        return 2
    elif n > 0.3:
        return 3
    elif n > 0.15:
        return 4
    elif n > 0.05:
        return 5
    else:
        return 6


# punctul c)
p_zar_corect = [0] * 6
p_zar_gresit = [0] * 6
for _ in range(10000):
    p_zar_corect[zar_corect() - 1] += 1
    p_zar_gresit[zar_gresit() - 1] += 1

for i in range(6):
    print(f"{i}: {p_zar_corect[i] / 10000}, {p_zar_gresit[i] / 10000}")


# EX 3 - SECVENTE DE 10/20/100 CU (HHHH) / (TTTT)
def sir_random(n): # SIRURI DE LUNGIME N CU 0/1
    t = []
    for _ in range(n):
        t.append(0 if np.random.rand() <= 0.5 else 1)
    return t


sir_de_1 = [1] * 4 # CONDITIA 1
sir_de_0 = [0] * 4 # CONDITIA 2

sir_de_8_de_1 = [1] * 8
sir_de_8_de_0 = [0] * 8

count = 0
n = 100 # LUNGIMEA SIRULUI
for _ in range(10000):
    sir = sir_random(n)
    for i in range(n - 3):
        # asta e pt 100, la 10/20 trebuie schimbate sirurile/lungimile din conditia de jos
        if sir[i:i+8] == sir_de_8_de_1 or sir[i:i+8] == sir_de_8_de_0:
            count += 1
            break

print(count / 10000)


# EX 4
zaruri = [[1, 4, 4, 4, 4, 4], [3, 3, 3, 3, 3, 6], [2, 2, 2, 5, 5, 5]]

p_zar_rosu = [0] * 6
p_zar_verde = [0] * 6
p_zar_negru = [0] * 6

x = np.random.randint(0, 3)
y = x
while y == x:
    y = np.random.randint(0, 3)

# 0 = rosu, 1 = verde, 2 = negru
count = 0
for _ in range(10000):
    a = np.random.randint(0, 6)
    b = np.random.randint(0, 6)
    if zaruri[x][a] > zaruri[y][b]:
        count += 1

if x == 0:
    print("1: ROSU")
elif x == 1:
    print("1: VERDE")
else:
    print("1: NEGRU")
if y == 0:
    print("2: ROSU")
elif y == 1:
    print("2: VERDE")
else:
    print("2: NEGRU")
print(count / 10000)

# rosu-negru: 0.41
# verde-negru: 0.58
# negru-verde: 0.42
# rosu-verde: 0.70
# negru-rosu: 0.57
# verde-rosu: 0.30
