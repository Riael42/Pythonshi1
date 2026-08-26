#!/usr/bin/env python3

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

    def show(self):
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15, 10)
    print(f"Plant created: {rose._name}: {rose.get_height()}cm, \
    {rose.get_age()} days old")

    if rose.set_height(25):
        print("Height updated: 25cm")
    if rose.set_age(30):
        print("Age updated: 30 days")

    if not rose.set_height(-5):
        print(f"{rose._name}: Error, height can't be negative")
        print("Height update rejected")

    if not rose.set_age(-3):
        print(f"{rose._name}: Error, age can't be negative")
        print("Age update rejected")

    print(
        f"Current state: {rose._name}: {rose.get_height()}cm, \
        {rose.get_age()} days old")
