class Game:
    def __init__(self, name, minimum_age):
        self.name = name
        self.minimum_age = minimum_age

    def get_name(self):
        return self.name

    def get_minimum_age(self):
        return self.minimum_age

    def show_info(self):
        print(f"Nome: {self.name}, eta' minima: {self.minimum_age}")


class OutDoorGame(Game):
    def __init__(self, name, minimum_age, space_needed):
        super().__init__(name, minimum_age)
        self.space_needed = space_needed

    def get_space_needed(self):
        return self.space_needed

    def show_info(self):
        super().show_info()
        print(f"spazio necessario: {self.space_needed}")


class BoardGame(Game):
    def __init__(self, name, minimum_age, number_player):
        super().__init__(name, minimum_age)
        self.number_player = number_player

    def get_number_player(self):
        return self.number_player

    def show_info(self):
        super().show_info()
        print(f"Numero giocatori: {self.number_player}")


def main():
    o1 = OutDoorGame("Calcio", 6, "Campo da calcio")
    o2 = OutDoorGame("Nascondino", 4, "Giardino")
    b1 = BoardGame("Monopoly", 8, 4)
    b2 = BoardGame("Scacchi", 10, 2)
    o1.show_info()
    print()
    o2.show_info()
    print()
    b1.show_info()
    print()
    b2.show_info()

    print(o1.get_name())
    print(o1.get_minimum_age())
    print(o1.get_space_needed())
    print(o2.get_name())
    print(o2.get_minimum_age())
    print(o2.get_space_needed())
    print(b1.get_name())
    print(b1.get_minimum_age())
    print(b1.get_number_player())
    print(b2.get_name())
    print(b2.get_minimum_age())
    print(b2.get_number_player())


if __name__ == '__main__':
    main()
