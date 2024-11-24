from random import randint
from collections import deque


def lcg(x, ln, m, a, c):
    nums = [(x := (a*x + c) % m) / m for _ in range(ln)]
    return nums


def glcg(x_vec, ln, m, a_vec):
    assert isinstance(x_vec, list)
    assert isinstance(a_vec, list)
    assert len(x_vec) == len(a_vec)
    x_vec = deque(x_vec)
    nums = []
    for _ in range(ln):
        x = sum(a * x for a, x in zip(a_vec, reversed(x_vec))) % m
        x_vec.popleft()
        x_vec.append(x)
        nums.append(x/m)
    return nums


def rc4_32(K, L, r):
    assert 32 >= L > 0 and type(L) == int
    assert len(K) == L
    assert r > 0 and type(r) == int
    # KSA
    S = list(range(32))
    j = 0
    for i in range(32):
        j = (j + S[i] + K[i % L]) % 32
        S[i], S[j] = S[j], S[i]
    # PRGA
    i, j = 0, 0
    Y = []
    for _ in range(r):
        i = (i + 1) % 32
        j = (j + S[i]) % 32
        S[i], S[j] = S[j], S[i]
        Y.append(S[(S[i] + S[j]) % 32])
    return Y


# Blum Blum Shub
def bbs(p, q, x, ln):
    # assert is_prime(p) and is_prime(q)
    assert x % p != 0 and x % q != 0 and p % 4 == 3 and q % 4 == 3
    m = p*q
    nums = [(x := x**2 % m) / m for _ in range(ln)]
    return nums


if __name__ == "__main__":
    print("lcg, dane: 13, 1, 5: ", lcg(13, 10, 13, 1, 5))
    print("lcg, dane: 2**10, 3, 7: ", lcg(13, 10, 2**10, 3, 7))
    print('glcg: ', glcg([12, 14, 73], 10, 2**10, [3, 7, 68]))
    print("excell's seed=0: ", lcg(0, 10, 1, 0.9821,  0.211327))
    print("excell's seed=1812433253: ", lcg(1812433253, 10, 1, 0.9821, 0.211327))
    L = 5
    K = [randint(0, 31) for _ in range(L)]
    print(rc4_32(K, L, 25))
    print(bbs(7883, 15331, 683498, 10))
