class Counter:
    def __init__(self):
        self.c = 0

    # getter
    def get_counter(self):
        return self.c

    # setter
    def set_counter(self, number):
        self.c = number

    def increment(self):
        self.c += 1

    def decrement(self):
        self.c -= 1


def main():
    counter = Counter()
    print(counter.get_counter())
    counter.increment()
    print(counter.get_counter())
    counter.decrement()
    print(counter.get_counter())
    counter.set_counter(3)
    print(counter.get_counter())
    counter.increment()
    print(counter.get_counter())
    counter.decrement()
    print(counter.get_counter())
    counter.decrement()
    print(counter.get_counter())
    counter.decrement()
    print(counter.get_counter())
    counter.decrement()
    print(counter.get_counter())


if __name__ == '__main__':
    main()
