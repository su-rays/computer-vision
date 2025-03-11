from abc import ABC, abstractmethod

# Interface-like abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Concrete class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Usage
circle = Circle(5)
square = Square(4)

print("Circle Area:", circle.area())  # Output: Circle Area: 78.5
print("Square Perimeter:", square.perimeter())  # Output: Square Perimeter: 16