class Film:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

    def getTitle(self):
        return self.title

    def getYear(self):
        return self.year

    def getGenre(self):
        return self.genre

    def __str__(self):
        return f"Titolo: {self.title}, Anno: {self.year}, Genere: {self.genre}"




if __name__ == '__main__':
    f = Film("Inception", 2010,"Fantascienza")
    print(f.getTitle())
    print(f.getYear())
    print(f.getGenre())
    print(Film("Inception", 2010,"Fantascienza"))