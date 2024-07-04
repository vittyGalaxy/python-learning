class Circle:
    pi = 3.14

    def area(self, radius):
        return Circle.pi * (radius ** 2)



if __name__ == '__main__':
    circle = Circle()

    fountain = circle.area(30)

    print(fountain)