class Salad:
    admin = False
    def __init__(self, tomatoes, onion, beans):
        self.tomatoes = tomatoes
        self.onion = onion
        self.beans = beans


class SaladTop(Salad):
    def __init__(self, tomatoes, onion, beans):
        super().__init__(tomatoes, onion, beans)
        self.garlic = True

if __name__ == '__main__':
