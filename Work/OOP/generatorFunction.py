#A generator method is a function that uses the yield keyword to produce a series of
#  values lazily (one at a time) instead of computing them all at once and returning 
# them as a list.


def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3


# Using a list
squares = [x**2 for x in range(1000000)]  # Consumes a lot of memory

# Using a generator
squares_gen = (x**2 for x in range(1000000))  # Uses minimal memory



# Inefficient: Loads the entire file into memory
with open("large_file.txt") as f:
    lines = f.readlines()  # Consumes memory for all lines at once
    for line in lines:
        print(line.strip())

# Efficient: Processes one line at a time
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

for line in read_large_file("large_file.txt"):
    print(line)  # Only one line is in memory at a time
