# ============================================================
# MEMBERSHIP OPERATORS: in / not in
# ============================================================

# Definition:
# Membership operators are used to check whether a value
# exists inside a sequence or collection.
#
# Python has two membership operators:
#
# in
# not in
#
# in      -> checks whether a value exists
# not in  -> checks whether a value does not exist
#
# The result is always True or False.


# ============================================================
# 1. IN OPERATOR
# ============================================================

# Definition:
# The "in" operator returns True when the given value
# is present inside a sequence or collection.


# Syntax:
#
# value in collection


# ------------------------------------------------------------
# Example 1: Check character in a string
# ------------------------------------------------------------

text = "Python"

print("P" in text)

# Output:
# True

# Reason:
# "P" exists inside the string "Python".
# Therefore, the result is True.


# ------------------------------------------------------------
# Example 2: Character is not present
# ------------------------------------------------------------

text = "Python"

print("z" in text)

# Output:
# False

# Reason:
# "z" does not exist inside "Python".
# Therefore, the result is False.


# ------------------------------------------------------------
# Example 3: Check word in a string
# ------------------------------------------------------------

sentence = "I am learning Python"

print("Python" in sentence)

# Output:
# True

# Reason:
# The word "Python" exists inside the sentence.


# ------------------------------------------------------------
# Example 4: Check word not present
# ------------------------------------------------------------

sentence = "I am learning Python"

print("Java" in sentence)

# Output:
# False

# Reason:
# The word "Java" does not exist in the sentence.


# ============================================================
# 2. NOT IN OPERATOR
# ============================================================

# Definition:
# The "not in" operator returns True when the given value
# is NOT present inside a sequence or collection.


# Syntax:
#
# value not in collection


# ------------------------------------------------------------
# Example 5: Character not in string
# ------------------------------------------------------------

text = "Python"

print("z" not in text)

# Output:
# True

# Reason:
# "z" is not present in "Python".
# Therefore, "z" not in text is True.


# ------------------------------------------------------------
# Example 6: Character is present
# ------------------------------------------------------------

text = "Python"

print("P" not in text)

# Output:
# False

# Reason:
# "P" is present in "Python".
# Therefore, the "not in" condition is False.


# ============================================================
# MEMBERSHIP WITH LIST
# ============================================================


# ------------------------------------------------------------
# Example 7: Value in a list
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(30 in numbers)

# Output:
# True

# Reason:
# 30 exists inside the list.


# ------------------------------------------------------------
# Example 8: Value not in a list
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(100 in numbers)

# Output:
# False

# Reason:
# 100 does not exist inside the list.


# ------------------------------------------------------------
# Example 9: Using not in with list
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(100 not in numbers)

# Output:
# True

# Reason:
# 100 is not present in the list.


# ============================================================
# MEMBERSHIP WITH TUPLE
# ============================================================


# ------------------------------------------------------------
# Example 10: Value in tuple
# ------------------------------------------------------------

languages = ("Python", "Java", "C++")

print("Python" in languages)

# Output:
# True

# Reason:
# "Python" exists inside the tuple.


# ------------------------------------------------------------
# Example 11: Value not in tuple
# ------------------------------------------------------------

languages = ("Python", "Java", "C++")

print("HTML" not in languages)

# Output:
# True

# Reason:
# "HTML" does not exist inside the tuple.


# ============================================================
# MEMBERSHIP WITH SET
# ============================================================


# ------------------------------------------------------------
# Example 12: Value in set
# ------------------------------------------------------------

skills = {"Python", "HTML", "CSS", "JavaScript"}

print("Python" in skills)

# Output:
# True

# Reason:
# "Python" exists inside the set.


# ------------------------------------------------------------
# Example 13: Value not in set
# ------------------------------------------------------------

skills = {"Python", "HTML", "CSS", "JavaScript"}

print("Java" not in skills)

# Output:
# True

# Reason:
# "Java" is not present in the set.


# ============================================================
# MEMBERSHIP WITH DICTIONARY
# ============================================================

# IMPORTANT:
# When "in" is used with a dictionary,
# Python normally checks the KEYS, not the values.


# ------------------------------------------------------------
# Example 14: Check dictionary key
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 20,
    "course": "AI"
}

print("name" in student)

# Output:
# True

# Reason:
# "name" is a key in the dictionary.


# ------------------------------------------------------------
# Example 15: Check dictionary key
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 20,
    "course": "AI"
}

print("email" in student)

# Output:
# False

# Reason:
# "email" is not a key in the dictionary.


# ------------------------------------------------------------
# Example 16: Check dictionary value
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 20,
    "course": "AI"
}

print("Rahul" in student.values())

# Output:
# True

# Reason:
# "Rahul" is a value in the dictionary.
# .values() gives access to dictionary values.


# ============================================================
# MEMBERSHIP WITH IF
# ============================================================


# ------------------------------------------------------------
# Example 17: Check language
# ------------------------------------------------------------

languages = ["Python", "Java", "C++"]

if "Python" in languages:
    print("Python is available")
else:
    print("Python is not available")

# Output:
# Python is available

# Reason:
# "Python" exists inside the list.
# Therefore, the if condition is True.


# ------------------------------------------------------------
# Example 18: Check unavailable language
# ------------------------------------------------------------

languages = ["Python", "Java", "C++"]

if "HTML" in languages:
    print("HTML is available")
else:
    print("HTML is not available")

# Output:
# HTML is not available

# Reason:
# "HTML" does not exist in the list.
# Therefore, the if condition is False.


# ------------------------------------------------------------
# Example 19: Using not in with if
# ------------------------------------------------------------

blocked_users = ["user1", "user2", "user3"]

username = "user5"

if username not in blocked_users:
    print("Access allowed")
else:
    print("Access denied")

# Output:
# Access allowed

# Reason:
# "user5" is not present in blocked_users.
# Therefore, not in returns True.


# ============================================================
# STRING MEMBERSHIP
# ============================================================


# ------------------------------------------------------------
# Example 20: Check substring
# ------------------------------------------------------------

email = "student@gmail.com"

if "@gmail.com" in email:
    print("Gmail account")
else:
    print("Other email")

# Output:
# Gmail account

# Reason:
# "@gmail.com" exists inside the email string.


# ------------------------------------------------------------
# Example 21: Check keyword
# ------------------------------------------------------------

message = "I am learning Python programming"

if "Python" in message:
    print("Python found")
else:
    print("Python not found")

# Output:
# Python found

# Reason:
# The word "Python" exists in the message.


# ------------------------------------------------------------
# Example 22: Case sensitivity
# ------------------------------------------------------------

language = "Python"

print("python" in language)

# Output:
# False

# Reason:
# Python is case-sensitive.
# "python" and "Python" are different strings.


# ------------------------------------------------------------
# Example 23: Case-insensitive membership
# ------------------------------------------------------------

language = "Python"

if "python" in language.lower():
    print("Python found")
else:
    print("Python not found")

# Output:
# Python found

# Reason:
# language.lower() converts "Python" into "python".
# Therefore, "python" is found.


# ============================================================
# USER INPUT + MEMBERSHIP
# ============================================================


# ------------------------------------------------------------
# Example 24: Check favorite language
# ------------------------------------------------------------

language = input("Enter your programming language: ")

if language in ["Python", "Java", "C++"]:
    print("Supported language")
else:
    print("Other language")

# Example Input:
# Enter your programming language: Python

# Output:
# Supported language

# Reason:
# "Python" exists inside the list.


# ------------------------------------------------------------
# Example 25: Check username
# ------------------------------------------------------------

username = input("Enter username: ")

users = ["admin", "student", "teacher"]

if username in users:
    print("User found")
else:
    print("User not found")

# Example Input:
# Enter username: student

# Output:
# User found

# Reason:
# "student" exists inside the users list.


# ============================================================
# INTERVIEW-STYLE EXAMPLES
# ============================================================


# ------------------------------------------------------------
# Example 26: Allowed file extensions
# ------------------------------------------------------------

filename = "program.py"

if filename.endswith((".py", ".js", ".java")):
    print("Programming file")
else:
    print("Other file")

# Output:
# Programming file

# Reason:
# The filename ends with ".py".
# So it matches one of the allowed extensions.


# ------------------------------------------------------------
# Example 27: Check allowed role
# ------------------------------------------------------------

role = "student"

if role in ["student", "teacher", "admin"]:
    print("Role is allowed")
else:
    print("Role is not allowed")

# Output:
# Role is allowed

# Reason:
# "student" exists inside the list of allowed roles.


# ------------------------------------------------------------
# Example 28: Check blocked word
# ------------------------------------------------------------

message = "This is a normal message"

blocked_words = ["spam", "hack", "scam"]

if any(word in message.lower() for word in blocked_words):
    print("Blocked word found")
else:
    print("No blocked word found")

# Output:
# No blocked word found

# Reason:
# None of the blocked words exist in the message.
# Therefore, the condition is False.


# ============================================================
# IMPORTANT DIFFERENCE
# ============================================================

# in:
#
# Checks whether something EXISTS.


numbers = [10, 20, 30]

print(20 in numbers)

# Output:
# True


# not in:
#
# Checks whether something DOES NOT EXIST.

print(50 not in numbers)

# Output:
# True


# ============================================================
# QUICK REVISION
# ============================================================

# "P" in "Python"
# -> True
#
# "z" in "Python"
# -> False
#
# "z" not in "Python"
# -> True
#
# 20 in [10, 20, 30]
# -> True
#
# 50 not in [10, 20, 30]
# -> True








'''NOTE:----Ekdum simple rule

in      → andar hai kya?
not in  → andar nahi hai kya?


Example:--

names = ["Rahul", "Aman", "Ravi"]

"Rahul" in names
# True

"Akash" in names
# False

"Akash" not in names
# True

'''




# Important: Dictionary mein in normally keys check karta hai:

'''student = {"name": "Rahul", "age": 20}

"name" in student
# True

"Rahul" in student
# False
'''


'''Values check karni ho toh:--

"Rahul" in student.values()
# True

'''