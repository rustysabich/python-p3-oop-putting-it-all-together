#!/usr/bin/env python3

class Book:
    
    # define attributes
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        
    # define page_count as property
    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")
       
    # compile the getter and setter methods of page_count attribute 
    page_count = property(get_page_count, set_page_count)
    
    ### methods ###
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        