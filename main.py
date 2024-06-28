if __name__ == '__main__':
    def fattoriale(x):
        if x == 1:
            return 1
        else:
            return x * fattoriale(x - 1)


    print(fattoriale(5))