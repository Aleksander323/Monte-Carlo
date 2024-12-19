from testy import *
from scipy.stats import kstest
from time import time

# start = time()

# Testowanie LCG
lcg_test1 = scd_level_lcg(test_chi2, 1000, 20)
lcg_test2 = scd_level_lcg(gap_test, 1000, 0.2, 0.4, 0.05)
lcg_test3 = scd_level_lcg(kstest, 1000, 'uniform')

# Testowanie GLCG
glcg_test1 = scd_level_glcg(test_chi2, 1000, 20)
glcg_test2 = scd_level_glcg(gap_test, 1000, 0.2, 0.4, 0.05)
glcg_test3 = scd_level_glcg(kstest, 1000, 'uniform')

# Testowanie bbs
bbs_test1 = scd_level_bbs(test_chi2, 1000, 20)
bbs_test2 = scd_level_bbs(gap_test, 1000, 0.2, 0.4, 0.05)
bbs_test3 = scd_level_bbs(kstest, 1000, 'uniform')

# Testowanie RC4
rc4_test1 = scd_level_rc4(test_chi2_rc4, 1000, 10, 32)
rc4_test2 = scd_level_rc4(frequency_of_pairs_test, 1000, 32)
rc4_test3 = scd_level_rc4(poker_test, 1000, 32)

# Testowanie liczb e, pi, sqrt(2)
e_test_scd = scd_level_bits(digits_e, 1000)
pi_test_scd = scd_level_bits(digits_pi, 1000)
sqrt2_test_scd = scd_level_bits(digits_sqrt2, 1000)

# end = time()

# Wyniki
print("Wyniki testowania lcg:")
print("scd level test chi2:", lcg_test1)
print("scd level gap test:", lcg_test2)
print("scd level ks test:", lcg_test3)
print("..............")
print("Wyniki testowania glcg:")
print("scd level test chi2:", glcg_test1)
print("scd level gap test:", glcg_test2)
print("scd level ks test:", glcg_test3)
print("..............")
print("Wyniki testowania bbs:")
print("scd level test chi2:", bbs_test1)
print("scd level gap test:", bbs_test2)
print("scd level ks test:", bbs_test3)
print("..............")
print("Wyniki testowania rc4:")
print("scd level test chi2 dyskretny:", rc4_test1)
print("scd level frequency of pairs test:", rc4_test2)
print("scd level poker test:", rc4_test3)
print("..............")
# print("Czas wykonania:", end-start)

