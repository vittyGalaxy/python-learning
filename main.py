class StudentRegister:
    def __init__(self):
        self.students = []

    def getStudents(self):
        if self.students:
            return self.students
        else:
            return "Il registro e' vuoto"

    def add_student(self, name):
        self.students.append(name)
        print(f"Studente {name} aggiunto al registro")

    def search_student(self, name):
        if name in self.students:
            print(f"Lo studente {name} e' presente nel registro.")

        else:
            print(f"Lo studente {name} non e' presente nel registro.")



def main():
    s = StudentRegister()
    print(s.getStudents())
    s.search_student("Vittorio")

    s.add_student("Vittorio")
    s.search_student("Vittorio")
    s.add_student("Luca")
    s.search_student("Vittorio")
    print(s.getStudents())




if __name__ == '__main__':
    main()