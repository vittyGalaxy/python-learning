class Show:
    def __init__(self, title, date, duration):
        self.title = title
        self.date = date
        self.duration = duration

    def get_title(self):
        return self.title

    def get_date(self):
        return self.date

    def get_duration(self):
        return self.duration

    def show_info(self):
        print(f"titolo: {self.title}, data: {self.date}, durata: {self.duration}")


class Concert(Show):
    def __init__(self, title, date, duration, artist, genre):
        super().__init__(title, date, duration)
        self.artist = artist
        self.genre = genre

    def get_artist(self):
        return self.artist

    def get_genre(self):
        return self.genre

    def show_info(self):
        super().show_info()
        print(f"artista: {self.artist}, genere: {self.genre}")


class OperaTheatrical(Show):
    def __init__(self, title, date, duration, director, cast):
        super().__init__(title, date, duration)
        self.director = director
        self.cast = cast

    def get_director(self):
        return self.director

    def get_cast(self):
        return self.cast

    def show_info(self):
        super().show_info()
        cast_str = ', '.join(self.cast)
        print(f"regista: {self.director}, cast: {cast_str}")


class Film(Show):
    def __init__(self, title, date, duration, director, rating):
        super().__init__(title, date, duration)
        self.director = director
        self.rating = rating

    def get_director(self):
        return self.director

    def get_rating(self):
        return self.rating

    def show_info(self):
        super().show_info()
        print(f"regista: {self.director}, valutazione: {self.rating}")


def main():
    c1 = Concert("Concerto di Beethoven", "2023-10-15", 120, "Orchestra Sinfonica", "Classica")
    c2 = Concert("Rock Night", "2023-11-01", 150, "The Rockers", "Rock")

    o1 = OperaTheatrical("Amleto", "2023-09-20", 180, "Giovanni Rossi", ["Marco Bianchi", "Luca Verdi"])
    o2 = OperaTheatrical("La Traviata", "2023-10-10", 160, "Maria Neri", ["Anna Rossi", "Francesco Gialli"])

    f1 = Film("Inception", "2023-12-05", 148, "Christopher Nolan", "PG-13")
    f2 = Film("Il Padrino", "2023-12-12", 175, "Francis Ford Coppola", "R")

    concert = [c1, c2]
    for c in concert:
        c.show_info()
        print(c.get_title())
        print(c.get_date())
        print(c.get_duration())
        print(c.get_artist())
        print(c.get_genre())

    opera_theatrical = [o1, o2]
    for o in opera_theatrical:
        o.show_info()
        print(o.get_title())
        print(o.get_date())
        print(o.get_duration())
        print(o.get_director())
        print(o.get_cast())

    film = [f1, f2]
    for f in film:
        f.show_info()
        print(f.get_title())
        print(f.get_date())
        print(f.get_duration())
        print(f.get_director())
        print(f.get_rating())


if __name__ == '__main__':
    main()
