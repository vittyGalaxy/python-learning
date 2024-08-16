def main():
    n = 10

    counter = 0
    for i in range(0, int(n)):
        a = input("Inserisci numero: ")

        if int(a) == 9:
            counter += 1

    print("I numeri 9 sono: ", str(counter))


if __name__ == '__main__':
    main()
