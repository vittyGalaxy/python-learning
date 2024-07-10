class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def accelerate(self):
        print("Sto accellerando")

    def brake(self):
        print("Sto frenando")

    def getBrand(self):
        return self.brand

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year)
        self.color = color

    def change_colour(self, new_color):
        self.color = new_color

    def getColor(self):
        return self.color

    def __str__(self):
        return super().__str__() + f", Color: {self.color}"


if __name__ == '__main__':
    v = Vehicle("Jeep", "Compass", 5)
    print(v.getBrand())
    print(v.getModel())
    print(v.getYear())
    print(Vehicle("Jeep", "Compass", 5))
    c = Car("Jeep", "Compass", 5, "Yellow")
    print(c.getColor())
    print(Car("Jeep", "Compass", 5, "Yellow"))