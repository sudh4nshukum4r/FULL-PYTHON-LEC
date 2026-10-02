# 1. WHAT IS STRING IN PYTHON?

#  A string is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.
# A string can be created by enclosing characters in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# In Python, strings are immutable, which means that once a string is created, it cannot be changed.
# Strings can contain letters, numbers, symbols, and whitespace characters. They are used to represent text in Python.
# Strings can be concatenated using the + operator and repeated using the * operator.
# Strings can be indexed and sliced to access individual characters or substrings.


# EXAMPLES OF STRINGS IN PYTHON:
Name = "John"  # String enclosed in double quotes
city = 'New York'  # String enclosed in single quotes
Paragraph = """This is a paragraph.
It can span multiple lines."""  # String enclosed in triple quotes
print(Name)  # Output: John
print(city)  # Output: New York
print(Paragraph)  # Output: This is a paragraph. It can span multiple lines.


# here: j o h n 'j' is character at index 0, 'o' is character at index 1, 'h' is character at index 2, 'n' is character at index 3
# new york: n is character at index 0, e is character at index 1, w is character at index 2,
#           space is character at index 3, y is character at index 4, o is character at index 5, r is character at index 6, k is character at index 7
# paragraph: t is character at index 0, h is character at index 1, i is character at index 2, s is character at index 3, space is character at index 4, i is character at index 5, s is character at index 6, space is character at index 7, a is character at index 8, space is character at index 9, p is character at index 10, a is character at index 11, r is character at index 12, a is character at index 13, g is character at index 14, r is character at index 15, a is character at index 16, p is character at index 17, h is character at index 18, . is character at index 19






# CREATING A STRING IN PYTHON:
# 1. Using single quotes:

string1 = 'Hello, World!'  # String enclosed in single quotes
print(string1)  # Output: Hello, World!


# 2. Using double quotes:

string2 = "Python is awesome!"  # String
print(string2)  # Output: Python is awesome!

# 3. Using triple quotes:

string3 = '''This is a multi-line string.
It can span multiple lines.'''
print(string3)  # Output: This is a multi-line string.It can span multiple lines.

# ALL three methods of creating strings are valid in Python, and you can choose the one that best suits your needs.



# MULTI-LINE STRINGS IN PYTHON:
# Multi-line strings can be created using triple quotes (''' ''' or """ """).
# FOR example:
multi_line_string = """This is a multi-line string.
It can span multiple lines.
You can use it to create paragraphs or long text."""
print(multi_line_string)



