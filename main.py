import numpy as np


def main():
    array_1d = np.arange(1, 16)
    print("Array 1D: ", array_1d)

    array_2d = array_1d.reshape(3, 5)
    print("Array 2D:\n", array_2d)

    second_row = array_2d[1, :]
    print("Seconda riga", second_row)

    third_column = array_2d[:, 2]
    print("Terza colonna:", third_column)

    mask = array_2d > 10
    major_elements_10 = array_2d[mask]
    print("Maschera booleana per elementi > 10:\n", mask)
    print("Elementi maggiori di 10: ", major_elements_10)

    sum_rows = np.sum(array_2d, axis=1)
    sum_columns = np.sum(array_2d, axis=0)
    print("Somma degli elementi di ciascuna riga: ", sum_rows)
    print("Somma degli elementi di ciascuna colonna: ", sum_columns)

    rows_sum_major_40 = array_2d[sum_rows > 40, :]
    print("Righe con somma degli elementi maggiore di 40:\n", rows_sum_major_40)


if __name__ == '__main__':
    main()
