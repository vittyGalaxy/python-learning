import numpy as np


def main():
    date = [1, 2, 3, 4]
    arr = np.array(date)
    print("array: ", arr)

    zeros_array = np.zeros(5)
    ones_array = np.ones(5)
    print("zeros: ", zeros_array)
    print("ones: ", ones_array)

    empty_array = np.empty(3)
    range_array = np.arange(5)
    print("Empty: ", empty_array)
    print("Range: ", range_array)

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print("Matrice: ")
    print(matrix)


if __name__ == '__main__':
    main()
