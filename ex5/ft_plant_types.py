#!/usr/bin/env python3

# Instead of super() we can just use Plant.function()
# but then gotta keep track of class name

class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = 0.0
        self._age = 0
        if not self.set_height(height):
            print(f"{self._name}: Error, height can't be negative")
        if not self.set_age(age):
            print(f"{self._name}: Error, age can't be negative")

    def set_height(self, height):
        if height < 0:
            return False
        self._height = float(height)
        return True

    def set_age(self, age):
        if age < 0:
            return False
        self._age = age
        return True

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def grow(self, amount):
        self.set_height(self._height + amount)

    def age(self, days):
        self.set_age(self._age + days)

    def show(self):
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color

    def bloom(self):
        print(f"{self._name} is blooming with {self._color} flowers!")

    def show(self):
        super().show()
        print(f"  Type: Flower, Color: {self._color}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self._name} produces shade \
        with its {self._trunk_diameter}cm trunk.")

    def show(self):
        super().show()
        print(f"  Type: Tree, Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def age(self, days):
        super().age(days)
        self._nutritional_value += days

    def grow(self, amount):
        super().grow(amount)
        self._nutritional_value += int(amount)

    def show(self):
        super().show()
        print(
            f"  Type: Vegetable, Harvest: {self._harvest_season}, \
            Nutrition: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flower = Flower("Rose", 25, 30, "red")
    tree = Tree("Oak", 200, 3650, 40)
    veggie = Vegetable("Carrot", 15, 10, "autumn")

    flower.show()
    tree.show()
    veggie.show()

    print()
    flower.bloom()
    tree.produce_shade()

    print()
    print("Growing and aging the vegetable...")
    veggie.age(5)
    veggie.grow(3)
    veggie.show()
