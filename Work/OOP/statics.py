class MyClass:
    # Class variable defined in the level of the class and shared for all class instances "inheritance"
    class_variable = 10

    def __init__(self):
        # Instance variable , unique for each instance for that class
        self.instance_variable = 20

    @staticmethod
    def static_method():
        # Static method does not (you can not ) instance variables but can access class variables like
        print("This is a static method." , MyClass.class_variable)

    @classmethod
    def class_method(cls):
        # Class method accesses class variables
        print(f"This is a class method, and class variable is {cls.class_variable}.")
        cls.class_variable += 5

    def non_static_method(self):
        # Instance method can access both class and instance variables
        print(f"This is a non-static method. Class variable is {self.class_variable}, instance variable is {self.instance_variable}.")

# Create an instance of MyClass
my_instance = MyClass()

# Accessing class variable
print(f"Class variable accessed through class: {MyClass.class_variable}")#10
print(f"Class variable accessed through instance: {my_instance.class_variable}")#10

# Accessing instance variable
print(f"Instance variable accessed through instance: {my_instance.instance_variable}")#20

# Calling static method
MyClass.static_method()#10
my_instance.static_method()#10

# Calling class method
MyClass.class_method()#10
my_instance.class_method()#15

# Calling instance method
my_instance.non_static_method() #20, 20