class Name:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Il mio nome e' " + self.name

if __name__ == '__main__':
    a = Name("Vittorio")
    print(a)