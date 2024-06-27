if __name__ == '__main__':
    dictionary = {"Hello": 4, "World": 5}
    print(dictionary)

    dictionary.update({"Hello Word": 9})
    print(dictionary)

    dictionary["Hello"] = 7
    print(dictionary)

    dictionary["Hello"] = 4
    print(dictionary)

    print(dictionary.get("Hello", 0))
    print(dictionary.get("Hi", 0))

    elemento = dictionary.pop("Hello Word", 0)
    print("elemento: " + str(elemento))
    print(dictionary)

    elemento = dictionary.pop("Hi", 0)
    print("elemento: " + str(elemento))
    print(dictionary)

    chiave = dictionary.keys()
    print("chiavi: " + str(chiave))

    valore = dictionary.values()
    print("valori: " + str(valore))

    elementi = dictionary.items()
    print("elementi: " + str(elementi))