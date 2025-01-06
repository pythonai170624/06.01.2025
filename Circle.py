import math
from argparse import ArgumentError
import shelve

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
        if not isinstance(other, Circle):
            raise ArgumentError("cannot add circle with non-circle")
        if isinstance(other, Circle):
            # return self.get_area() + other.get_area()
            return Circle(self.radius + other.radius)


circle1 = Circle(4.6)
circle2 = Circle(4.6)
circle3 = circle1 + circle2

print(circle3.radius)
sh = shelve.open('data.db')
sh['circle3'] = circle3
circle3 = sh.get('circle3')
print('circle3', circle3.radius)
sh.close()

print(circle1 == circle2)
print(circle1 == 4.6)
print(circle1 == 4.7)
print(circle1 + circle2)
print(circle1 - circle2)
print(circle1 * circle2)
print(circle1.isbigger(circle2))
print(circle1 > circle2)
# [1,2] + [3]  __add__
# {1,2} & {3}
print(circle1 < circle2)
print(repr(circle1))
print(len(circle1))  # hekef
print(circle1)



