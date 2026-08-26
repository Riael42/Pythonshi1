#!/usr/bin/env python3

class Plant:
    class Statistics:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self):
            self._grow_calls += 1

        def record_age(self):
            self._age_calls += 1

        def record_show(self):
            self._show_calls += 1

        def display(self):
            print(f"    grow() calls: {self._grow_calls}")
            print(f"    age() calls: {self._age_calls}")
            print(f"    show() calls: {self._show_calls}")

    @staticmethod
    def is_older_than_a_year(age):
        return age > 365

    @classmethod
    def create_anonymous(cls, height=0, age=0):
        return cls("Anonymous", height, age)

    def __init__(self, name, height, age):
        self._name = name
        self._height = 0.0
        self._age = 0
        self._stats = self.Statistics()
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

    def get_name(self):
        return self._name

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def grow(self, amount):
        self.set_height(self._height + amount)
        self._stats.record_grow()

    def age(self, days):
        self.set_age(self._age + days)
        self._stats.record_age()

    def show(self):
        self._stats.record_show()
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def show_stats(self):
        print(f"Statistics for {self._name}:")
        self._stats.display()


class Flower(Plant):
    class Statistics(Plant.Statistics):
        pass

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color

    def bloom(self):
        print(f"{self._name} is blooming with {self._color} flowers!")

    def show(self):
        super().show()
        print(f"  Type: Flower, Color: {self._color}")


class Tree(Plant):
    class Statistics(Plant.Statistics):
        def __init__(self):
            super().__init__()
            self._shade_calls = 0

        def record_shade(self):
            self._shade_calls += 1

        def display(self):
            super().display()
            print(f"    produce_shade() calls: {self._shade_calls}")

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        self._stats.record_shade()
        print(f"{self._name} produces shade with \
        its {self._trunk_diameter}cm trunk.")

    def show(self):
        super().show()
        print(f"  Type: Tree, Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    class Statistics(Plant.Statistics):
        pass

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


class Seed(Flower):
    class Statistics(Flower.Statistics):
        pass

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self):
        super().bloom()
        self._seeds = 10
        print(f"{self._name} produced {self._seeds} seeds.")

    def show(self):
        super().show()
        print(f"  Type: Seed, Seeds: {self._seeds}")


def display_garden_stats(plant):
    print("=== Garden Analytics Report ===")
    plant.show()
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden Analytics ===")

    flower = Flower("Rose", 25, 30, "red")
    tree = Tree("Oak", 200, 4000, 40)
    veggie = Vegetable("Carrot", 15, 10, "autumn")
    seed = Seed("Tulip", 20, 50, "yellow")
    anon = Plant.create_anonymous(10, 5)

    flower.grow(5)
    tree.age(10)
    tree.produce_shade()
    veggie.grow(3)
    veggie.age(5)
    seed.bloom()

    print(f"Is Oak older than a year? \
        {Plant.is_older_than_a_year(tree.get_age())}")
    print(f"Is Rose older than a year? \
        {Plant.is_older_than_a_year(flower.get_age())}")
    print()

    for plant in (flower, tree, veggie, seed, anon):
        display_garden_stats(plant)
        print()
