class Color:
    def __init__(self, red, green, blu):
        self.red = red
        self.green = green
        self.blu = blu

    def __repr__(self):
        return "Colore in RGB = {red}, {green}, {blu}".format(red = self.red, green = self.green, blu = self.blu)

    def __add__(self, other):
        new_red = min(self.red + other.red, 255)
        new_green = min(self.green + other.green, 255)
        new_blu = min(self.blu + other.blu, 255)
        return Color(new_red, new_green, new_blu)


if __name__ == '__main__':
    red = Color(255, 0,0)
    green = Color(0, 255,0)

    yellow = red + green
    print(yellow)