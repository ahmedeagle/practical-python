#The methods like __len__, __getitem__, __setitem__, and __delitem__ a
# re special or magic methods in Python. They allow you to define or 
# customize the behavior of your objects when they are used with common operators
#  or built-in functions, such as len(), indexing, assignment, and deletion.

#Here’s the point of these methods: they provide a way for your custom classes
#  to emulate Python's built-in types (like lists, dictionaries, and tuples) by
#  defining their expected behavior.

# in short it enables you to use built in methods in your logic

class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

my_list = MyList([10, 20, 30])


my_list[1]=100
print(my_list.data)  # Output: 20    
print(MyList.data)   # error can not call instance variable by class name
print(my_list[1])  # Output: 20
