class PortableDevice:
    def __init__(self, brand, model, battery_capacity, screen_size, internal_memory):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity
        self.screen_size = screen_size
        self.internal_memory = internal_memory

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_battery_capacity(self):
        return self.battery_capacity

    def get_screen_size(self):
        return self.screen_size

    def get_internal_memory(self):
        return self.internal_memory

    def show_info(self):
        print(f"marca: {self.brand}, modello: {self.model}, capacita batteria: {self.battery_capacity}, dimensione schermo: {self.screen_size}, memoria interna: {self.internal_memory}")


class Smartphone(PortableDevice):
    def __init__(self, brand, model, battery_capacity, screen_size, internal_memory, camera_megapixel):
        super().__init__(brand, model, battery_capacity, screen_size, internal_memory)
        self.camera_megapixel = camera_megapixel

    def get_camera_megapixel(self):
        return self.camera_megapixel

    def show_info(self):
        super().show_info()
        print(f"camera megapixel: {self.camera_megapixel}")


class Tablet(PortableDevice):
    def __init__(self, brand, model, battery_capacity, screen_size, internal_memory, pen_support):
        super().__init__(brand, model, battery_capacity, screen_size, internal_memory)
        self.pen_support = pen_support

    def get_pen_support(self):
        return self.pen_support

    def show_info(self):
        super().show_info()
        if self.pen_support:
            self.pen_support = "Si, c'e' la penna"

        else:
            self.pen_support = "No, non c'e' la penna"
        print(f"supporto penna: {self.pen_support}")


def main():
    s1 = Smartphone("Apple", "iPhone 14", 3095, 6.1, 128, 12)
    s2 = Smartphone("Samsung", "Galaxy S23", 3900, 6.8, 256, 50)
    t1 = Tablet("Microsoft", "Surface Pro 9", 5670, 12.3, 256, True)
    t2 = Tablet("Samsung", "Galaxy Tab S9", 8000, 11.0, 128, False)

    s1.show_info()
    print()
    s2.show_info()
    print()
    t1.show_info()
    print()
    t2.show_info()
    print()


    print(s1.get_brand())
    print(s1.get_model())
    print(s1.get_screen_size())
    print(s1.get_internal_memory())
    print(s1.get_camera_megapixel())
    print(s1.get_battery_capacity())

    print(s2.get_brand())
    print(s2.get_model())
    print(s2.get_screen_size())
    print(s2.get_internal_memory())
    print(s2.get_camera_megapixel())
    print(s2.get_battery_capacity())

    print(t1.get_brand())
    print(t1.get_model())
    print(t1.get_battery_capacity())
    print(t1.get_pen_support())
    print(t1.get_screen_size())
    print(t1.get_internal_memory())

    print(t2.get_brand())
    print(t2.get_model())
    print(t2.get_battery_capacity())
    print(t2.get_pen_support())
    print(t2.screen_size)
    print(t2.internal_memory)


if __name__ == '__main__':
    main()
