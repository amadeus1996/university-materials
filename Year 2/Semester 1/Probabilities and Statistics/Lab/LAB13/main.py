import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# TEOREMA LIMITA CENTRALA Daca aveam x1, ..., xn i.i.d. (independente si identic distribuite),
# atunci (sqrt(n) / ceva) * (((x1 + ... + xn) / n) - miu) tinde la N(0,1) cu n tinde la +inf.

# P(a < chestia de sus < b) = integral{f(x) dx | [a, b]} (integrala de la a la b din pdf pentru N(0,1))


A = np.load("sample_Normal(mu,4).npy")
plt.title("Normal(mu,4)")
plt.hist(A, bins=50, edgecolor='black')
plt.grid()
plt.show()

B = np.load("sample_Normal(mu,sigma2).npy")
plt.title("Normal(mu,sigma2)")
plt.hist(B, bins=50, edgecolor='black')
plt.grid()
plt.show()

C = np.load("sample_Normal(3,sigma2).npy")
plt.title("Normal(3,sigma2)")
plt.hist(C, bins=50, edgecolor='black')
plt.grid()
plt.show()

print(st.norm.interval(0.99, loc=0, scale=1))