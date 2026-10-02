
# ============================================================
# 1. STRING
# ============================================================

# DEFINITION:
# A string is an immutable sequence of characters enclosed
# within single quotes, double quotes, or triple quotes.
#
# HINGLISH:
# String text/characters ko store karne ke liye use hoti hai.
# Python mein string ke characters ko directly change nahi
# kar sakte, isliye strings immutable hoti hain.

name = "Sudhanshu"
language = 'Python'

print(name)
print(language)

# OUTPUT:
# Sudhanshu
# Python


# ============================================================
# 2. CREATING A STRING
# ============================================================

# DEFINITION:
# A string can be created by enclosing characters or text
# inside quotation marks.

# Single quotes
name = 'Python'

# Double quotes
name2 = "Programming"

# Triple quotes
message = """Python is
a programming
language."""

print(name)
print(name2)
print(message)

# REASON:
# Quotes tell Python that the given value is a string.


# ============================================================
# 3. STRING INDEXING
# ============================================================

# DEFINITION:
# String indexing is the process of accessing individual
# characters using their position (index) in the string.
#
# HINGLISH:
# String ke har character ka ek index number hota hai.
# Python mein indexing 0 se start hoti hai.

word = "PYTHON"

# Character: P  Y  T  H  O  N
# Index:     0  1  2  3  4  5

print(word[0])
print(word[2])
print(word[5])

# OUTPUT:
# P
# T
# N

# REASON:
# Python indexing always starts from 0.


# ============================================================
# 4. NEGATIVE INDEXING
# ============================================================

# DEFINITION:
# Negative indexing allows characters to be accessed
# from the end of a string.
#
# HINGLISH:
# Negative indexing right side se start hoti hai.
# Last character ka index -1 hota hai.

word = "PYTHON"

# Character: P   Y   T   H   O   N
# Negative: -6  -5  -4  -3  -2  -1

print(word[-1])
print(word[-2])
print(word[-3])

# OUTPUT:
# N
# O
# H

# REASON:
# -1 always refers to the last character.


# ============================================================
# 5. STRING LENGTH - len()
# ============================================================

# DEFINITION:
# The len() function returns the total number of characters
# present in a string.
#
# HINGLISH:
# len() string ke total characters count karta hai.

word = "PYTHON"

print(len(word))

# OUTPUT:
# 6

# REASON:
# P, Y, T, H, O, N = 6 characters.


# IMPORTANT:
# If length = 6
# Valid indexes = 0 to 5
#
# Last index = len(string) - 1

print(word[len(word) - 1])

# OUTPUT:
# N


# ============================================================
# 6. ACCESSING CHARACTERS USING A LOOP
# ============================================================

# DEFINITION:
# A string can be traversed character by character using
# a for loop.
#
# HINGLISH:
# for loop string ke har character ko one by one access karta hai.

word = "CAT"

for char in word:
    print(char)

# OUTPUT:
# C
# A
# T

# REASON:
# Each iteration stores the current character in 'char'.


# ============================================================
# 7. INDEX + CHARACTER USING LOOP
# ============================================================

# DEFINITION:
# The range() function can be combined with len() to
# access both the index and character of a string.

word = "DOG"

for i in range(len(word)):
    print(i, word[i])

# OUTPUT:
# 0 D
# 1 O
# 2 G

# REASON:
# i = index
# word[i] = character at that index


# ============================================================
# 8. STRING SLICING
# ============================================================

# DEFINITION:
# String slicing is the process of extracting a portion
# of a string using a range of indexes.
#
# SYNTAX:
# string[start:end]
#
# IMPORTANT:
# start is included.
# end is excluded.
#
# HINGLISH:
# String ka ek specific part nikalne ke liye slicing use hoti hai.

word = "PYTHON"

print(word[1:4])

# Index:
# P  Y  T  H  O  N
# 0  1  2  3  4  5

# OUTPUT:
# YTH

# REASON:
# Index 1, 2, 3 included hain.
# Index 4 excluded hai.


# ============================================================
# 9. SLICING FROM BEGINNING
# ============================================================

word = "PYTHON"

print(word[:3])

# OUTPUT:
# PYT

# REASON:
# Empty start means slicing begins from index 0.


# ============================================================
# 10. SLICING UNTIL THE END
# ============================================================

word = "PYTHON"

print(word[3:])

# OUTPUT:
# HON

# REASON:
# Empty end means slicing continues until the last character.


# ============================================================
# 11. SLICING WITH STEP
# ============================================================

# DEFINITION:
# The step value specifies the interval between selected
# characters.
#
# SYNTAX:
# string[start:end:step]

word = "PYTHON"

print(word[::2])

# OUTPUT:
# PTO

# REASON:
# Every second character is selected.


# ============================================================
# 12. REVERSE A STRING USING SLICING
# ============================================================

word = "PYTHON"

print(word[::-1])

# OUTPUT:
# NOHTYP

# REASON:
# Step = -1 means move from right to left.


# ============================================================
# 13. STRING CONCATENATION
# ============================================================

# DEFINITION:
# String concatenation is the process of joining two or more
# strings together.
#
# HINGLISH:
# Do ya more strings ko jodne ko concatenation kehte hain.

first = "Python"
last = "Programming"

result = first + " " + last

print(result)

# OUTPUT:
# Python Programming

# REASON:
# + operator strings ko join karta hai.


# ============================================================
# 14. STRING REPETITION
# ============================================================

# DEFINITION:
# String repetition means repeating a string multiple times
# using the * operator.

word = "Hi "

print(word * 3)

# OUTPUT:
# Hi Hi Hi

# REASON:
# * 3 string ko three times repeat karta hai.


# ============================================================
# 15. MEMBERSHIP OPERATORS
# ============================================================

# DEFINITION:
# Membership operators are used to check whether a character
# or substring exists inside a string.

word = "PYTHON"

print("P" in word)
print("JAVA" in word)
print("JAVA" not in word)

# OUTPUT:
# True
# False
# True

# REASON:
# 'in' checks presence.
# 'not in' checks absence.


# ============================================================
# 16. upper()
# ============================================================

# DEFINITION:
# upper() returns a new string with all alphabetic characters
# converted to uppercase.
#
# HINGLISH:
# Saare letters ko CAPITAL letters mein convert karta hai.

text = "python"

print(text.upper())

# OUTPUT:
# PYTHON

# REASON:
# Lowercase letters uppercase mein convert hue.


# ============================================================
# 17. lower()
# ============================================================

# DEFINITION:
# lower() returns a new string with all alphabetic characters
# converted to lowercase.

text = "PYTHON"

print(text.lower())

# OUTPUT:
# python

# REASON:
# Uppercase letters lowercase mein convert hue.


# ============================================================
# 18. capitalize()
# ============================================================

# DEFINITION:
# capitalize() converts the first character to uppercase
# and the remaining characters to lowercase.

text = "pYTHON PROGRAMMING"

print(text.capitalize())

# OUTPUT:
# Python programming

# REASON:
# Only first character uppercase hai; remaining lowercase.


# ============================================================
# 19. title()
# ============================================================

# DEFINITION:
# title() converts the first character of each word
# to uppercase.

text = "python programming language"

print(text.title())

# OUTPUT:
# Python Programming Language

# REASON:
# Har word ka first character uppercase hua.


# ============================================================
# 20. swapcase()
# ============================================================

# DEFINITION:
# swapcase() converts uppercase characters to lowercase
# and lowercase characters to uppercase.

text = "PyThOn"

print(text.swapcase())

# OUTPUT:
# pYtHoN

# REASON:
# Character ka case reverse ho gaya.


# ============================================================
# 21. strip()
# ============================================================

# DEFINITION:
# strip() removes leading and trailing whitespace
# from a string.

text = "   Python   "

print(text.strip())

# OUTPUT:
# Python

# REASON:
# Left aur right ke extra spaces remove hue.


# ============================================================
# 22. lstrip()
# ============================================================

# DEFINITION:
# lstrip() removes leading whitespace from a string.

text = "   Python   "

print(text.lstrip())

# OUTPUT:
# Python   

# REASON:
# Sirf left-side spaces remove hue.


# ============================================================
# 23. rstrip()
# ============================================================

# DEFINITION:
# rstrip() removes trailing whitespace from a string.

text = "   Python   "

print(text.rstrip())

# OUTPUT:
#    Python

# REASON:
# Sirf right-side spaces remove hue.


# ============================================================
# 24. replace()
# ============================================================

# DEFINITION:
# replace() returns a new string in which a specified
# substring is replaced by another substring.

# SYNTAX:
# string.replace(old, new)

text = "I like Java"

print(text.replace("Java", "Python"))

# OUTPUT:
# I like Python

# REASON:
# Java ko Python se replace kiya gaya.


# ============================================================
# 25. split()
# ============================================================

# DEFINITION:
# split() divides a string into a list of substrings
# using a specified separator.

text = "Python is easy"

print(text.split())

# OUTPUT:
# ['Python', 'is', 'easy']

# REASON:
# Default separator whitespace hota hai.


# ============================================================
# 26. join()
# ============================================================

# DEFINITION:
# join() combines elements of an iterable into a single string
# using a specified separator.

words = ["Python", "is", "easy"]

print(" ".join(words))

# OUTPUT:
# Python is easy

# REASON:
# Space separator ban kar elements ko join karta hai.


# ============================================================
# 27. find()
# ============================================================

# DEFINITION:
# find() returns the index of the first occurrence
# of a specified substring.
# It returns -1 if the substring is not found.

text = "Python Programming"

print(text.find("P"))
print(text.find("Java"))

# OUTPUT:
# 0
# -1

# REASON:
# P index 0 par hai.
# Java present nahi hai, therefore -1.


# ============================================================
# 28. index()
# ============================================================

# DEFINITION:
# index() returns the index of the first occurrence
# of a specified substring.
#
# IMPORTANT:
# If the substring is not found, index() raises ValueError.

text = "Python"

print(text.index("t"))

# OUTPUT:
# 2

# REASON:
# t index 2 par hai.


# ============================================================
# 29. count()
# ============================================================

# DEFINITION:
# count() returns the number of occurrences of a specified
# substring in a string.

text = "banana"

print(text.count("a"))

# OUTPUT:
# 3

# REASON:
# 'a' total 3 times present hai.


# ============================================================
# 30. startswith()
# ============================================================

# DEFINITION:
# startswith() checks whether a string begins with
# a specified substring.

text = "Python Programming"

print(text.startswith("Python"))

# OUTPUT:
# True

# REASON:
# String Python se start ho rahi hai.


# ============================================================
# 31. endswith()
# ============================================================

# DEFINITION:
# endswith() checks whether a string ends with
# a specified substring.

file_name = "program.py"

print(file_name.endswith(".py"))

# OUTPUT:
# True

# REASON:
# String .py par end ho rahi hai.


# ============================================================
# 32. isalpha()
# ============================================================

# DEFINITION:
# isalpha() returns True if all characters are alphabetic
# and the string is not empty.

print("Python".isalpha())

# OUTPUT:
# True

# REASON:
# String mein sirf alphabets hain.


# ============================================================
# 33. isdigit()
# ============================================================

# DEFINITION:
# isdigit() returns True if all characters are digits
# and the string is not empty.

print("12345".isdigit())

# OUTPUT:
# True

# REASON:
# Saare characters digits hain.


# ============================================================
# 34. isalnum()
# ============================================================

# DEFINITION:
# isalnum() returns True if all characters are alphabetic
# or numeric and the string is not empty.

print("Python123".isalnum())

# OUTPUT:
# True

# REASON:
# Alphabets + numbers allowed hain.


# ============================================================
# 35. isspace()
# ============================================================

# DEFINITION:
# isspace() returns True if all characters are whitespace
# and the string is not empty.

print("   ".isspace())

# OUTPUT:
# True

# REASON:
# String mein sirf whitespace characters hain.


# ============================================================
# 36. islower()
# ============================================================

# DEFINITION:
# islower() returns True if all cased characters
# are lowercase.

print("python".islower())

# OUTPUT:
# True

# REASON:
# All alphabetic characters lowercase hain.


# ============================================================
# 37. isupper()
# ============================================================

# DEFINITION:
# isupper() returns True if all cased characters
# are uppercase.

print("PYTHON".isupper())

# OUTPUT:
# True

# REASON:
# All alphabetic characters uppercase hain.


# ============================================================
# 38. zfill()
# ============================================================

# DEFINITION:
# zfill() pads a numeric string with zeros on the left
# until it reaches the specified width.

number = "42"

print(number.zfill(5))

# OUTPUT:
# 00042

# REASON:
# Total width 5 karne ke liye zeros add hue.


# ============================================================
# 39. center()
# ============================================================

# DEFINITION:
# center() returns a centered string padded to
# the specified width.

text = "AI"

print(text.center(10, "-"))

# OUTPUT:
# ----AI----

# REASON:
# String ko center mein place karke remaining space
# '-' se fill ki gayi.


# ============================================================
# 40. STRING IMMUTABILITY
# ============================================================

# DEFINITION:
# String immutability means that the characters of an existing
# string cannot be changed directly after the string is created.
#
# HINGLISH:
# Ek baar string create hone ke baad uske individual characters
# ko directly modify nahi kar sakte.

word = "CAT"

# This is NOT allowed:
#
# word[0] = "B"
#
# ERROR:
# TypeError

# REASON:
# Python strings are immutable.


# Correct approach:

word = "BAT"

print(word)

# OUTPUT:
# BAT

# REASON:
# Humne original string ko modify nahi kiya.
# Humne ek new string assign ki.


# ============================================================
# 41. IMPORTANT IMMUTABILITY EXAMPLE
# ============================================================

text = "python"

new_text = text.upper()

print(text)
print(new_text)

# OUTPUT:
# python
# PYTHON

# REASON:
# upper() original string ko change nahi karta.
# It returns a NEW string.


# ============================================================
# 42. METHOD CHAINING
# ============================================================

# DEFINITION:
# Method chaining is the process of calling multiple methods
# sequentially on the result of the previous method.

text = "   python programming   "

result = text.strip().upper()

print(result)

# OUTPUT:
# PYTHON PROGRAMMING

# REASON:
# Step 1: strip() -> extra spaces remove
# Step 2: upper() -> uppercase


# ============================================================
# 43. IMPORTANT DIFFERENCES FOR EXAM
# ============================================================

# upper()
# -> All letters uppercase.
#
# lower()
# -> All letters lowercase.
#
# capitalize()
# -> Only first character uppercase.
#
# title()
# -> First character of every word uppercase.
#
# ------------------------------------------------------------
#
# strip()
# -> Both left and right whitespace.
#
# lstrip()
# -> Left whitespace.
#
# rstrip()
# -> Right whitespace.
#
# ------------------------------------------------------------
#
# find()
# -> Not found = -1
#
# index()
# -> Not found = ValueError
#
# ------------------------------------------------------------
#
# split()
# -> String to List
#
# join()
# -> Iterable to String
#
# ============================================================


# ============================================================
# 44. QUICK REVISION
# ============================================================

# upper()       -> uppercase
# lower()       -> lowercase
# capitalize()  -> first letter uppercase
# title()       -> each word first letter uppercase
# swapcase()    -> reverse case
#
# strip()       -> both-side spaces
# lstrip()      -> left spaces
# rstrip()      -> right spaces
#
# replace()     -> replace text
# split()       -> String -> List
# join()        -> List/Iterable -> String
#
# find()        -> position / -1
# index()       -> position / ValueError
# count()       -> number of occurrences
#
# startswith()  -> starting check
# endswith()    -> ending check
#
# isalpha()     -> alphabets
# isdigit()     -> digits
# isalnum()     -> alphabets + numbers
# isspace()     -> whitespace
# islower()     -> lowercase check
# isupper()     -> uppercase check
#
# zfill()       -> zeros on left
# center()      -> center alignment
#
# ============================================================
#                 END OF STRING NOTES
# ============================================================