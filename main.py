class Dish:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_ingredients(self):
        return self.ingredients

    def show_info(self):
        ingredients_str = ', '.join(self.ingredients)
        print(f"nome: {self.name}, prezzo: {self.price:.2f}, ingredienti: {ingredients_str}")


class Appetizers(Dish):
    def __init__(self, name, price, ingredients, calories):
        super().__init__(name, price, ingredients)
        self.calories = calories

    def get_calories(self):
        return self.calories

    def show_info(self):
        super().show_info()
        print(f"calories: {self.calories}")


class MainCourse(Dish):
    def __init__(self, name, price, ingredients, cooking_time):
        super().__init__(name, price, ingredients)
        self.cooking_time = cooking_time

    def get_cooking_time(self):
        return self.cooking_time

    def show_info(self):
        super().show_info()
        print(f"tempo cottura: {self.cooking_time}")

class Dessert(Dish):
    def __init__(self, name, price, ingredients, contains_sugar):
        super().__init__(name, price, ingredients)
        self.contains_sugar = contains_sugar

    def get_contains_sugar(self):
        return self.contains_sugar

    def show_info(self):
        super().show_info()
        if self.contains_sugar:
            sugar_str = "Si"

        else:
            sugar_str = "No"
        print(f"contiene zucchero: {sugar_str}")


def main():
    a1 = Appetizers("Bruschetta", 5.0, ["pane", "pomodoro", "basilico"], 150)
    a2 = Appetizers("Carpaccio di manzo", 10.0, ["manzo", "rucola", "parmigiano"], 200)

    m1 = MainCourse("Lasagna", 12.0, ["pasta", "carne", "besciamella"], 40)
    m2 = MainCourse("Bistecca alla Fiorentina", 25.0, ["bistecca", "olio", "rosmarino"], 15)

    d1 = Dessert("Tiramisù", 6.0, ["mascarpone", "caffè", "savoiardi"], True)
    d2 = Dessert("Macedonia", 4.0, ["frutta", "succo di limone"], False)

    appetizers = [a1, a2]
    for a in appetizers:
        a.show_info()
        print(a.get_name())
        print(a.get_price())
        print(a.get_ingredients())
        print(a.get_calories())

    main_course = [m1, m2]
    for m in main_course:
        m.show_info()
        print(m.get_name())
        print(m.get_price())
        print(m.get_ingredients())
        print(m.get_cooking_time())

    dessert = [d1, d2]
    for d in dessert:
        d.show_info()
        print(d.get_name())
        print(d.get_price())
        print(d.get_ingredients())
        print(d.get_contains_sugar())


if __name__ == '__main__':
    main()
