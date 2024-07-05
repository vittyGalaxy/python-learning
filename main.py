def max_number(a):
    m = a[0]
    for i in a:
        if i > m:
            m = i

    return m

if __name__ == '__main__':

    b = [1, 5, 2, 22, 99, 100, 2, 4, 8]
    print(max_number(b))