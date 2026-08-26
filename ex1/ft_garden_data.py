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
    plant1 = Plant("Long Leaf", 75, 30)
    plant2 = Plant("Giggle Bush", 62, 42)
    plant3 = Plant("Jazz Cabbage", 42, 420)
    print("==Garden Plant Registry==")
    plant1.show()
    plant2.show()
    plant3.show()
