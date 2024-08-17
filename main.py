import random
import numpy as np


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(arr)
    even_numbers = []

    arr2 = []
    for i in arr:
        if i % 2 == 0:
            even_numbers.append(i)
            arr2.append(i)

        else:
            arr2.append(-1)

    print(even_numbers)
    print(arr2)

    arr3 = []
    for i in arr:
        if 5 < i < 15:
            arr3.append(i)

    print(arr3)

    arr_copy = []
    for i in arr:
        arr_copy.append(i * 2)

    print(arr_copy)



if __name__ == '__main__':
    main()
