# Create a set with initial elements
fruits = {"apple", "orange", "banana"}

# Create a set from a List, Tuple, Set
numbers = set([1, 2, 2, 3, 4, 4, 4]) 
# -> {1, 2, 3, 4}

# Create an empty set, not empty_set = {}
empty_set = set()

fruits.add("mango")

fruits.update(["grape", "watermelon"])

fruits.discard("apple")

fruits.remove("orange")  # Raises a KeyError

fruits.clear()

# Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print(A | B)        # {1, 2, 3, 4, 5, 6}

# Intersection
print(A & B)        # {3, 4}

# Difference
print(A - B)        # {1, 2}

# Symmetric Difference
print(A ^ B)        # {1, 2, 5, 6}

