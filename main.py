class House:
    def __init__(self, address, surface):
        self.address = address
        self.surface = surface

    def get_address(self):
        return self.address

    def get_surface(self):
        return self.surface

    def show_info(self):
        print(f"indirizzo: {self.address}, superficie: {self.surface}")


class Apartment(House):
    def __init__(self, address, surface, floor, number_of_rooms):
        super().__init__(address, surface)
        self.floor = floor
        self.number_of_rooms = number_of_rooms

    def get_floor(self):
        return self.floor

    def get_number_of_rooms(self):
        return self.number_of_rooms

    def show_info(self):
        super().show_info()
        print(f"piano: {self.floor}, numero di camere: {self.number_of_rooms}")


class Villa(House):
    def __init__(self, address, surface, garden, number_of_floors):
        super().__init__(address, surface)
        self.garden = garden
        self.number_of_floors = number_of_floors

    def get_garden(self):
        return self.garden

    def get_number_of_floors(self):
        return self.number_of_floors

    def show_info(self):
        super().show_info()
        print(f"giardino: {self.garden}, numero di piani: {self.number_of_floors}")


def main():
    a1 = Apartment("Via Roma 10", 80, 2, 3)
    a2 = Apartment("Corso Italia 25", 100, 5, 4)

    v1 = Villa("Via delle Rose 15", 250, True, 2)
    v2 = Villa("Via dei Gelsomini 20", 300, False, 3)

    apartment = [a1, a2]
    for a in apartment:
        a.show_info()
        print(a.get_address())
        print(a.get_surface())
        print(a.get_floor())
        print(a.get_number_of_rooms())

    villa = [v1, v2]
    for v in villa:
        v.show_info()
        print(v.get_address())
        print(v.get_surface())
        print(v.get_garden())
        print(v.get_number_of_floors())


if __name__ == '__main__':
    main()
