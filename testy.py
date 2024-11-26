import numpy
from scipy.stats import chisquare
from random import randint, seed
from generatory import rc4_32, lcg, glcg


def test_chi2(nums, k):
    assert isinstance(nums, (list, numpy.ndarray))
    freq = [0] * k
    for x in nums:
        freq[int(x * k)] += 1

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


def scd_level(test, R, nums, *args, **kwargs):
    n = len(nums)
    pv_freq = [0] * 10
    j = 0
    for _ in range(R):
        pv = test(nums[j:j+int(n/R)], *args, **kwargs)[1]
        pv_freq[int(pv * 10)] += 1
        j += int(n/R)

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
