class Student:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_score(self):
        return self.score

    def add_score(self, s):
        self.score += s


def main():
    s = Student("Vittorio")
    print(s.get_score())
    s.add_score(6)
    s.add_score(7)
    s.add_score(8)
    s.add_score(9)
    s.add_score(10)
    print(s.get_score())



if __name__ == '__main__':
    main()