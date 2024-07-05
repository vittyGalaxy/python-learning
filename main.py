def sum(a):
    s = 0
    for i in a:
        s += i
    return s

if __name__ == '__main__':

    b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sum(b))