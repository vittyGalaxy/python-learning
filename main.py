if __name__ == '__main__':
    a = 3
    b = 3
    print(a is b)

    a = 2
    print(a is not b)
    print(a is b)

    a = "ciao"
    print("c" in a)
    print("i" in a)
    print("a" in a)
    print("o" in a)
    print("s" in a)

    a = 4
    totale = (a * b) + (a * 2)
    print(totale)

    a += b
    print(a)

    a -= b
    print(a)

    a *= b
    print(a)

    a /= b
    print(a)

    c = 5
    print(a > b or a < c)
    print(b < a < c)
    print(c > b or a < c)
    print(b > a and a < c)
    print(b > a and c < a)