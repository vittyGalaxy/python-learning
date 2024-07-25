import numpy as np


def main():
    array1 = np.array(([1, 2, 3]))
    array2 = np.array([4, 5, 6])

    concatenated = np.concatenate((array1, array2))
    print("Concatenato: ", concatenated)

    vstack = np.vstack((array1, array2))
    print("Vstack:\n", vstack)

    hstack = np.hstack((array1, array2))
    print("Hstack: ", hstack)

    large_array = np.arange(12)
    divided = np.split(large_array, 3)
    print("Diviso in 3 parti: ", divided)

    latge_matrix = np.array([[1, 2, 3], [4, 5, 6]])
    hsplit = np.hsplit(latge_matrix, 3)
    print("Hsplit:\n", hsplit)


if __name__ == '__main__':
    main()
