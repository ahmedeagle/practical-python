from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def conceretDescription(self):
        return "I am a concrete method for all shapes"
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c= Circle(5)
print(c.area(), c.conceretDescription())
        
