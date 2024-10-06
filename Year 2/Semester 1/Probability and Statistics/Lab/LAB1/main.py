import numpy as np

# a) 
# count = 0
# for _ in range(100000):
#     angle1 = np.random.rand() * 2 * np.pi
#     angle2 = np.random.rand() * 2 * np.pi
#
#     m1 = (np.cos(angle1) + np.cos(angle2)) / 2
#     m2 = (np.sin(angle1) + np.sin(angle2)) / 2
#
#     M = (m1 ** 2 + m2 ** 2) ** (1/2)
#
#     if M <= 0.5:
#         count += 1
#
# print(count / 100000)


# b)
# count = 0
# for _ in range(100000):
#     r = np.random.rand()
#     angle = np.random.rand() * 2 * np.pi
#     x = r * np.cos(angle)
#     y = r * np.sin(angle)
#     M = (x ** 2 + y ** 2) ** (1/2)
#     if M <= 0.5:
#         count += 1
#
# print(count / 100000)


# c)
count = 0
for _ in range(100000):
    r = np.random.rand()
    angle = np.random.rand() * 2 * np.pi
    x = (r ** (1 / 2)) * np.cos(angle)
    y = (r ** (1 / 2)) * np.sin(angle)
    M = (x ** 2 + y ** 2) ** (1 / 2)
    if M <= 0.5:
        count += 1

print(count / 100000)