import random
import numpy as np


def main():
    a = np.arange(0, 10)
    print(a)
    b = np.arange(10, 20)
    print(b)
    c = a + b
    print(c)
    print(c.mean())
    d = c * 2
    print(d)

    e = []
    for i in d:
        if i > 20:
            e.append(i)

    print(e)


if __name__ == '__main__':
    main()
