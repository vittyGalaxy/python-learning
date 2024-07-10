class Employee:
    def __init__(self, name, surname, freshman, salary):
        self.name = name
        self.surname = surname
        self.freshman = freshman
        self.salary = salary

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getFreshman(self):
        return self.freshman

    def getSalary(self):
        return self.salary

    def increase_salary(self):
        self.salary += ((self.salary * 10) / 100)

    def print_details(self):
        print(f"Impiegato: {self.name} {self.surname}, matricola {self.freshman}, stipendio{self.salary:.2f} euro")





if __name__ == '__main__':
    e = Employee("Vittorio", "Tiozzo", 12345, 3000)
    print(e.getName())
    print(e.getSurname())
    print(e.getFreshman())
    print(e.getSalary())
    e.print_details()
    e.increase_salary()
    e.print_details()