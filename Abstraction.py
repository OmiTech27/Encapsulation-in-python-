from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Create objects of different classes
rectangle = Rectangle(5, 3)
circle = Circle(4)

# Call the area() method on different objects
print("Area of the rectangle:", rectangle.area())
print("Area of the circle:", circle.area())
