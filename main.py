class Array:
    def __init__(self):
        self.a = []

    def add_head(self, number):
        self.a.insert(0, number)

    def add_end(self, number):
        self.a.append(number)

    def array_sort(self):
        self.a.sort()

    def number_search(self, number):
        b = []

        for i in self.a:
            if self.a[i] == number:
                b.append(i)

        return b

    def get_array(self):
        return self.a


def main():
    array = Array()
    array.add_end(3)
    array.add_head(1)
    array.add_head(2)
    print(array.get_array())
    array.array_sort()
    print(array.get_array())
    array.add_head(1)
    print(array.number_search(1))


if __name__ == '__main__':
    main()
