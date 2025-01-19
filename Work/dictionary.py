my_dict = {"name": "Alice", "age": 25, "city": "London"}
for key in my_dict:
    print(f"Key: {key}")

for value in my_dict.values():
    print(f"Value: {value}")    


for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")    

#Create a Dictionary from Tuples:
tuples = [("name", "Alice"), ("age", 25), ("city", "London")]
my_dict = dict(tuples)
print(my_dict)  # {'name': 'Alice', 'age': 25, 'city': 'London'}    


d = {"name": "Alice", "age": 25}
d["city"] = "London"  # Add key-value pair
print(d.keys())  # Get keys
print(d.values())  # Get values
print(d.items())  # Get key-value pairs


#Dictionary Comprehension from two lists:
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = {key: value for key, value in zip(keys, values)}
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}