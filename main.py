import random

import numpy as np


def main():
    b = input("Inserisci la base: ")
    e = input("Inserisci l'esponente: ")

    p = 1
    for i in range(0, int(e)):
        p *= int(b)

    print("Il ristato e': ", str(p))


if __name__ == '__main__':
    main()
