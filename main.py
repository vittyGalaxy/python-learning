if __name__ == '__main__':
    a = "ciao"
    b = 3
    print(str(b) + a)

    c = a[:0]
    d = a[:1]
    e = a[:2]
    f = a[:3]
    g = a[:4]
    h = a[2:3]
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)

    a = True
    b = True
    c = not(not(a and b) or (b and a) and not b)
    print(c)

    b = False
    print(a)
    print(b)
    print(int(a))
    print(int(b))