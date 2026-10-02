# STRING METHODS - PRACTICE EXAMPLES


# 1. upper()
text = "python programming"
print(text.upper())


# Output:
# PYTHON PROGRAMMING


# Reason:
# upper() converts all lowercase letters into uppercase letters.



# 2. lower()
text = "PYTHON PROGRAMMING"
print(text.lower())


# Output:
# python programming


# Reason:
# lower() converts all uppercase letters into lowercase letters.



# 3. capitalize()
text = "python programming"
print(text.capitalize())


# Output:
# Python programming


# Reason:
# capitalize() makes the first character uppercase and the remaining characters lowercase.



# 4. title()
text = "python programming language"
print(text.title())


# Output:
# Python Programming Language


# Reason:
# title() makes the first letter of every word uppercase.



# 5. swapcase()
text = "Python PROGRAMMING"
print(text.swapcase())


# Output:
# pYTHON programming


# Reason:
# swapcase() changes uppercase letters to lowercase and lowercase letters to uppercase.



# 6. strip()
text = "   Python   "
print(text.strip())


# Output:
# Python


# Reason:
# strip() removes spaces from both the beginning and the end.



# 7. lstrip()
text = "   Python"
print(text.lstrip())


# Output:
# Python


# Reason:
# lstrip() removes spaces only from the left side.



# 8. rstrip()
text = "Python   "
print(text.rstrip())


# Output:
# Python


# Reason:
# rstrip() removes spaces only from the right side.



# 9. replace()
text = "I like Java"
print(text.replace("Java", "Python"))


# Output:
# I like Python


# Reason:
# replace() replaces one part of a string with another.



# 10. split()
text = "Python is easy"
print(text.split())


# Output:
# ['Python', 'is', 'easy']


# Reason:
# split() divides the string into a list of words.



# 11. split() with separator
text = "Python,Java,C++"
print(text.split(","))


# Output:
# ['Python', 'Java', 'C++']


# Reason:
# The comma is used as the separator, so the string is divided wherever a comma appears.



# 12. join()
words = ["Python", "is", "easy"]
print(" ".join(words))


# Output:
# Python is easy


# Reason:
# join() combines list elements using the given string as a separator.



# 13. find()
text = "Python Programming"
print(text.find("Pro"))


# Output:
# 7


# Reason:
# "Pro" starts at index 7.



# 14. index()
text = "Python Programming"
print(text.index("Pro"))


# Output:
# 7


# Reason:
# index() returns the position where "Pro" first appears.



# 15. count()
text = "banana"
print(text.count("a"))


# Output:
# 3


# Reason:
# The letter "a" appears three times in the string.



# 16. startswith()
text = "Python Programming"
print(text.startswith("Python"))


# Output:
# True


# Reason:
# The string starts with "Python", so the result is True.



# 17. endswith()
text = "Python Programming"
print(text.endswith("Programming"))


# Output:
# True


# Reason:
# The string ends with "Programming", so the result is True.



# 18. isalpha()
text = "Python"
print(text.isalpha())


# Output:
# True


# Reason:
# The string contains only alphabetic characters.



# 19. isdigit()
text = "12345"
print(text.isdigit())


# Output:
# True


# Reason:
# The string contains only digits.



# 20. isalnum()
text = "Python123"
print(text.isalnum())


# Output:
# True


# Reason:
# The string contains only letters and numbers.



# 21. isspace()
text = "     "
print(text.isspace())


# Output:
# True


# Reason:
# The string contains only whitespace characters.



# 22. islower()
text = "python"
print(text.islower())


# Output:
# True


# Reason:
# All alphabetic characters are lowercase.



# 23. isupper()
text = "PYTHON"
print(text.isupper())


# Output:
# True


# Reason:
# All alphabetic characters are uppercase.



# 24. zfill()
number = "25"
print(number.zfill(5))


# Output:
# 00025


# Reason:
# zfill() adds zeros to the left until the string reaches the given width.



# 25. center()
text = "Python"
print(text.center(10, "-"))


# Output:
# --Python--


# Reason:
# center() places the string in the center and fills the remaining space with "-".



# 26. ljust()
text = "Python"
print(text.ljust(10, "-"))


# Output:
# Python----


# Reason:
# ljust() keeps the string on the left and fills the remaining space on the right.



# 27. rjust()
text = "Python"
print(text.rjust(10, "-"))


# Output:
# ----Python


# Reason:
# rjust() keeps the string on the right and fills the remaining space on the left.



# 28. String Immutability
text = "Python"

# text[0] = "J"     # This will give TypeError

text = "J" + text[1:]
print(text)


# Output:
# Jython


# Reason:
# Strings are immutable, so individual characters cannot be changed directly.
# We create a new string instead.