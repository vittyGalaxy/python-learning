import random

import numpy as np


def create_array(dim_1, dim_2, val_min, val_max):
    a = []
    b = []
    for i in range(dim_1):
        a.append(random.randint(val_min, val_max))

    for i in range(dim_2):
        b.append(random.randint(val_min, val_max))

    array = np.array(a, b)

    return array


def main():
    arr = create_array(3, 4, 0, 10)
    print(arr)


if __name__ == '__main__':
    main()
