# String: He said Hello!
text = "He said Hello!"

# String: He said "Hello!" (double quote in string -> use \")
text = "He said \"Hello!\""

# Multi-line strings
multiline_str = """This is a string
that spans across
multiple lines."""

# Convert number to string
num_str = str(100)  # "100"

# Indexing
text = "Python Programming"
print(text[0])    # 'P'
print(text[-1])   # 'g'

# Slicing
print(text[0:6])     # 'Python'
print(text[7:])      # 'Programming'
print(text[::-1])    # 'gnimmargorP nohtyP'

# Immutability (error when doing below)
text = "Hello"
text[0] = "J"        # Error, cant assign

# Concate string
new_text = "J" + text[1:]  # "J" + "ello" -> "Jello"

# String method
msg = "hello Python world"
print(msg.upper())          # 'HELLO PYTHON WORLD'
print(msg.lower())          # 'hello python world'
print(msg.title())          # 'Hello Python World'
print(msg.capitalize())     # 'Hello python world'

# Trimming
text = "   python programming   "
print(text.strip())         # 'python programming'

# Replace
text = "   python programming   "
text.replace("python", "Java")    # '   Java programming   '

# Splitting
raw_data = "apple,banana,cherry"
fruit_list = raw_data.split(",")   # ['apple', 'banana', 'cherry']

# Joining
new_string = "-".join(fruit_list)
print(new_string)                  # 'apple-banana-cherry'

# Python3 f-string
name = "Alice"
message = f"Hello, my name is {name}"    # 'Hello, my name is Alice'

# Rounding floating numbers f-string
price = 49.9987
print(f"Price: ${price:.2f}")            # 'Price: $50.00'

# Checking String Contents
text = "Python123"
print("Py" in text)           # True

print(text.isalpha())         # False
print(text.isalnum())         # True
print(text.isdigit())         # False
print(text.startswith("Py"))  # True
print(text.endswith("123"))   # True
