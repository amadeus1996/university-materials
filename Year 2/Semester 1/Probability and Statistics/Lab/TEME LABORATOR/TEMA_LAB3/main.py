import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


# EX 5)
print("EX 5:")


def pointInCircle(x, y, P, r):
    return ((x - P[0]) ** 2 + (y - P[1]) ** 2) <= r ** 2
    # formula: x^2 + y^2 <= r^2
    # verifica daca un punct este in disc


def pointInEllipse(x, y, a, b):
    return ((x / a) ** 2 + (y / b) ** 2) <= 1
    # formula: (x^2/a^2) + (y^2/b^2) <= 1
    # verifica daca un punct este in elipsa


N = 100000
X = np.random.uniform(-4, 4, N)
Y = np.random.uniform(-4, 4, N)
commonPoints = pointInCircle(X, Y, [2, 2], 2 ** (1 / 2)) & pointInEllipse(X, Y, 3, 2)
circle = plt.Circle((2, 2), 2 ** (1 / 2), color="red", fill=False)
ellipse = plt.matplotlib.patches.Ellipse((0, 0), 6, 4, edgecolor="green", fill=False)

plt.title("SIMULARE PCT COMUNE CERC-ELIPSA")
plt.scatter(X, Y, s=1, color="lightgray")
plt.scatter(X[commonPoints], Y[commonPoints], s=1, color="blue")
plt.gca().add_artist(circle)
plt.gca().add_artist(ellipse)
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.show()

count = np.sum(pointInCircle(X, Y, [2, 2], 2 ** (1 / 2)) & pointInEllipse(X, Y, 3, 2))
print((count / N) * 64, end="\n\n")


# EX 6)
print("EX 6:")


def f1(x, y):
    return x ** 2 + y ** 4 + 2 * x * y - 1


def f2(x, y):
    return y ** 2 + (x ** 2) * np.cos(x) - 1


def f3(x, y):
    return np.e ** (x ** 2) + y ** 2 - 4 + 2.99 * np.cos(y)


x_f1 = np.random.uniform(-3, 3, N)
y_f1 = np.random.uniform(-3, 3, N)

x_f2 = np.random.uniform(-5, 5, N)
y_f2 = np.random.uniform(-5, 5, N)

x_f3 = np.random.uniform(-2.5, 2.5, N)
y_f3 = np.random.uniform(-2.5, 2.5, N)

inside_D1 = f1(x_f1, y_f1) <= 0
inside_D2 = f2(x_f2, y_f2) <= 0
inside_D3 = f3(x_f3, y_f3) <= 0

print(f"Arie D1: {36 * (np.sum(inside_D1) / N)}")
print(f"Arie D2: {100 * (np.sum(inside_D2) / N)}")
print(f"Arie D3: {25 * (np.sum(inside_D3) / N)}", end="\n\n")

plt.title("SIMULARE D1")
plt.scatter(x_f1, y_f1, s=1, color='lightgray')
plt.scatter(x_f1[inside_D1], y_f1[inside_D1], s=1, color='green')
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.show()

plt.title("SIMULARE D2")
plt.scatter(x_f2, y_f2, s=1, color='lightgray')
plt.scatter(x_f2[inside_D2], y_f2[inside_D2], s=1, color='red')
plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.show()

plt.title("SIMULARE D3")
plt.scatter(x_f3, y_f3, s=1, color='lightgray')
plt.scatter(x_f3[inside_D3], y_f3[inside_D3], s=1, color='orange')
plt.xlim([-2.5, 2.5])
plt.ylim([-2.5, 2.5])
plt.show()


# EX 7)
print("EX 7:")
r, R = 1, 2
X = np.random.uniform(-R / 2, R / 2, N)
Y = np.random.uniform(-R / 2, R / 2, N)
count = np.sum((X ** 2 + Y ** 2) <= r ** 2)
pi = (count / N) * (R ** 2 / r ** 2)
print(pi, end="\n\n")


# EX 8)
print("EX 8:")


def stick():
    global count
    x1 = np.random.uniform(0, 10)
    angle = np.random.uniform(0, 2 * np.pi)
    x2 = x1 + np.cos(angle)
    for i in range(0, 11):
        if (x1 < i < x2) or (x1 > i > x2):
            count += 1
            break


count = 0
for _ in range(10000):
    stick()
print(20000 / count)
