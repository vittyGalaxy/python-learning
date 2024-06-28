if __name__ == '__main__':
    print((lambda x: x ** 2)(2))

    quadrato = lambda x: x ** 2
    print(quadrato(4))


    def funct(f, num):
        return f(num)


    print(funct(lambda x: x ** 2, 8))