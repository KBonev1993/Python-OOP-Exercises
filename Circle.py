class Circle:
    pi = 3.14


    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return circle.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * circle.pi * self.radius

circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
