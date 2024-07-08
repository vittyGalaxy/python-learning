class Persona:
    def __init__(self, name, age, sesso):
        print("Ciao, mi chiamo " + name + ", sono " + sesso + " e ho " + str(age) + " anni")

if __name__ == '__main__':

    Persona("Vittorio", 17, "Maschio")