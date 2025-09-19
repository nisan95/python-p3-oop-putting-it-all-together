#!/usr/bin/env python3

class Shoe:

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"

    # Brand property
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Brand must be a non-empty string")
        self._brand = value.strip()

    # Size property
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
        else:
            self._size = size

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")