from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass




class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_perimeter(self):
        return 2 * pi * self.r

    def calculate_area(self):
        return pi * self.r ** 2


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    def calculate_area(self):
        return self.height * self.width


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
