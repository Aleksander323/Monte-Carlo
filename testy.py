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


def scd_level(test, R, nums, *args, **kwargs):
    n = len(nums)
    pv_freq = [0] * 10
    j = 0
    size = int(n/R)
    
    for _ in range(R):
        segment = nums[j:j+size]
        _, pv = test(segment, *args, **kwargs)
        pv_freq[int(pv * 10)] += 1
        j += size

    return chisquare(pv_freq)


if __name__ == "__main__":
    # seed(10)
    L = 13
    K = [randint(0, 31) for _ in range(L)]
    print("bbs final p_value:", scd_level(test_chi2, 1000, bbs(125223563, 25223743, 6834782, 10**7), 100)[1])
    print("lcg final p_value:", scd_level(test_chi2, 1024, lcg(1652, 2 ** 24, 2 ** 40, 16801, 126581), 100)[1])
    print("rc4_32 final p_value:", scd_level(test_chi2_rc4, 1000, rc4_32(K, L, 10**7), 5, 32)[1])
    # for _ in range(10):
        # print(test_chi2(np.random.uniform, 10, size=1000))
