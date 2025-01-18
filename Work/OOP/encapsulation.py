# Encapsulation Basics in Python
# Encapsulation refers to restricting access to certain parts of an object’s data and behavior, providing controlled access through methods.

# Python’s Approach
# Public Members:

# Accessible anywhere.
# No special syntax is required.

# class MyClass:
#     def __init__(self):
#         self.public_var = "I am public"

# obj = MyClass()
# print(obj.public_var)  # Output: I am public
# Protected Members:

# Indicated by a single underscore (_) prefix.
# By convention, _protected_var signals that the attribute should only be accessed within the class or its subclasses.
# It’s not strictly enforced, but it communicates intent.

# class MyClass:
#     def __init__(self):
#         self._protected_var = "I am protected"

# obj = MyClass()
# print(obj._protected_var)  # Output: I am protected (still accessible)
# Private Members:

# Indicated by a double underscore (__) prefix.
# Python performs name mangling, making the attribute harder to access from outside the class.
# It’s not fully private but adds an extra layer of protection.
# 

# class MyClass:
#     def __init__(self):
#         self.__private_var = "I am private"

# obj = MyClass()
# # print(obj.__private_var)  # AttributeError: 'MyClass' object has no attribute '__private_var'
# print(obj._MyClass__private_var)  # Output: I am private (name mangling)
# Why Python’s Approach?
# Trust Developers:

# Python assumes that developers know what they’re doing.
# You can still access "private" or "protected" attributes if absolutely necessary.
# Simplicity:

# Strict encapsulation requires additional syntax and complexity. Python values simplicity and clarity.
# Flexibility:

# Encapsulation is there to signal intent rather than enforce strict rules.


#Example: Using Properties for Encapsulation

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property  #we can simply make this fuctions as data attribute 
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
#Normal attribute access now triggers the getter and setter methods under @property and @shares.setter.

s = Stock('IBM', 50, 91.1)
s.shares         # Triggers @property
