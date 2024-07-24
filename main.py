import numpy as np


def main():
    int_array = np.array([1, 2, 3, 4], dtype="int32")
    float_array = np.array([1.0, 2.0, 3.0], dtype="float64")

    print("Array di interi: ", int_array)
    print("Array di float: ", float_array)

    date = np.array([[1, 2, 3], [4, 5, 6]], dtype="int64")
    print("Numero di dimensioni: ", date.ndim)
    print("Forma dell'array: ", date.shape)
    print("Dimensione totale dell'array: ", date.size)
    print("Tipo di dati dell'array: ", date.dtype)
    print("Dimensione in byte degli elementi: ", date.itemsize, "byte")


if __name__ == '__main__':
    main()
