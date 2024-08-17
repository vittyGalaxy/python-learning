import random
import numpy as np


def main():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix)
    print(matrix.sum())
    print(np.sum(matrix, axis=0))
    print(np.prod(matrix, axis=1))
    max_value = np.max(matrix)
    max_index = np.unravel_index(np.argmax(matrix), matrix.shape)
    print(max_value)
    print(max_index)

if __name__ == '__main__':
    main()
