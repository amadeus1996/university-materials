import numpy as np

N = 100000
prob_A = 0.03  # un utilizator a cumparat un produs = 3%
prob_B = 0.10  # un utilizator a apasat pe o reclama = 10%
prob_B_given_A = 0.80  # probabilitatea ca utilizatorul sa fi apasat pe reclama, stiind ca acesta cumparase produsul = 80%
# prob_A_given_B = probabilitatea ca utilizatorul sa cumpere produsul dupa ce apasa pe reclama
#                = (prob_B_given_A * prob_A) / prob_B

prob_A_numeric = np.random.rand(N) <= prob_A
count = 0  # de cate ori s-a apasat pe o reclama, stiind ca fusese cumparat produsul (B|A)
count_total = 0  # numarul de produse cumparate
for i in range(N):
    if prob_A_numeric[i]:  # daca a cumparat un produs
        count_total += 1
        if np.random.rand() <= prob_B_given_A:  # daca apasase pe o reclama, stiind ca produsul a fost cumparat
            count += 1

prob_A_numeric = np.sum(prob_A_numeric) / N # cam 3%
prob_B_given_A_numeric = count / count_total # cam 80%
prob_B_numeric = np.sum(np.random.rand(N) <= prob_B) / N # cam 10%

print(f"P(A): {prob_A_numeric}")
print(f"P(B): {prob_B_numeric}")
print(f"P(B|A): {prob_B_given_A_numeric}")
print(f"P(A|B): {(prob_B_given_A_numeric * prob_A_numeric) / prob_B_numeric}")
