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


if __name__ == '__main__':
    main()
