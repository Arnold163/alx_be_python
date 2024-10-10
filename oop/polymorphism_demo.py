#polymorphism the ability of an object to take on many forms
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

class Circle(Shape):    
    def __init__(self, radius):
        self.radius = radius    

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
def main():
    shapes =[
        Circle(7),
        Rectangle(10, 5)
    ]

    for shape in shapes:
        print(f"The area is {shape.area()}")

if __name__ == "__main__":
    main()