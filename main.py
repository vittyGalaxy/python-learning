def count_duplications(a, b):
    value = 0
    for i in a:
        if i == b:
            value += 1

    return value


if __name__ == '__main__':

    c = [2, 3, 4, 4, 4, 5, 6, 7, 7, 8, 8, 8, 9, 9, 10]
    print(count_duplications(c, 2))
    print(count_duplications(c, 3))
    print(count_duplications(c, 4))
    print(count_duplications(c, 5))
    print(count_duplications(c, 6))
    print(count_duplications(c, 7))
    print(count_duplications(c, 8))
    print(count_duplications(c, 9))
    print(count_duplications(c, 10))
    print(count_duplications(c, 1))