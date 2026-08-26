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


if __name__ == "__main__":
    plants = [
        Plant("Long Leaf", 75, 30),
        Plant("Giggle Bush", 62, 42),
        Plant("Jazz Cabbage", 42, 420),
        Plant("Funky Fern", 15, 15),
        Plant("Silly Sprout", 5, 5),
    ]

    print("==Garden Plant Factory==")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
