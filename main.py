class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def show_info(self):
        print(f"Nome: {self.name}, eta': {self.age}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def get_subject(self):
        return self.subject

    def show_info(self):
        super().show_info()
        print(f"Materia': {self.subject}")


class Student(Person):
    def __init__(self, name, age, classroom):
        super().__init__(name, age)
        self.classroom = classroom

    def get_classroom(self):
        return self.classroom

    def show_info(self):
        super().show_info()
        print(f"classe: {self.classroom}")


def main():
    t = Teacher("Giovanni Rossi", 40, "Matematica")
    s = Student("Anna Bianchi", 16, "3A")
    t.show_info()
    print()
    s.show_info()

    print()
    print(t.get_name())
    print(t.get_age())
    print(t.get_subject())
    print(s.get_name())
    print(s.get_age())
    print(s.get_classroom())


if __name__ == '__main__':
    main()
