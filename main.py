class Animals:
    def __init__(self, animals):
        self.animals = animals


    def getAnimals(self):
        return self.animals

    def recognition(self):
        if self.animals == "gatto" or self.animals == "cane":
            return print("Questo e' un " + Animals.getAnimals(self))

        return print("Non riconosco questo animale")


if __name__ == '__main__':
    a = Animals("gatto")
    print(a.recognition())
    a = Animals("cane")
    print(a.recognition())
    a = Animals("wwwww")