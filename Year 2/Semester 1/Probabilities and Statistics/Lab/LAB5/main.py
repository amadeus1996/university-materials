import numpy as np

# EX 1
print("EX 1:")
N = 100000
A, B = np.random.randint(1, 7, N), np.random.randint(1, 7, N)
C = A + B

prob_A = np.mean(A == 1)
prob_B = np.mean(B == 6)
prob_C = np.mean(C == 7)
prob_A_inters_C = np.mean((A == 1) & (C == 7))
prob_B_inters_C = np.mean((B == 6) & (C == 7))
prob_A_inters_B_inters_C = np.mean((A == 1) & (B == 6) & (C == 7))

print(f"P(A) = {prob_A}")
print(f"P(B) = {prob_B}")
print(f"P(C) = {prob_C}")
print(f"P(A & C) = {prob_A_inters_C}, P(A) * P(C) = {prob_A * prob_C}")
print(f"P(B & C) = {prob_B_inters_C}, P(B) * P(C) = {prob_B * prob_C}")
print(f"P(A & B & C) = {prob_A_inters_B_inters_C}, P(A) * P(B) * P(C) = {prob_A * prob_B * prob_C}\n")

# EX 2
print("EX 2:")
A, C = np.random.randint(1, 7, N), np.random.randint(1, 7, N)
B = A + C

prob_A = np.mean(A <= 2)
prob_B = np.mean(B == 7)
prob_C = np.mean(C & 1)  # aici ar fi impar, dar nr. de fete impare = nr. de fete pare => 50/50
prob_A_inters_C = np.mean((A <= 2) & (C & 1))
prob_A_inters_B = np.mean((A <= 2) & (B == 7))
prob_B_inters_C = np.mean((B == 7) & (C & 1))
prob_A_inters_B_inters_C = np.mean((A <= 2) & (B == 7) & (C & 1))

print(f"P(A) = {prob_A}")
print(f"P(B) = {prob_B}")
print(f"P(C) = {prob_C}")
print(f"P(A & C) = {prob_A_inters_C}, P(A) * P(C) = {prob_A * prob_C}")
print(f"P(A & B) = {prob_A_inters_B}, P(A) * P(B) = {prob_A * prob_B}")
print(f"P(B & C) = {prob_B_inters_C}, P(B) * P(C) = {prob_B * prob_C}")
print(f"P(A & B & C) = {prob_A_inters_B_inters_C}, P(A) * P(B) * P(C) = {prob_A * prob_B * prob_C}\n")

# EX 3
print("EX 3: ")
print("A: primul zar e numar prim")
print("B: al doilea zar e patrat perfect")
print("C: modulul diferentei celor doua zaruri este 0 sau 2")

A, B = np.random.randint(1, 7, N), np.random.randint(1, 7, N)
C = np.abs(A - B)

prob_A = np.mean((A == 2) | (A == 3) | (A == 5))
prob_B = np.mean((B == 1) | (B == 4))
prob_C = np.mean((C == 0) | (C == 2))
prob_A_inters_B = np.mean((((A == 2) | (A == 3) | (A == 5)) & ((B == 1) | (B == 4))))
prob_A_inters_C = np.mean(((A == 2) | (A == 3) | (A == 5)) & ((C == 0) | (C == 2)))
prob_B_inters_C = np.mean(((B == 1) | (B == 4)) & ((C == 0) | (C == 22)))
prob_A_inters_B_inters_C = np.mean(((A == 2) | (A == 3) | (A == 5)) & ((B == 1) | (B == 4)) & ((C == 0) | (C == 2)))

print(f"P(A) = {prob_A}")
print(f"P(B) = {prob_B}")
print(f"P(C) = {prob_C}")
print(f"P(A & C) = {prob_A_inters_C}, P(A) * P(C) = {prob_A * prob_C}")
print(f"P(A & B) = {prob_A_inters_B}, P(A) * P(B) = {prob_A * prob_B}")
print(f"P(B & C) = {prob_B_inters_C}, P(B) * P(C) = {prob_B * prob_C}")
print(f"P(A & B & C) = {prob_A_inters_B_inters_C}, P(A) * P(B) * P(C) = {prob_A * prob_B * prob_C}\n")


# EX 4
print("EX 4: ")
X = np.random.uniform(-1, 1, N)
Y = np.random.uniform(-1, 1, N)
# Luam evenimentul "numar > 0"
prob_X = np.mean(X > 0)
prob_Y = np.mean(Y > 0)
prob_X_inters_Y = np.mean((X > 0) & (Y > 0))

print(f"P(X) = {prob_X}")
print(f"P(Y) = {prob_Y}")
print(f"P(X & Y) = {prob_X_inters_Y}, P(X) * P(Y) = {prob_X * prob_Y}\n")

Y = -X
prob_Y = np.mean(Y > 0)
prob_X_inters_Y = np.mean((X > 0) & (Y > 0))

print(f"P(X) = {prob_X}")
print(f"P(Y) = {prob_Y}")
print(f"P(X & Y) = {prob_X_inters_Y}, P(X) * P(Y) = {prob_X * prob_Y}\n")


# EX 5
print("EX 5: m = 32, M = 100")
N = 10000


def joc(m, M):
    for _ in range(N):
        if np.random.rand() <= 0.5:
            m += 1
        else:
            m -= 1

        if m == 0:
            return -1
        elif m == M:
            return 1
    return -1


count = 0
for _ in range(N):
    if joc(32, 100) > 0:
        count += 1
print(count / N)
