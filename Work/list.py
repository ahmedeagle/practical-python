my_list = [10, 20, 30]
for item in my_list:
    print(f"Item: {item}")

lst = [3, 1, 4, 1, 5]
lst.append(9)  # Add an element
lst.sort()  # Sort the list
lst.pop()  # Remove last element
print(lst[::-1])  # Reverse the list
print(len(lst))  # Length of the list    

lst = [5, 2, 9, 1]
lst.sort()  # In-place sort
sorted_lst = sorted(lst)  # New sorted list

#Index and Elements:
for index, item in enumerate(my_list):
    print(f"Index: {index}, Item: {item}")


#List Comprehension:
squares = [x**2 for x in range(10)]