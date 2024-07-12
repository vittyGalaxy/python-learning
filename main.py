class Animal:
    def __init__(self, animals):
        self.animals = animals

    def get_animal(self):
        return self.animals

    def recognition(self):
        if self.animals == "gatto" or self.animals == "cane":
            print("Questo e' un ")
            return self.animals
        else:
            return print("Non riconosco questo animale")


def main():
    a = Animal("gatto")
    print(a.recognition())
    print(a.get_animal())
    a = Animal("cane")
    print(a.recognition())
    print(a.get_animal())



if __name__ == '__main__':
    main()