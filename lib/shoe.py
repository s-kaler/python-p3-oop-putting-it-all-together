#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = "Adidas", size = 1):
        self.brand = brand
        if isinstance(size, int):
            self.size = size
        else:
            print("size must be an integer")
    
    def get_brand(self):
        return self._brand
    
    def set_brand(self, brand):
        self._brand = brand

    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

    condition = 'Old'

    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")