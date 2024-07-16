class Artwork:
    def __init__(self, title, artist, year_creation):
        self.title = title
        self.artist = artist
        self.year_creation = year_creation

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_year_creation(self):
        return self.year_creation

    def show_info(self):
        print(f"titolo: {self.title}, artista: {self.artist}, anno di creazione: {self.year_creation}")


class Painting(Artwork):
    def __init__(self, title, artist, year_creation, technique, dimensions):
        super().__init__(title, artist, year_creation)
        self.technique = technique
        self.dimensions = dimensions

    def get_technique(self):
        return self.technique

    def get_dimensions(self):
        return self.dimensions

    def show_info(self):
        super().show_info()
        print(f"tecnica: {self.technique}, dimensioni: {self.dimensions}")


class Sculpture(Artwork):
    def __init__(self, title, artist, year_creation, material, height):
        super().__init__(title, artist, year_creation)
        self.material = material
        self.height = height

    def get_material(self):
        return self.material

    def get_height(self):
        return self.height

    def show_info(self):
        super().show_info()
        print(f"materiale: {self.material}, altezza: {self.height}")


def main():
    p1 = Painting("Notte Stellata", "Vincent van Gogh", 1889, "olio su tela", "73.7x92.1 cm")
    p2 = Painting("La Gioconda", "Leonardo da Vinci", 1503, "olio su tavola", "77x53 cm")
    s1 = Sculpture("David", "Michelangelo", 1504, "marmo", 517)
    s2 = Sculpture("Il Pensatore", "Auguste Rodin", 1902, "bronzo", 188)

    p1.show_info()
    print()
    p2.show_info()
    print()
    s1.show_info()
    print()
    s2.show_info()
    print()

    print(p1.get_title())
    print(p1.get_artist())
    print(p1.get_year_creation())
    print(p1.get_technique())
    print(p1.get_dimensions())

    print(p2.get_title())
    print(p2.get_artist())
    print(p2.get_year_creation())
    print(p2.get_technique())
    print(p2.get_dimensions())

    print(s1.get_title())
    print(s1.get_artist())
    print(s1.get_year_creation())
    print(s1.get_material())
    print(s1.get_height())

    print(s2.get_title())
    print(s2.get_artist())
    print(s2.get_year_creation())
    print(s2.get_material())
    print(s2.get_height())


if __name__ == '__main__':
    main()
