import random

import numpy as np


def main():
    n = input("Inserisci quante ripetizioni di x: ")

    if int(n) < 0:
        return 0

    for i in range(0, int(n)):
        print(str(i + 1) + ") x")


if __name__ == '__main__':
    main()
