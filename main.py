import numpy as np


def main():
    original_array = np.arange(10)
    remodelled_array = original_array.reshape((2, 5))
    print("Array originale: ", original_array)
    print("Array rimodellato:\n", remodelled_array)

    array_to_resize = np.array([1, 2, 3, 4])
    array_to_resize.resize((2, 3))
    print("Array ridimensionato:\n", array_to_resize)

    two_dimensional_array = np.array([[1, 2], [3, 4]])
    flat_ravel = two_dimensional_array.ravel()
    array_flatten = two_dimensional_array.flatten()
    print("Raven: ", flat_ravel)
    print("Flatten: ", array_flatten)


if __name__ == '__main__':
    main()
