class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.vote = []

    def get_vote(self):
        return self.vote

    def add_vote(self, v):
        self.vote.append(v)

    def calculate_average(self):
        average = sum(self.vote) / len(self.get_vote())
        return average


def main():
    s = Student("Vittorio", "Tiozzo")
    print(s.get_vote())
    s.add_vote(6)
    s.add_vote(7)
    s.add_vote(8)
    s.add_vote(9)
    s.add_vote(10)
    print(s.get_vote())
    print(s.calculate_average())



if __name__ == '__main__':
    main()