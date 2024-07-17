from abc import ABC, abstractmethod


class TeamMember:
    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary

    def show_info(self):
        print(f"nome: {self.name}, cognome: {self.surname}, eta': {self.age}, stipendio: {self.salary}")

    def calculate_bonus(self):
        pass


class Developer(TeamMember):
    def __init__(self, name, surname, age, salary, programming_languages, years_of_experience):
        super().__init__(name, surname, age, salary)
        self.programming_languages = programming_languages
        self.years_of_experience = years_of_experience

    def get_programming_languages(self):
        return self.programming_languages

    def get_years_of_experience(self):
        return self.years_of_experience

    def show_info(self):
        super().show_info()
        print(f"linguaggio programmazione: {self.programming_languages}, anni di esperienza: {self.years_of_experience}")

    def calculate_bonus(self):
        return self.salary * self.years_of_experience * 0.05


class Manager(TeamMember):
    def __init__(self, name, surname, age, salary, teams_managed, projects_completed):
        super().__init__(name, surname, age, salary)
        self.teams_managed = teams_managed
        self.projects_completed = projects_completed

    def get_teams_managed(self):
        return self.teams_managed

    def get_projects_completed(self):
        return self.projects_completed

    def show_info(self):
        super().show_info()
        print(f"team gestiti: {self.teams_managed}, progetti completati: {self.projects_completed}")

    def calculate_bonus(self):
        return self.salary * self.projects_completed * 0.1


def main():
    d1 = Developer("Alice", "Verdi", 28, 3500.0, ["Python", "JavaScript"], 5)
    d2 = Developer("Bob", "Bianchi", 32, 4000.0, ["Java", "C++"], 7)
    m1 = Manager("Clara", "Rossi", 40, 6000.0, 3, 10)
    m2 = Manager("David", "Neri", 45, 7000.0, 4, 12)

    d1.show_info()
    print(f"Bonus: {d1.calculate_bonus():.2} euro")
    print()
    d2.show_info()
    print(f"Bonus: {d2.calculate_bonus():.2} euro")
    print()
    m1.show_info()
    print(f"Bonus: {m1.calculate_bonus():.2} euro")
    print()
    m2.show_info()
    print(f"Bonus: {m2.calculate_bonus():.2} euro")
    print()

    print(d1.get_name())
    print(d1.get_surname())
    print(d1.get_age())
    print(d1.get_salary())
    print(d1.get_programming_languages())
    print(d1.get_years_of_experience())

    print(d2.get_name())
    print(d2.get_surname())
    print(d2.get_age())
    print(d2.get_salary())
    print(d2.get_programming_languages())
    print(d2.get_years_of_experience())

    print(m1.get_name())
    print(m1.get_surname())
    print(m1.get_age())
    print(m1.get_salary())
    print(m1.get_teams_managed())
    print(m1.get_projects_completed())

    print(m2.get_name())
    print(m2.get_surname())
    print(m2.get_age())
    print(m2.get_salary())
    print(m2.get_teams_managed())
    print(m2.get_projects_completed())


if __name__ == '__main__':
    main()
