import numpy as np


def main():
    array_1d = np.arange(10)
    print("Array 1D", array_1d)

    summ = np.sum(array_1d)
    maxx = np.max(array_1d)
    minn = np.min(array_1d)
    average = np.mean(array_1d)
    print("La somma e': ", summ)
    print("Il massimo e': ", maxx)
    print("Il minore e': ", minn)
    print("La media e': ", average)

    mask = array_1d > 5
    major_elements_5 = array_1d[mask]
    print("Maschera booleana per elementi > 5:\n", mask)
    print("Elementi maggiori di 5: ", major_elements_5)


if __name__ == '__main__':
    main()
