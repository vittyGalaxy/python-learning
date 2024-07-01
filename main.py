if __name__ == '__main__':

    lettere = ["a", "b", "c", "d", "e"]
    punti = ["1", "3", "2", "5", "2"]
    a = zip(lettere, punti)
    print(a)

    a = list(zip(lettere, punti))
    print(a)

    dictionary = {key: value for key, value in a}
    print(dictionary)