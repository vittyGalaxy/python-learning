def shape_area(choice):
    choice.lower()
    if choice == "square":
        b = input("Inserisci base: ")
        area = int(b) * 4

    if choice == "rectangle":
        b = input("Inserisci la base: ")
        h = input("Inserisci l'altezza: ")
        area = int(b) * int(h)

    if choice == "triangle":
        b = input("Inserisci la base: ")
        h = input("Inserisci l'altezza: ")
        area = (float(b) * float(h)) / 2

    if choice == "circle":
        r = input("Inserisci il raggio: ")
        area = 3.14 * (int(r) ** 2)

    return area


if __name__ == '__main__':

    print(shape_area("square"))
    print(shape_area("triangle"))
    print(shape_area("circle"))
    print(shape_area("rectangle"))