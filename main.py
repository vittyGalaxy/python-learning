import numpy as np


def main():
    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])
    sum = a + b
    sub = b - a
    mul = a * b
    div = b / a
    print("Somma: ", sum)
    print("Sottrazione: ", sub)
    print("Moltiplicazione: ", mul)
    print("Divisione: ", div)

    arr = np.array([1, 2, 3, 4])

    square_roots = np.sqrt(arr)
    exponential = np.exp(arr)

    print("Radici quadrate: ", square_roots)
    print("Esponenziali: ", exponential)

    c = np.array([1, 2, 3])
    d = 10
    result = c + d
    print("Il risultato e': ", result)

    x = np.array([1, 2, 3])
    y = np.array([[1], [2], [3]])
    result_matrix = x + y
    print("Il risultato del broadsting con una matrice: ", result_matrix)


if __name__ == '__main__':
    main()
