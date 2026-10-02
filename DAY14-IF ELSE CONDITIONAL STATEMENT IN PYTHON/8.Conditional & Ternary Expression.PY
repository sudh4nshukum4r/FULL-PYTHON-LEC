# ============================================================
# CONDITIONAL / TERNARY EXPRESSION
# ============================================================

# Definition:
# A conditional expression is a short way to write
# a simple if-else statement in one line.
#
# It is also commonly called a ternary operator/expression
# in Python.


# Syntax:
#
# value_if_true if condition else value_if_false


# ============================================================
# BASIC EXAMPLES
# ============================================================


# ------------------------------------------------------------
# Example 1: Adult or Minor
# ------------------------------------------------------------

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)

# Output:
# Adult

# Reason:
# age >= 18 is True.
# Therefore, "Adult" is selected.


# ------------------------------------------------------------
# Example 2: Minor
# ------------------------------------------------------------

age = 15

result = "Adult" if age >= 18 else "Minor"

print(result)

# Output:
# Minor

# Reason:
# age >= 18 is False.
# Therefore, "Minor" is selected.


# ------------------------------------------------------------
# Example 3: Even or Odd
# ------------------------------------------------------------

num = 7

result = "Even" if num % 2 == 0 else "Odd"

print(result)

# Output:
# Odd

# Reason:
# 7 % 2 gives 1.
# So num % 2 == 0 is False.
# Therefore, "Odd" is selected.


# ------------------------------------------------------------
# Example 4: Positive or Negative
# ------------------------------------------------------------

num = -10

result = "Positive" if num >= 0 else "Negative"

print(result)

# Output:
# Negative

# Reason:
# -10 >= 0 is False.
# Therefore, "Negative" is selected.


# ------------------------------------------------------------
# Example 5: Pass or Fail
# ------------------------------------------------------------

marks = 75

result = "Pass" if marks >= 40 else "Fail"

print(result)

# Output:
# Pass

# Reason:
# 75 >= 40 is True.
# Therefore, "Pass" is selected.


# ============================================================
# TERNARY WITH NUMBERS
# ============================================================


# ------------------------------------------------------------
# Example 6: Find greater number
# ------------------------------------------------------------

a = 20
b = 10

greater = a if a > b else b

print(greater)

# Output:
# 20

# Reason:
# a > b means 20 > 10, which is True.
# Therefore, a (20) is selected.


# ------------------------------------------------------------
# Example 7: Find smaller number
# ------------------------------------------------------------

a = 20
b = 10

smaller = a if a < b else b

print(smaller)

# Output:
# 10

# Reason:
# 20 < 10 is False.
# Therefore, b (10) is selected.


# ------------------------------------------------------------
# Example 8: Find maximum of two numbers
# ------------------------------------------------------------

x = 50
y = 80

maximum = x if x > y else y

print(maximum)

# Output:
# 80

# Reason:
# 50 > 80 is False.
# Therefore, y (80) is selected.


# ------------------------------------------------------------
# Example 9: Find minimum of two numbers
# ------------------------------------------------------------

x = 50
y = 80

minimum = x if x < y else y

print(minimum)

# Output:
# 50

# Reason:
# 50 < 80 is True.
# Therefore, x (50) is selected.


# ============================================================
# TERNARY WITH USER INPUT
# ============================================================


# ------------------------------------------------------------
# Example 10: User age
# ------------------------------------------------------------

age = int(input("Enter your age: "))

result = "Adult" if age >= 18 else "Minor"

print(result)

# Example Input:
# Enter your age: 21

# Output:
# Adult

# Reason:
# 21 >= 18 is True.
# Therefore, "Adult" is selected.


# ------------------------------------------------------------
# Example 11: User marks
# ------------------------------------------------------------

marks = int(input("Enter your marks: "))

result = "Pass" if marks >= 40 else "Fail"

print(result)

# Example Input:
# Enter your marks: 35

# Output:
# Fail

# Reason:
# 35 >= 40 is False.
# Therefore, "Fail" is selected.


# ------------------------------------------------------------
# Example 12: User number
# ------------------------------------------------------------

num = int(input("Enter a number: "))

result = "Even" if num % 2 == 0 else "Odd"

print(result)

# Example Input:
# Enter a number: 12

# Output:
# Even

# Reason:
# 12 % 2 gives 0.
# Therefore, the condition is True.


# ============================================================
# TERNARY WITH STRINGS
# ============================================================


# ------------------------------------------------------------
# Example 13: Check username
# ------------------------------------------------------------

username = "admin"

message = "Welcome Admin" if username == "admin" else "Unknown User"

print(message)

# Output:
# Welcome Admin

# Reason:
# username == "admin" is True.
# Therefore, "Welcome Admin" is selected.


# ------------------------------------------------------------
# Example 14: Check language
# ------------------------------------------------------------

language = "Python"

message = "Python selected" if language == "Python" else "Other language"

print(message)

# Output:
# Python selected

# Reason:
# language is equal to "Python".
# Therefore, the first value is selected.


# ============================================================
# TERNARY WITH LOGICAL OPERATORS
# ============================================================


# ------------------------------------------------------------
# Example 15: Eligibility
# ------------------------------------------------------------

age = 20
marks = 75

result = "Eligible" if age >= 18 and marks >= 40 else "Not Eligible"

print(result)

# Output:
# Eligible

# Reason:
# age >= 18 is True.
# marks >= 40 is also True.
# True and True = True.
# Therefore, "Eligible" is selected.


# ------------------------------------------------------------
# Example 16: Weekend check
# ------------------------------------------------------------

day = "Sunday"

result = "Weekend" if day == "Saturday" or day == "Sunday" else "Weekday"

print(result)

# Output:
# Weekend

# Reason:
# day == "Sunday" is True.
# Therefore, the OR condition is True.


# ============================================================
# TERNARY WITH MEMBERSHIP
# ============================================================


# ------------------------------------------------------------
# Example 17: Language availability
# ------------------------------------------------------------

language = "Python"

result = "Available" if language in ["Python", "Java", "C++"] else "Not Available"

print(result)

# Output:
# Available

# Reason:
# "Python" exists in the list.
# Therefore, the condition is True.


# ------------------------------------------------------------
# Example 18: User role
# ------------------------------------------------------------

role = "student"

result = "Allowed" if role in ["student", "teacher", "admin"] else "Denied"

print(result)

# Output:
# Allowed

# Reason:
# "student" exists in the allowed roles list.


# ============================================================
# TERNARY INSIDE PRINT
# ============================================================


# ------------------------------------------------------------
# Example 19: Directly print result
# ------------------------------------------------------------

age = 22

print("Adult" if age >= 18 else "Minor")

# Output:
# Adult

# Reason:
# age >= 18 is True.
# Therefore, "Adult" is printed.


# ------------------------------------------------------------
# Example 20: Direct even/odd
# ------------------------------------------------------------

num = 9

print("Even" if num % 2 == 0 else "Odd")

# Output:
# Odd

# Reason:
# 9 % 2 gives 1.
# Therefore, the condition is False.


# ============================================================
# NESTED TERNARY
# ============================================================

# A ternary expression can also contain another
# conditional expression.
#
# But beginners should avoid making it too complicated.


# ------------------------------------------------------------
# Example 21: Grade using nested ternary
# ------------------------------------------------------------

marks = 85

grade = (
    "A"
    if marks >= 80
    else "B"
    if marks >= 60
    else "C"
)

print(grade)

# Output:
# A

# Reason:
# marks is 85.
# 85 >= 80 is True.
# Therefore, "A" is selected.


# ------------------------------------------------------------
# Example 22: Positive, negative or zero
# ------------------------------------------------------------

num = -5

result = (
    "Positive"
    if num > 0
    else "Zero"
    if num == 0
    else "Negative"
)

print(result)

# Output:
# Negative

# Reason:
# num > 0 is False.
# num == 0 is also False.
# Therefore, "Negative" is selected.


# ============================================================
# NORMAL IF-ELSE VS TERNARY
# ============================================================


# ------------------------------------------------------------
# Normal if-else
# ------------------------------------------------------------

age = 20

if age >= 18:
    result = "Adult"
else:
    result = "Minor"

print(result)

# Output:
# Adult


# ------------------------------------------------------------
# Same logic using ternary
# ------------------------------------------------------------

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)

# Output:
# Adult

# Reason:
# Both programs produce the same result.
# The ternary expression is simply a shorter way
# to write a simple if-else assignment.


# ============================================================
# IMPORTANT RULE
# ============================================================

# Ternary syntax is NOT:

# if condition:
#     value1
# else:
#     value2


# Correct ternary syntax is:

# value1 if condition else value2


# Example:

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)

# Output:
# Adult





'''NOTE:----Ternary ka formula bas ye yaad karo


1) VALUE_IF_TRUE if CONDITION else VALUE_IF_FALSE

--Example:--

age = 20
result = "Adult" if age >= 18 else "Minor"


Isko normal if-else mein likho toh:--

if age >= 18:
    result = "Adult"
else:
    result = "Minor"
'''

'''
 Ternary tab use karo jab condition simple ho. 
 Bahut complicated logic ho toh normal if-elif-else 
zyada readable hota hai.
'''