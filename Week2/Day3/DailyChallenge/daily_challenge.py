import turtle
import random

class Circle:

    _pi = 3.14159

    def __init__(self, radius=1.0, diameter=None):
        if diameter is not None:
            self.radius = diameter / 2
        else:
            self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __ne__(self, other):
        return self.radius != other.radius

    def __ge__(self, other):
        return self.radius >= other.radius
    
    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius
    

def display_crcles(t, circles, scale=10):
    for circle in circles:
        t.circle(circle.radius * scale)

c1 = Circle(radius=5)
c2 = Circle(diameter=12)

print(c1 + c2)
print(c1 > c2)
print(c1 == c2)
print(c1 == c1)

circles = [Circle(random.randint(1, 10)) for _ in range(6)]

print(circles)
circles = sorted(circles)
print(circles)

t = turtle.Turtle()
display_crcles(t, circles)