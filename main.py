class MusicalInstrument:
    def __init__(self, name, typee):
        self.name = name
        self.typee = typee

    def get_name(self):
        return self.name

    def get_typee(self):
        return self.typee

    def show_info(self):
        print(f"Nome: {self.name}, tipo: {self.typee}")


class Guitar(MusicalInstrument):
    def __init__(self, name, ropes):
        super().__init__(name, "A corda")
        self.ropes = ropes

    def get_ropes(self):
        return self.ropes

    def show_info(self):
        super().show_info()
        print(f"Corde': {self.ropes}")


class Piano(MusicalInstrument):
    def __init__(self, name, number_keys):
        super().__init__(name, "A tastiera")
        self.number_keys = number_keys

    def get_number_keys(self):
        return self.number_keys

    def show_info(self):
        super().show_info()
        print(f"Numero tasti: {self.number_keys}")


def main():
    g = Guitar("Fender Stratocaster", 6)
    p = Piano("Yamaha U3", 88)
    g.show_info()
    print()
    p.show_info()

    print()
    print(g.get_name())
    print(g.get_typee())
    print(g.get_ropes())
    print(p.get_name())
    print(p.get_typee())
    print(p.get_number_keys())


if __name__ == '__main__':
    main()
