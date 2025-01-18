tpl = (1, 2, 3)
print(tpl[0])  # Access element
print(tpl.count(2))  # Count occurrences of 2
print(tpl.index(3))  # Get index of 3   

my_tuple = (10, 20, 30)
for item in my_tuple:
    print(f"Item: {item}")


#Create a Dictionary from Tuples:
my_tuple = [("name", "Alice"), ("age", 25), ("city", "London")]
my_dict = dict(my_tuple)
print(my_dict)  # {'name': 'Alice', 'age': 25, 'city': 'London'}

#tuples are immutable can not modify them put u can change to list them tuple like tpl = (1, 2, 3)

# Convert to list
tpl_list = list(tpl)

# Add items to the list
tpl_list.append(4)

# Convert back to tuple
tpl = tuple(tpl_list)

print(tpl)  # Output: (1, 2, 3, 4)

