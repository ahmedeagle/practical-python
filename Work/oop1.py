class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"
    
    def greetNonInstance(self,name2):
        return self.name , name2

instance = MyClass("John")
print(instance.greetNonInstance('ddff'))
