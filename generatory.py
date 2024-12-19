from random import randint
from collections import deque


def lcg(x, ln, m, a, c, scaling=True):
     if scaling:
        nums = [(x := (a*x + c) % m) / m for _ in range(ln)]
    else:
        nums = [x := (a * x + c) % m for _ in range(ln)]
    return nums


def glcg(x_vec, ln, m, a_vec, scaling=True):
    assert isinstance(x_vec, list)
    assert isinstance(a_vec, list)
    assert len(x_vec) == len(a_vec)
    
    x_vec = deque(x_vec)
    nums = [0]*ln
    
    for _ in range(ln):
        x = sum(a * x for a, x in zip(a_vec, reversed(x_vec))) % m
        x_vec.popleft()
        x_vec.append(x)
        if scaling:
            nums[t] = x/m
        else:
            nums[t] = x
        
    return nums


def rc4_32(K, L, r, m, i_arg=0, j_arg=0, S_arg=None, get_S=False, scdlevel=False):
    assert m >= L > 0 and type(L) == int
    assert len(K) == L
    assert r > 0 and type(r) == int
    
    # KSA
    if not scdlevel:
        S = list(range(m))
        j = 0
        for i in range(m):
            j = (j + S[i] + K[i % L]) % m
            S[i], S[j] = S[j], S[i]

    # PRGA
        i, j = i_arg, j_arg
        Y = [0]*r
        for t in range(r):
            i = (i + 1) % m
            j = (j + S[i]) % m
            S[i], S[j] = S[j], S[i]
            Y[t] = S[(S[i] + S[j]) % m]
        if not get_S:
            return Y
        else:
            return Y, i, j, S
    else:
        S = S_arg
        i, j = i_arg, j_arg
        Y = [0] * r
        for t in range(r):
            i = (i + 1) % m
            j = (j + S[i]) % m
            S[i], S[j] = S[j], S[i]
            Y[t] = S[(S[i] + S[j]) % m]
        return Y, i, j, S


# Blum Blum Shub
def bbs(p, q, x, ln, scaling=True):
    # assert is_prime(p) and is_prime(q)
    assert x % p != 0 and x % q != 0 and p % 4 == 3 and q % 4 == 3
    
    m = p*q
    if scaling:
        nums = [(x := x*x % m) / m for _ in range(ln)]
    else:
        nums = [x := x * x % m for _ in range(ln)]
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
