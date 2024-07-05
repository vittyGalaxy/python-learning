def even_number(a):
    result = []

    for i in a:
        if (a[i] % 2) == 0:
            result.append(i)

    return result

if __name__ == '__main__':

    b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(even_number(b))