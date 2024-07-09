class Animals:
    def __init__(self, animals):
        self.animals = animals


    def getAnimals(self):
        return self.animals

    def recognition(self):
        if self.animals == "gatto" or self.animals == "cane":
            print("Questo e' un ")
            return self.animals
        else:
            return print("Non riconosco questo animale")

if __name__ == '__main__':
    a = Animals("gatto")
    print(a.recognition())
    print(a.getAnimals())
    a = Animals("cane")
    print(a.recognition())
    print(a.getAnimals())