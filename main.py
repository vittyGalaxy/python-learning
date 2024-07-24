import numpy as np


def main():
    arr = np.array([10, 20, 30, 40, 50])
    first_element = arr[0]
    fourth_element = arr[3]
    print("Primo elemento: ", first_element)
    print("Quarto elemento: ", fourth_element)

    subsequence = arr[1:4]
    print("Sottosequenza: ", subsequence)

    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    first_line = matrix[0]
    second_line = matrix[:, 1]
    print("Prima riga: ", first_line)
    print("Seconda colonna: ", second_line)

    under_matrix = matrix[0:2, 1:3]
    print("sotto-matrice:\n", under_matrix)

    matrix[2, 2] = 99
    print("Matrice, aggiornata: \n", matrix)

if __name__ == '__main__':
    main()
