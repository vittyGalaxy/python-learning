if __name__ == '__main__':
    t = ()
    print(type(t))

    t = (4)
    print(type(t))

    t = (4,)
    print(type(t))

    t = (4, 5, 6)
    (primo, secondo, terzo) = t
    print(primo)
    print(secondo)
    print(terzo)