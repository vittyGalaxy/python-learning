class Counter:
    def __init__(self, counter):
        print("Contero' +1 alla volta")
        self.counter = counter

    def increase(self):
        self.counter += 1
        return self.counter

if __name__ == '__main__':

    c = Counter(0)
    print(c.increase())
    print(c.increase())
    print(c.increase())
