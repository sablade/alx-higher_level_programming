#!/usr/bin/python3
""" Rectangle Class with private instance attrubutes """
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        
        self.__width = value
