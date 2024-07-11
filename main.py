class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def greet(self):
        print(f"Ciao, mi chiamo {self.name} e ho {self.age} anni")

class Employee(Person):
    def __init__(self, name, age, agency, position):
        super().__init__(name, age)
        self.agency = agency
        self.position = position

    def presents(self):
        print(f"Sono {self.name}, ho {self.age} anni, lavoro per {self.agency} come {self.position}")



def main():
    p = Person("Luca", 20)
    p.greet()

    e = Employee("Marco", 28, "TechCorp", "Sviluppatore")
    e.greet()
    e.presents()



if __name__ == '__main__':
    main()