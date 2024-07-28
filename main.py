import numpy as np


def main():
    n = 4

    np.random.seed(0)
    matrix_a = np.random.randint(0, 11, size=(n, n))
    matrix_b = np.random.randint(0, 11, size=(n, n))
    print("Matrice A:\n", matrix_a)
    print("Matrice B:\n", matrix_b)

    summ = matrix_a + matrix_b
    print("Somma delle matrici:\n", summ)

    subb = matrix_a - matrix_b
    print("Differenza delle matrici:\n", subb)

    mul = matrix_a * matrix_b
    print("Prodotto delle matrici:\n", mul)


if __name__ == '__main__':
    main()
