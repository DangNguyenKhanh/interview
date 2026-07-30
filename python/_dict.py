# Create a dictionary with initial key-value pairs
user = {
    "name": "Alice",
    "age": 25,
    "email": "alice@gmail.com",
    "is_active": True
}

# Create an empty dictionary
empty_dict = {}
empty_dict_2 = dict()

# Access by key
user = {"name": "Alice", "age": 25}
print(user["name"])  # 'Alice'

print(user.get("age"))             # 25
print(user.get("phone"))           # None
print(user.get("phone", "N/A"))    # 'N/A'

# Update value by key
user["age"] = 26
user["phone"] = "123-456-789"      # Add new key

# Removing item by key
student = {"id": 101, "name": "Bob", "grade": "A", "age": 20}
grade = student.pop("grade")  # 'A'

last_item = student.popitem()  # last_item = ('age', 20)

del student["id"]

student.clear()  # {}

# Iterating
scores = {"Math": 90, "English": 85, "Physics": 92}
for subject in scores.keys():
    print(subject) # Math, English, Physics

for score in scores.values():
    print(score) # 90, 85, 92

for subject, score in scores.items():
    print(f"{subject}: {score}")

# Comprehension
squares = {x: x**2 for x in range(1, 5)}  # {1: 1, 2: 4, 3: 9, 4: 16}

all_scores = {"Alice": 85, "Bob": 42, "Charlie": 68}
passed = {name: score for name, score in all_scores.items() if score >= 50}

# 'in' operator
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Keys
print("name" in student)                    # True    O(1)
print("name" in student.keys())             # True    O(1)
print("Alice" in student.values())          # True    O(n)
print(("name", "Bob") in student.items())   # False   O(n)

