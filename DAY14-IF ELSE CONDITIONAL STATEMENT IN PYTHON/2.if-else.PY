# ============================================================
# IF-ELSE STATEMENT
# ============================================================

# Definition:
# The if-else statement is used to execute one block of code
# when a condition is True and another block when it is False.


# Syntax:
#
# if condition:
#     statement
# else:
#     statement


# ------------------------------------------------------------
# Example 1: Basic if-else
# ------------------------------------------------------------

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Output:
# Adult

# Reason:
# age is 20.
# 20 >= 18 is True, so the if block executes.


# ------------------------------------------------------------
# Example 2: Condition is False
# ------------------------------------------------------------

age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Output:
# Minor

# Reason:
# age is 15.
# 15 >= 18 is False, so the else block executes.


# ------------------------------------------------------------
# Example 3: Check positive or negative
# ------------------------------------------------------------

num = -10

if num >= 0:
    print("Positive")
else:
    print("Negative")

# Output:
# Negative

# Reason:
# num is -10.
# -10 >= 0 is False, so else executes.


# ------------------------------------------------------------
# Example 4: Check even or odd
# ------------------------------------------------------------

num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output:
# Odd

# Reason:
# 7 % 2 gives 1.
# 1 == 0 is False, so the else block executes.


# ------------------------------------------------------------
# Example 5: Check pass or fail
# ------------------------------------------------------------

marks = 65

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Output:
# Pass

# Reason:
# marks is 65.
# 65 >= 40 is True, so Pass is printed.


# ------------------------------------------------------------
# Example 6: Check voting eligibility
# ------------------------------------------------------------

age = 17

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Output:
# Not eligible to vote

# Reason:
# age is 17.
# 17 >= 18 is False, so else executes.


# ------------------------------------------------------------
# Example 7: Compare two numbers
# ------------------------------------------------------------

a = 25
b = 20

if a > b:
    print("a is greater")
else:
    print("b is greater or equal")

# Output:
# a is greater

# Reason:
# 25 > 20 is True.
# Therefore, the if block executes.


# ------------------------------------------------------------
# Example 8: Check password
# ------------------------------------------------------------

password = "python123"

if password == "python123":
    print("Login successful")
else:
    print("Wrong password")

# Output:
# Login successful

# Reason:
# The entered password is exactly equal to "python123".
# Therefore, the condition is True.


# ------------------------------------------------------------
# Example 9: Wrong password
# ------------------------------------------------------------

password = "hello123"

if password == "python123":
    print("Login successful")
else:
    print("Wrong password")

# Output:
# Wrong password

# Reason:
# "hello123" is not equal to "python123".
# Therefore, the condition is False.


# ------------------------------------------------------------
# Example 10: Check username
# ------------------------------------------------------------

username = "admin"

if username == "admin":
    print("Welcome Admin")
else:
    print("Unknown User")

# Output:
# Welcome Admin

# Reason:
# username is "admin".
# The comparison returns True.


# ------------------------------------------------------------
# Example 11: String comparison
# ------------------------------------------------------------

city = "Delhi"

if city == "Delhi":
    print("Capital city")
else:
    print("Different city")

# Output:
# Capital city

# Reason:
# city contains "Delhi".
# Therefore, city == "Delhi" is True.


# ------------------------------------------------------------
# Example 12: Check character
# ------------------------------------------------------------

letter = "A"

if letter == "A":
    print("Letter A")
else:
    print("Some other letter")

# Output:
# Letter A

# Reason:
# letter is exactly "A".
# So the condition is True.


# ------------------------------------------------------------
# Example 13: Using !=
# ------------------------------------------------------------

age = 25

if age != 18:
    print("Age is not 18")
else:
    print("Age is 18")

# Output:
# Age is not 18

# Reason:
# 25 is not equal to 18.
# Therefore, age != 18 is True.


# ------------------------------------------------------------
# Example 14: Check temperature
# ------------------------------------------------------------

temperature = 35

if temperature > 30:
    print("Hot")
else:
    print("Normal")

# Output:
# Hot

# Reason:
# 35 > 30 is True.
# Therefore, "Hot" is printed.


# ------------------------------------------------------------
# Example 15: Check number range
# ------------------------------------------------------------

num = 50

if num >= 1 and num <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is outside the range")

# Output:
# Number is between 1 and 100

# Reason:
# 50 >= 1 is True.
# 50 <= 100 is also True.
# Both conditions are True because we used and.


# ------------------------------------------------------------
# Example 16: User input
# ------------------------------------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example Input:
# Enter your age: 20

# Output:
# You are an adult

# Reason:
# The input is converted from string to integer using int().
# 20 >= 18 is True, so the if block executes.


# ------------------------------------------------------------
# Example 17: User input - Even or Odd
# ------------------------------------------------------------

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example Input:
# Enter a number: 12

# Output:
# Even

# Reason:
# 12 % 2 gives 0.
# Therefore, the number is even.


# ------------------------------------------------------------
# Example 18: User input - Pass or Fail
# ------------------------------------------------------------

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Example Input:
# Enter your marks: 35

# Output:
# Fail

# Reason:
# 35 >= 40 is False.
# Therefore, the else block executes.


# ------------------------------------------------------------
# Example 19: Check divisible by 5
# ------------------------------------------------------------

num = 25

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# Output:
# Divisible by 5

# Reason:
# 25 % 5 gives 0.
# Therefore, 25 is divisible by 5.


# ------------------------------------------------------------
# Example 20: Check empty string
# ------------------------------------------------------------

name = "Sudhanshu"

if name:
    print("Name is available")
else:
    print("Name is empty")

# Output:
# Name is available

# Reason:
# The string contains a value, so it is treated as True.


# ------------------------------------------------------------
# Example 21: Check membership
# ------------------------------------------------------------

language = "Python"

if language in ["Python", "Java", "C++"]:
    print("Language is available")
else:
    print("Language is not available")

# Output:
# Language is available

# Reason:
# "Python" exists inside the list.
# Therefore, the condition is True.


# ------------------------------------------------------------
# Example 22: Simple login system
# ------------------------------------------------------------

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")

# Output:
# Login successful

# Reason:
# Both username and password are correct.
# Since both conditions are True, the complete condition is True.


# ------------------------------------------------------------
# Example 23: Check student eligibility
# ------------------------------------------------------------

marks = 75

if marks >= 60:
    print("Eligible")
else:
    print("Not eligible")

# Output:
# Eligible

# Reason:
# 75 >= 60 is True.
# Therefore, the student is eligible.


# ------------------------------------------------------------
# Example 24: Find greater number
# ------------------------------------------------------------

a = 100
b = 150

if a > b:
    print("a is greater")
else:
    print("b is greater or equal")

# Output:
# b is greater or equal

# Reason:
# 100 > 150 is False.
# Therefore, the else block executes.


# ------------------------------------------------------------
# Example 25: Interview-style example
# ------------------------------------------------------------

age = 22
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# Output:
# Entry allowed

# Reason:
# age >= 18 is True.
# has_id is also True.
# Both conditions are True, so entry is allowed.














'''NOTE:----Important point yaad rakhna


                    
if-else ka simple logic:

Condition True  →  if block
Condition False →  else block

Example:
age = 16if age >= 18:
    print("Adult")else:
            print("Minor")


Yahan dono blocks ek saath execute nahi hote. Condition ke according sirf ek block execute hota

'''