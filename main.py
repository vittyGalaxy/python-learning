class Building:
    def __init__(self, address, number_of_floors, construction_year):
        self.address = address
        self.number_of_floors = number_of_floors
        self.costruction_year = construction_year

    def get_address(self):
        return self.address

    def get_number_of_floors(self):
        return self.number_of_floors

    def get_costruction_year(self):
        return self.costruction_year

    def show_info(self):
        print(f"indirizzo: {self.address}, numero di piani: {self.number_of_floors}, anno di costruzione: {self.costruction_year}")


class House(Building):
    def __init__(self, address, number_of_floors, construction_year, number_of_rooms, garden):
        super().__init__(address, number_of_floors, construction_year)
        self.number_of_rooms = number_of_rooms
        self.garden = garden

    def get_number_of_rooms(self):
        return self.number_of_rooms

    def get_garden(self):
        return self.garden

    def show_info(self):
        super().show_info()
        if self.garden:
            self.garden = "C'e' il giardino"

        else:
            self.garden = "Non c'e' il giardino"
        print(f"numero camere: {self.number_of_rooms}, giardino: {self.garden}")


class Office(Building):
    def __init__(self, address, number_of_floors, construction_year, number_offices, elevator):
        super().__init__(address, number_of_floors, construction_year)
        self.number_offices = number_offices
        self.elevator = elevator

    def get_number_offices(self):
        return self.number_offices

    def get_elevator(self):
        return self.elevator

    def show_info(self):
        super().show_info()
        if self.elevator:
            self.elevator = "C'e' l'ascensore"

        else:
            self.elevator = "Non c'e' l'ascensore"
        print(f"numero di uffici: {self.number_offices}, l'ascensore: {self.elevator}")


def main():
    h = House("Via Roma 1", 2, 1990, 5, True)
    o = Office("Corso Venezia 15", 5, 2010, 10, True)

    h.show_info()
    print()
    o.show_info()
    print()

    print(h.get_address())
    print(h.get_number_of_floors())
    print(h.get_costruction_year())
    print(h.get_number_of_rooms())
    print(h.get_garden())

    print(o.get_address())
    print(o.get_number_of_floors())
    print(o.get_costruction_year())
    print(o.get_number_offices())
    print(o.get_elevator())


if __name__ == '__main__':
    main()
