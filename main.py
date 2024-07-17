class Attraction:
    def __init__(self, name, minimum_height, capacity, duration):
        self.name = name
        self.minimum_height = minimum_height
        self.capacity = capacity
        self.duration = duration

    def get_name(self):
        return self.name

    def get_minimum_height(self):
        return self.minimum_height

    def get_capacity(self):
        return self.capacity

    def get_duration(self):
        return self.duration

    def show_info(self):
        print(f"nome: {self.name}, altezza minima: {self.minimum_height}, capacita': {self.capacity}, durata: {self.duration}")


class Carousel(Attraction):
    def __init__(self, name, minimum_height, capacity, duration, number_of_laps, type_of_ride):
        super().__init__(name, minimum_height, capacity, duration)
        self.number_of_laps = number_of_laps
        self.type_of_ride = type_of_ride

    def get_number_of_laps(self):
        return self.number_of_laps

    def get_type_of_ride(self):
        return self.type_of_ride

    def show_info(self):
        super().show_info()
        print(f"numero di giri: {self.number_of_laps}, tipo di giostra: {self.type_of_ride}")


class RollerCoaster(Attraction):
    def __init__(self, name, minimum_height, capacity, duration, max_speed, number_inversions):
        super().__init__(name, minimum_height, capacity, duration)
        self.max_speed = max_speed
        self.number_inversions = number_inversions

    def get_max_speed(self):
        return self.max_speed

    def get_number_inversions(self):
        return self.number_inversions

    def show_info(self):
        super().show_info()
        print(f"velocita' max: {self.max_speed}, numero di inversioni: {self.number_inversions}")


class FerrisWheel(Attraction):
    def __init__(self, name, minimum_height, capacity, duration, height, number_of_cabins):
        super().__init__(name, minimum_height, capacity, duration)
        self.height = height
        self.number_of_cabins = number_of_cabins

    def get_height(self):
        return self.height

    def get_number_of_cabins(self):
        return self.number_of_cabins

    def show_info(self):
        super().show_info()
        print(f"altezza: {self.height}, numero di cabine: {self.number_of_cabins}")


def main():
    c1 = Carousel("Carousel Fantasia", 90, 20, 5, 10, "carousel")
    c2 = Carousel("Disco Magico", 120, 15, 7, 5, "disco")

    r1 = RollerCoaster("Vertigo", 140, 30, 3, 100, 5)
    r2 = RollerCoaster("Thunderbolt", 160, 40, 4, 120, 8)

    f1 = FerrisWheel("Sky View", 110, 40, 15, 50, 20)
    f2 = FerrisWheel("Star Ferris", 100, 30, 12, 45, 15)

    carousel = [c1, c2]
    for c in carousel:
        c.show_info()
        print(c.get_name())
        print(c.get_minimum_height())
        print(c.get_capacity())
        print(c.get_duration())
        print(c.get_number_of_laps())
        print(c.get_type_of_ride())

    rollerCoaster = [r1, r2]
    for r in rollerCoaster:
        r.show_info()
        print(r.get_name())
        print(r.get_minimum_height())
        print(r.get_capacity())
        print(r.get_duration())
        print(r.get_max_speed())
        print(r.get_number_inversions())

    ferris_wheel = [f1, f2]
    for f in ferris_wheel:
        f.show_info()
        print(f.get_name())
        print(f.get_minimum_height())
        print(f.get_capacity())
        print(f.get_duration())
        print(f.get_height())
        print(f.get_number_of_cabins())


if __name__ == '__main__':
    main()
