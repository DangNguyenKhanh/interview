numbers = [10, 20, 30, 40]

person = ["Alice", 25, 1.75, True]

empty_list = []

empty_list_2 = list()

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing
print(fruits[0])
print(fruits[2])

# Negative indexing
print(fruits[-1])

# List slicing: [start:stop:step]
print(fruits[1:4])   # ['banana', 'cherry', 'date']
print(fruits[:3])    # ['apple', 'banana', 'cherry']

# Reversed list
print(fruits[::-1])  # ['elderberry', 'date', 'cherry', 'banana', 'apple']

fruits = ["apple", "banana"]
fruits.append("cherry")             # ['apple', 'banana', 'cherry']
fruits.insert(1, "mango")           # ['apple', 'mango', 'banana', 'cherry']
fruits.extend(["orange", "grape"])  # ['apple', 'mango', 'banana', 'cherry', 'orange', 'grape']

items = ["apple", "banana", "cherry", "banana", "date"]
items.remove("banana")      # ['apple', 'cherry', 'banana', 'date']

# Index removing (return value)
removed_item = items.pop(1) # ['apple', 'banana', 'date']

# Index removing (not return value)
del items[0]
del items

# Clear to empty list
items.clear()

# Built-in function combine with list
numbers = [5, 2, 9, 1, 5, 6]

print(len(numbers))         # Output: 6

print(numbers.count(5))     # Output: 2

print(numbers.index(9))     # Output: 2

numbers.sort()              
print(numbers)              # Output: [1, 2, 5, 5, 6, 9]

numbers.sort(reverse=True)  
print(numbers)              # Output: [9, 6, 5, 5, 2, 1]

original = [3, 1, 2]
new_list = sorted(original)

# List Comprehension
squares = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]

names = ["alice", "bob", "charlie"]
uppercase_names = [name.upper() for name in names] # ['ALICE', 'BOB', 'CHARLIE']






