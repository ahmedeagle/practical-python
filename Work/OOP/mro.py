class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):

    def __init__(self, name):
        self.name = name 

    def showName(self):
        print(self.name)        

# Creating an instance of D
d = D("Emam")
print(d.greet())
d.showName()
