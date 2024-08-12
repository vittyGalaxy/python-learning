import random

import numpy as np


def main():
    a = np.random.randint(1, 51, 10)
    print("Gli elementi sono: " + str(a))

    s = np.sum(a)
    print("somma: " + str(s))

    ma = np.max(a)
    print("massimo: " + str(ma))
    mi = np.min(a)
    print("minimo: " + str(mi))

    av = np.mean(a)
    print("media: " + str(av))

    sor = np.sort(a)
    print("Sort: " + str(sor))


if __name__ == '__main__':
    main()
