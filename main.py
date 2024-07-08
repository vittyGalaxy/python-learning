class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def birthday(self):
        self.age += 1

    def __str__(self):
        return "Si chiama " + self.name + " " + self.surname + " e ha " + str(self.age) + " anni"


if __name__ == '__main__':

    p1 = Person("Vittorio", "Tiozzo", 17)
    p2 = Person("Marco", "Bianco", 11)

    print(p1)
    print(p2)

    p1.birthday()
    p2.birthday()

    print(p1)
    print(p2)