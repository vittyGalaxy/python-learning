class Student:
    def __init__(self, name, surname, vote):
        self.name = name
        self.surname = surname
        self.vote = vote

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getVote(self):
        return self.vote

    def calculate_average(self):
        average = sum(self.vote) / len(self.getVote())
        return average



if __name__ == '__main__':
    s = Student("Vittorio", "Tiozzo", [6, 7, 8, 9, 10])
    print(s.getName())
    print(s.getSurname())
    print(s.getVote())
    print(s.calculate_average())