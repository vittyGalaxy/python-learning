class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def __str__(self):
        return f"Ciao! Mi chiamo {self.name} {self.surname}!"



if __name__ == '__main__':
    s = Student("Vittorio", "Tiozzo")
    print(s.getName())
    print(s.getSurname())
    print(Student("Vittorio", "Tiozzo"))