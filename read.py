import numpy as np
from matplotlib import pyplot as plt
from scipy import stats as sstats

import urllib.request


def read_digits(url):
    data = []
    with urllib.request.urlopen(url) as f:
        for line in f:
            data.append(line.strip())
    datastring = []

    for line in data:
        datastring.append(line.decode("utf-8"))

    datastring = ''.join(datastring)
    datastring = list(map(int, list(datastring)))

    return (np.array(datastring))


digits_pi = read_digits('http://www.math.uni.wroc.pl/~rolski/Zajecia/data.pi')
digits_e = read_digits('http://www.math.uni.wroc.pl/~rolski/Zajecia/data.e')
digits_sqrt2 = read_digits('http://www.math.uni.wroc.pl/~rolski/Zajecia/data.sqrt2')

if __name__ == "__main__":
    print(digits_pi[:30])
    #print(digits_e[:10])
    #print(digits_sqrt2[:10])