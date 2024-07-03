if __name__ == '__main__':
    def dizionario(stringa):
        dictionary = {}
        l = 0
        for i in stringa:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

        return dictionary

    print(dizionario("hello"))