
#like traits in php
# similar to multiple inheritance but 
# Mixins in Python: Mixins serve a similar purpose, adding specific methods or functionality to a class without full inheritance. They're meant to provide specific behavior to a class but are not intended to be instantiated on their own.
# n PHP, when there is a conflict between methods in different traits, you can use insteadof to resolve conflicts.
#In Python, method resolution order (MRO) is used to determine which method to call if there are conflicting methods in multiple mixins. 
class Flyable:
    def fly(self):
        print("Flying")

class Animal():
    def move(self):
        print("Moving")

class Bird(Animal, Flyable):
  pass

bird = Bird()
bird.move()  # Output: Moving
bird.fly()   # Output: Flying
