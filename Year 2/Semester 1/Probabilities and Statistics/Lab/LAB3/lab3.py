import numpy as np
import matplotlib.pyplot as plt

# EX 1)
# a)
print("EX 1 - a):")
def ex_1(a: float, b: float, c: float, d: float) -> bool:
    return True if c <= np.random.uniform(a, b) <= d else False


count = 0
for _ in range(10000):
    if ex_1(0, 1, 0.3, 0.5):
        count += 1

print(count / 10000, end="\n\n")

# b)
print("EX 1 - b):")
count = 0
a = np.random.uniform(0, 1)
while a == 1:
    a = np.random.uniform(0, 1)

b = np.random.uniform(a, 1)

c = np.random.uniform(a, b)
while c == b:
    c = np.random.uniform(a, b)

d = np.random.uniform(c, b)

print(f"a={a}, b={b}, c={c}, d={d}")
for _ in range(10000):
    if ex_1(a, b, c, d):
        count += 1

print(count / 10000, end="\n\n")


# EX 2)
# a)
print("EX 2 - a):")
def ex_2(a1: float, b1: float, c1: float, d1: float, a2: float, b2: float, c2: float, d2: float) -> bool:
    x = np.random.uniform(a1, b1)
    y = np.random.uniform(a2, b2)
    return True if c1 <= x <= d1 and c2 <= y <= d2 else False


count = 0
for _ in range(10000):
    if ex_2(0, 1, 0.2, 0.8, 0, 1, 0.2, 0.8):
        count += 1

print(count / 10000, end="\n\n")

# b)
print("EX 2 - b):")
a1 = np.random.uniform(0, 1)
while a1 == 1:
    a1 = np.random.uniform(0, 1)

b1 = np.random.uniform(a1, 1)

a2 = np.random.uniform(0, 1)
while a2 == 1:
    a2 = np.random.uniform(0, 1)

b2 = np.random.uniform(a2, 1)

c1 = np.random.uniform(a1, b1)
while c1 == b1:
    c1 = np.random.uniform(a1, b1)

d1 = np.random.uniform(c1, b1)

c2 = np.random.uniform(a2, b2)
while c2 == b2:
    c2 = np.random.uniform(a2, b2)

d2 = np.random.uniform(c2, b2)

count = 0
for _ in range(10000):
    if ex_2(a1, b1, c1, d1, a2, b2, c2, d2):
        count += 1

print(f"a1={a1}, b1={b1}, a2={a2}, b2={b2}, c1={c1}, d1={d1}, c2={c2}, d2={d2}")
print(count / 10000, end="\n\n")


# EX 3)
print("EX 3 - a), b), c), d):")
def ex_3(r: float, d: int, N: int) -> float:
    R = 2 * r
    t = np.random.uniform(-R / 2, R / 2, size=(d, N))

    n = np.sum(1 * (np.linalg.norm(t, axis=0) <= r))

    volume = (n / N) * R ** d
    print(f"{d}D ball, r = {r}, volume = {volume}")
    return volume


volumes = []
for i in range(2, 11):
    volumes.append(ex_3(1, i, 100000))

plt.title("Estimarea numerica pentru aria discului B(0, r) cu d de la 2 la 10")
plt.plot(range(2, 11), volumes,  marker='o')
plt.xlabel("DIMENSIUNE")
plt.ylabel("VOLUM")
plt.show()
