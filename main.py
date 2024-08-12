import random

import numpy as np


def main():
    a = np.random.randint(10, 100, (3, 4))
    print("Matrice: " + str(a))

    sm = np.sum(a)
    print("somma: " + str(sm))

    sr = np.sum(a, axis=1)
    print("Somma degli elementi per riga: " + str(sr))

    maxc = np.max(a, axis=0)
    print("valore massimo di ciascuna colonna: " + str(maxc))

    arr = a + 10
    print("Matrice modificata: " + str(arr))


if __name__ == '__main__':
    main()
