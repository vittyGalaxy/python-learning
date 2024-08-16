import random
import numpy as np


def create_array(dim1, dim2, val_min, val_max):
    matr = np.random.randint(val_min, val_max, (dim1, dim2))

    return matr


def main():
    print(create_array(2, 3, 2, 7))


if __name__ == '__main__':
    main()
