#!/usr/bin/env python3

class Shoe:
    
    # initialize attributes
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        
    # define size attribute as a property
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")
            
    # compile the getter and setter methods
    size = property(get_size, set_size)
    
    ### methods ###
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'