class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def __str__(self):
        return f"Nome: {self.name}, Punteggio: {self.score}"




if __name__ == '__main__':
    s = Student("Vittorio", 9)
    print(s.getName())
    print(s.getScore())
    print(Student("Vittorio", 9))