import numpy as np
from scipy.stats import chisquare, norm
from random import randint, seed
from generatory import *
from collections import Counter


def test_chi2(nums, k):
    assert isinstance(nums, (list, np.ndarray))
    freq = [0] * k
    for x in nums:
        freq[int(x * k)] += 1

    return chisquare(freq)
    

def frequency_of_pairs_test(nums, M):
    n = len(nums) - len(nums) % 2
    freq = [0] * (M * M)

    for i in range(0, n, 2):
        freq[M * nums[i] + nums[i + 1]] += 1

    return chisquare(freq)


def test_chi2_rc4(nums, k, n):
    assert k <= n
    freq = [0] * k
    p = int(n/k)
    for x in nums:
        if x <= n - p:
            freq[int(x/p)] += 1
        else:
            freq[-1] += 1

    f_exp = [p*len(nums)/n] * (k - 1)
    f_exp.append(len(nums) - sum(f_exp))

    return chisquare(freq, f_exp)


def gap_test(nums, alpha, beta, masa):
    assert 0 <= alpha < beta <= 1 and beta-alpha > masa

    p = beta - alpha
    koszyki = 0

    while (1 - p) ** koszyki * p > masa:
        koszyki += 1

    gaps = []
    current_gap = 0
    nums_inside = 0

    for num in nums:
        if alpha <= num <= beta:
            gaps.append(current_gap)
            current_gap = 0
            nums_inside += 1
        else:
            current_gap += 1

    if nums_inside < 2:
        raise ValueError(
            "W liście nums znajdują się mniej niż 2 liczby z przedziału [alpha, beta] - nie można policzyć odległości")

    gap_values, counts = np.unique(gaps, return_counts=True)
    final_counts = [0] * (koszyki + 1)

    for i in range(len(gap_values)):
        if gap_values[i] < koszyki:
            final_counts[gap_values[i]] = counts[i]
    final_counts[-1] = sum(counts) - sum(final_counts)

    expected_counts = [(1 - p) ** k * p * nums_inside for k in range(koszyki)]
    expected_counts.append(nums_inside - sum(expected_counts))

    return chisquare(final_counts, expected_counts)


def poker_test(nums, M):
    n = len(nums) - (len(nums) % 5)
    freq = [0] * 5

    for i in range(0, n, 5):
        unique_count = len(Counter(nums[i:i+5]))
        freq[unique_count - 1] += 1

    S = [1, 15, 25, 10, 1]
    expected_freq = [S[0]/M**4]

    for i in range(4):
        expected_freq.append(expected_freq[i]*(M-1-i)*S[i+1]/S[i])
    expected_freq = [n*x/5 for x in expected_freq]

    return chisquare(freq, expected_freq)


def frequency_monobit_test(bits):
    n = len(bits)
    converted = [2*b-1 for b in bits]
    s = sum(converted)/np.sqrt(n)
    pv = 2*(1-norm.cdf(abs(s)))
    return pv


def scd_level_bits(digits, R):
    pv_freq = [0]*10
    x = 0

    for _ in range(R):
        bitsy = digits[x:(1000+x)]
        pv = frequency_monobit_test(bitsy)
        if pv == 1:
            pv_freq[-1] += 1
        else:
            pv_freq[int(10*pv)] += 1
        x += 1000
    print("Rozkład p-wartości:", pv_freq)

    return chisquare(pv_freq)


def scd_level_lcg(test, R, *args, **kwargs):
    pv_freq = [0]*10
    seed = 1652
    for _ in range(R):
        nums = lcg(seed, 2**20, 2 ** 42, 16801, 126581, scaling=False)
        seed = nums[-1]
        nums = [x / 2 ** 42 for x in nums]
        _, pv = test(nums, *args, **kwargs)
        pv_freq[int(pv * 10)] += 1
    print("Rozkład p-wartości:", pv_freq)
    return chisquare(pv_freq)


def scd_level_glcg(test, R, *args, **kwargs):
    pv_freq = [0] * 10
    seed = [1342, 648, 137, 19, 925]
    a_vec = [113, 4381, 7849, 229, 61]
    for _ in range(R):
        nums = glcg(seed, 2**20, 2 ** 42, a_vec, scaling=False)
        seed = nums[-5:]
        nums = [x / 2 ** 42 for x in nums]
        _, pv = test(nums, *args, **kwargs)
        pv_freq[int(pv * 10)] += 1
    print("Rozkład p-wartości:", pv_freq)
    return chisquare(pv_freq)


def scd_level_bbs(test, R, *args, **kwargs):
    pv_freq = [0] * 10
    seed = 6834782
    p, q = 125223563, 65581727
    m = p*q
    for _ in range(R):
        nums = bbs(125223563, 65581727, seed, 2**20, scaling=False)
        seed = nums[-1]
        nums = [x / m for x in nums]
        _, pv = test(nums, *args, **kwargs)
        pv_freq[int(pv * 10)] += 1
    print("Rozkład p-wartości:", pv_freq)
    return chisquare(pv_freq)


def scd_level_rc4(test, R, *args, **kwargs):
    pv_freq = [0] * 10
    L = 40
    m = 32
    K = [28, 7, 0, 5, 2, 5, 6, 22, 15, 1, 1, 1, 22,
         30, 29, 9, 5, 11, 7, 0, 31, 15, 4, 29, 4,
         5, 2, 17, 4, 19, 30, 22, 17, 15, 12, 29, 1, 4, 0, 21]
    nums, i, j, S = rc4(K, L, 2**20, m, get_S=True)
    _, pv = test(nums, *args, **kwargs)
    pv_freq[int(pv * 10)] += 1

    for _ in range(R-1):
        nums, i, j, S = rc4(K, L, 2**20, m, i_arg=i, j_arg=j, S_arg=S, scdlevel=True)
        _, pv = test(nums, *args, **kwargs)
        pv_freq[int(pv * 10)] += 1
    print("Rozkład p-wartości:", pv_freq)
    return chisquare(pv_freq)


if __name__ == "__main__":
    # seed(10)
    L = 13
    K = [randint(0, 31) for _ in range(L)]
    # for _ in range(10):
        # print(test_chi2(np.random.uniform, 10, size=1000))
