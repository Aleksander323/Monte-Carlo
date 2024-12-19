from testy import *
from scipy.stats import kstest
from random import randint, seed
from time import time

start = time()

# Generowanie liczb, rozmiar = 2**20
st1 = time()
lcg_nums = lcg(1652, 2 ** 20, 2 ** 42, 16801, 126581)
sp1 = time()

st2 = time()
x_vec = [randint(1, 1200) for _ in range(k)]
a_vec = [randint(1, 1200) for _ in range(k)]
glcg_nums = glcg(x_vec, 2**20, 2**42, a_vec)
sp2 = time()

st3 = time()
bbs_nums = bbs(125223563, 25223743, 6834782, 2**20)
sp3 = time()

st4 = time()
L = 40
m = 32
seed(1234)
K = [randint(0, m-1) for _ in range(L)]
rc4_nums = rc4(K, L, 2**20, 32)
sp4 = time()

end = time()

start2 = time()
# Testowanie LCG

# test chi2, koszyki = 20
lcg_test1 = test_chi2(lcg_nums, 20)

# gap test alpha = 0.2, beta = 0.4, masa koszyka = 0.05
lcg_test2 = gap_test(lcg_nums, 0.2, 0.4, 0.05)

# test KS
lcg_test3 = kstest(lcg_nums, 'uniform')


# Testowanie GLCG

# test chi2, koszyki = 20
glcg_test1 = test_chi2(glcg_nums, 20)

# gap test alpha = 0.2, beta = 0.4, masa koszyka = 0.05
glcg_test2 = gap_test(glcg_nums, 0.2, 0.4, 0.05)

# test KS
glcg_test3 = kstest(glcg_nums, 'uniform')


# Testowanie bbs

# test chi2, koszyki = 20
bbs_test1 = test_chi2(bbs_nums, 20)

# gap test alpha = 0.2, beta = 0.4, masa koszyka = 0.05
bbs_test2 = gap_test(bbs_nums, 0.2, 0.4, 0.05)

# test KS
bbs_test3 = kstest(bbs_nums, 'uniform')


# Testowanie RC4

# test chi2_rc4, koszyki = 10
rc4_test1 = test_chi2_rc4(rc4_nums, 10, 32)

# frequency of pairs test
rc4_test2 = frequency_of_pairs_test(rc4_nums, 32)

# poker test
rc4_test3 = poker_test(rc4_nums, 32)


# Testowanie liczb e, pi, sqrt(2)

e_test = frequency_monobit_test(digits_e[0:1000])
pi_test = frequency_monobit_test(digits_pi[0:1000])
sqrt2_test = frequency_monobit_test(digits_sqrt2[0:1000])

end2 = time()

# Wyniki
print("Wyniki testowania lcg:")
print("test chi2:", lcg_test1)
print("gap test:", lcg_test2)
print("ks test:", lcg_test3)
print("..............")
print("Wyniki testowania glcg:")
print("test chi2:", glcg_test1)
print("gap test:", glcg_test2)
print("ks test:", glcg_test3)
print("..............")
print("Wyniki testowania bbs:")
print("test chi2:", bbs_test1)
print("gap test:", bbs_test2)
print("ks test:", bbs_test3)
print("..............")
print("Wyniki testowania rc4:")
print("test chi2 dyskretny:", rc4_test1)
print("frequency of pairs test:", rc4_test2)
print("poker test:", rc4_test3)
print("..............")
print("Wyniki testowania liczb e, pi, sqrt(2):")
print("p-wartość dla e:", e_test)
print("p-wartość dla pi:", pi_test)
print("p-wartość dla sqrt(2):", sqrt2_test)
print("..............")
print("Czas wykonania:", end-start, end2-start2)
print("czasy generowania: lcg:", sp1-st1, "glcg:", sp2-st2, "bbs:", sp3-st3, "rc4:", sp4-st4)



