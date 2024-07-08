class Persona:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def presentation(self):
        print(f"Ciao, mi chiamo {self.name}, sono {self.sex} e ho {self.age} anni")

if __name__ == '__main__':

    persona = Persona("Vittorio", 17, "Maschio")
    persona.presentation()