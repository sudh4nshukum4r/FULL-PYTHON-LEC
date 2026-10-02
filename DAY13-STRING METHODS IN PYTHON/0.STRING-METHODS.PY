# ==========================================================
# STRING METHODS IN PYTHON
# ==========================================================

# Definition:
# String methods are built-in methods used to perform
# different operations on strings.
#
# Syntax:
# string.method()
#
# Example:
# text = "python"
# print(text.upper())


# ==========================================================
# 1. upper()
# ==========================================================

# Definition:
# The upper() method converts all alphabetic characters
# of a string into uppercase letters.
#
# Syntax:
# string.upper()

text = "python"

print(text.upper())

# Output:
# PYTHON

# Reason:
# upper() changes lowercase letters into uppercase letters.


# ==========================================================
# 2. lower()
# ==========================================================

# Definition:
# The lower() method converts all alphabetic characters
# of a string into lowercase letters.
#
# Syntax:
# string.lower()

text = "PYTHON"

print(text.lower())

# Output:
# python

# Reason:
# lower() changes uppercase letters into lowercase letters.


# ==========================================================
# 3. capitalize()
# ==========================================================

# Definition:
# The capitalize() method converts the first character
# of a string to uppercase and the remaining characters
# to lowercase.
#
# Syntax:
# string.capitalize()

text = "pYTHON PROGRAMMING"

print(text.capitalize())

# Output:
# Python programming

# Reason:
# Only the first character becomes uppercase and
# the remaining letters become lowercase.


# ==========================================================
# 4. title()
# ==========================================================

# Definition:
# The title() method converts the first character of
# each word into uppercase.
#
# Syntax:
# string.title()

text = "python programming language"

print(text.title())

# Output:
# Python Programming Language

# Reason:
# Every word starts with an uppercase letter.


# ==========================================================
# 5. swapcase()
# ==========================================================

# Definition:
# The swapcase() method changes uppercase characters
# to lowercase and lowercase characters to uppercase.
#
# Syntax:
# string.swapcase()

text = "PyThOn"

print(text.swapcase())

# Output:
# pYtHoN

# Reason:
# The case of every alphabetic character is reversed.


# ==========================================================
# 6. strip()
# ==========================================================

# Definition:
# The strip() method removes whitespace from both the
# beginning and the end of a string.
#
# Syntax:
# string.strip()

text = "   Python   "

print(text.strip())

# Output:
# Python

# Reason:
# Extra spaces from both sides are removed.


# ==========================================================
# 7. lstrip()
# ==========================================================

# Definition:
# The lstrip() method removes whitespace from the
# left side of a string.
#
# Syntax:
# string.lstrip()

text = "   Python"

print(text.lstrip())

# Output:
# Python

# Reason:
# Spaces are removed only from the left side.


# ==========================================================
# 8. rstrip()
# ==========================================================

# Definition:
# The rstrip() method removes whitespace from the
# right side of a string.
#
# Syntax:
# string.rstrip()

text = "Python   "

print(text.rstrip())

# Output:
# Python

# Reason:
# Spaces are removed only from the right side.


# ==========================================================
# 9. replace()
# ==========================================================

# Definition:
# The replace() method replaces a specified substring
# with another substring.
#
# Syntax:
# string.replace(old, new)

text = "I like Java"

print(text.replace("Java", "Python"))

# Output:
# I like Python

# Reason:
# "Java" is replaced by "Python".


# ==========================================================
# 10. split()
# ==========================================================

# Definition:
# The split() method divides a string into a list of
# substrings.
#
# Syntax:
# string.split()

text = "Python is easy"

print(text.split())

# Output:
# ['Python', 'is', 'easy']

# Reason:
# The string is divided at whitespace and converted into a list.


# ==========================================================
# 11. split() WITH SEPARATOR
# ==========================================================

# Definition:
# split() can also divide a string using a specified separator.
#
# Syntax:
# string.split(separator)

text = "Python,Java,C++"

print(text.split(","))

# Output:
# ['Python', 'Java', 'C++']

# Reason:
# Comma is used as the separator.


# ==========================================================
# 12. join()
# ==========================================================

# Definition:
# The join() method combines elements of an iterable
# into a single string.
#
# Syntax:
# separator.join(iterable)

words = ["Python", "is", "easy"]

print(" ".join(words))

# Output:
# Python is easy

# Reason:
# A space is placed between all the words.


# ==========================================================
# 13. find()
# ==========================================================

# Definition:
# The find() method returns the index of the first
# occurrence of a specified substring.
# It returns -1 if the substring is not found.
#
# Syntax:
# string.find(substring)

text = "Python Programming"

print(text.find("P"))
print(text.find("Java"))

# Output:
# 0
# -1

# Reason:
# "P" is found at index 0.
# "Java" is not present, so -1 is returned.


# ==========================================================
# 14. index()
# ==========================================================

# Definition:
# The index() method returns the index of the first
# occurrence of a specified substring.
#
# Syntax:
# string.index(substring)

text = "Python"

print(text.index("t"))

# Output:
# 2

# Reason:
# "t" is present at index 2.

# Important:
# If the substring is not found, index() raises ValueError.


# ==========================================================
# 15. count()
# ==========================================================

# Definition:
# The count() method returns the number of times a
# specified substring occurs in a string.
#
# Syntax:
# string.count(substring)

text = "banana"

print(text.count("a"))

# Output:
# 3

# Reason:
# The letter "a" occurs three times.


# ==========================================================
# 16. startswith()
# ==========================================================

# Definition:
# The startswith() method checks whether a string
# starts with a specified substring.
#
# Syntax:
# string.startswith(value)

text = "Python Programming"

print(text.startswith("Python"))

# Output:
# True

# Reason:
# The string starts with "Python".


# ==========================================================
# 17. endswith()
# ==========================================================

# Definition:
# The endswith() method checks whether a string
# ends with a specified substring.
#
# Syntax:
# string.endswith(value)

file_name = "program.py"

print(file_name.endswith(".py"))

# Output:
# True

# Reason:
# The file name ends with ".py".


# ==========================================================
# 18. isalpha()
# ==========================================================

# Definition:
# The isalpha() method returns True if all characters
# in the string are alphabetic.
#
# Syntax:
# string.isalpha()

text = "Python"

print(text.isalpha())

# Output:
# True

# Reason:
# The string contains only alphabetic characters.


# ==========================================================
# 19. isdigit()
# ==========================================================

# Definition:
# The isdigit() method returns True if all characters
# in the string are digits.
#
# Syntax:
# string.isdigit()

number = "12345"

print(number.isdigit())

# Output:
# True

# Reason:
# All characters are digits.


# ==========================================================
# 20. isalnum()
# ==========================================================

# Definition:
# The isalnum() method returns True if all characters
# are alphabetic or numeric.
#
# Syntax:
# string.isalnum()

text = "Python123"

print(text.isalnum())

# Output:
# True

# Reason:
# The string contains only letters and numbers.


# ==========================================================
# 21. isspace()
# ==========================================================

# Definition:
# The isspace() method returns True if all characters
# in the string are whitespace characters.
#
# Syntax:
# string.isspace()

text = "   "

print(text.isspace())

# Output:
# True

# Reason:
# The string contains only spaces.


# ==========================================================
# 22. islower()
# ==========================================================

# Definition:
# The islower() method returns True if all cased
# characters in the string are lowercase.
#
# Syntax:
# string.islower()

text = "python"

print(text.islower())

# Output:
# True

# Reason:
# All alphabetic characters are lowercase.


# ==========================================================
# 23. isupper()
# ==========================================================

# Definition:
# The isupper() method returns True if all cased
# characters in the string are uppercase.
#
# Syntax:
# string.isupper()

text = "PYTHON"

print(text.isupper())

# Output:
# True

# Reason:
# All alphabetic characters are uppercase.


# ==========================================================
# 24. zfill()
# ==========================================================

# Definition:
# The zfill() method adds zeros to the left side of
# a string until it reaches the specified width.
#
# Syntax:
# string.zfill(width)

number = "42"

print(number.zfill(5))

# Output:
# 00042

# Reason:
# Three zeros are added to make the total length 5.


# ==========================================================
# 25. center()
# ==========================================================

# Definition:
# The center() method returns a centered string padded
# to a specified width.
#
# Syntax:
# string.center(width, fillchar)

text = "AI"

print(text.center(10, "-"))

# Output:
# ----AI----

# Reason:
# The string is placed in the center and the remaining
# space is filled with "-". 


# ==========================================================
# 26. ljust()
# ==========================================================

# Definition:
# The ljust() method left-aligns a string and pads
# the remaining space on the right.
#
# Syntax:
# string.ljust(width, fillchar)

text = "AI"

print(text.ljust(6, "-"))

# Output:
# AI----

# Reason:
# The string stays on the left and "-" fills the remaining space.


# ==========================================================
# 27. rjust()
# ==========================================================

# Definition:
# The rjust() method right-aligns a string and pads
# the remaining space on the left.
#
# Syntax:
# string.rjust(width, fillchar)

text = "AI"

print(text.rjust(6, "-"))

# Output:
# ----AI

# Reason:
# The string moves to the right and "-" fills the left side.


# ==========================================================
# 28. STRING IMMUTABILITY
# ==========================================================

# Definition:
# String immutability means that the characters of an
# existing string cannot be changed directly after
# the string has been created.
#
# HINGLISH:
# Ek baar string banne ke baad uske individual characters
# ko directly change nahi kar sakte.

word = "CAT"

# This will NOT work:
#
# word[0] = "B"

# Error:
# TypeError

# Reason:
# Python strings are immutable.


# Correct way:

word = "BAT"

print(word)

# Output:
# BAT

# Reason:
# We created a new string instead of changing one
# character of the old string.


# ==========================================================
# IMPORTANT EXAM DIFFERENCES
# ==========================================================

# upper()
# -> Converts all letters to uppercase.
#
# lower()
# -> Converts all letters to lowercase.
#
# capitalize()
# -> First character uppercase, remaining lowercase.
#
# title()
# -> First character of every word uppercase.
#
# ----------------------------------------------------------
#
# strip()
# -> Removes spaces from both sides.
#
# lstrip()
# -> Removes spaces from left side.
#
# rstrip()
# -> Removes spaces from right side.
#
# ----------------------------------------------------------
#
# find()
# -> Returns -1 if not found.
#
# index()
# -> Raises ValueError if not found.
#
# ----------------------------------------------------------
#
# split()
# -> Converts a string into a list.
#
# join()
# -> Combines elements into a string.
#
# ----------------------------------------------------------
#
# isalpha()
# -> Checks alphabets.
#
# isdigit()
# -> Checks digits.
#
# isalnum()
# -> Checks alphabets and numbers.
#
# ==========================================================
# END OF STRING METHODS
# ==========================================================