import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        elif isinstance(other, float) or isinstance(other, int):
            return self.radius == other
        return False

    def get_area(self):
        return math.pi * self.radius ** 2

    def __add__(self, other):
        if isinstance(other, Circle):
            return self.get_area() + other.get_area()


circle1 = Circle(4.6)
circle2 = Circle(4.6)

print(circle1 == circle2)
print(circle1 == 4.6)
print(circle1 == 4.7)
print(circle1 + circle2)
print(circle1 - circle2)
print(circle1 * circle2)
print(circle1 > circle2)
print(circle1 < circle2)
print(repr(circle1))
print(len(circle1))  # hekef
print(circle1)



