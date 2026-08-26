#!/usr/bin/env python3

class Plant:
    # class definition with attributes
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    # class method to print the aforementioned attributes
    def show(self):
        print(f"{self.name}: {self.height} cm, {self.age} days old")

    # class method to grow height of plant
    def grow(self, growth):
        self.height += growth

    # class method to age up the plant
    def age_up(self, days):
        self.age += days


if __name__ == "__main__":
    plant1 = Plant("Long Leaf", 10, 5)
    plant1.show()
    init_height = plant1.height
    init_age = plant1.age
    for i in range(1, 8, 1):
        plant1.grow(2)
        plant1.age_up(1)
        print(f"Day {i}: Height: {plant1.height} cm, Age: {plant1.age} days")
    fina_height = plant1.height
    fina_age = plant1.age
    print(f"Initial Height: {init_height} cm, Initial Age: {init_age}")
    print(f"  Final Height: {fina_height} cm, Final Age: {fina_age}")
