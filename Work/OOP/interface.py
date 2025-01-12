from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.1416 * self.__radius * self.__radius

    def perimeter(self):
        return 2 * 3.1416 * self.__radius    

class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)           
    

r = Rectangle(10, 20)
print(r.area())

c = Circle(10)
print(c.area())
