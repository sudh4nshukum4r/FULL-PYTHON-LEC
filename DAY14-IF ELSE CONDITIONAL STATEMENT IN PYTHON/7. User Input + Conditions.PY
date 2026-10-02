# ============================================================
# USER INPUT + CONDITIONS
# ============================================================

# Definition:
# User input allows a Python program to take information
# from the user while the program is running.
#
# input() is used to take input from the user.
#
# Important:
# input() always returns a string.
# If we need a number, we usually convert it using int()
# or float().


# Syntax:
#
# variable = input("Message: ")
#
# For integer:
# variable = int(input("Message: "))
#
# For decimal:
# variable = float(input("Message: "))


# ============================================================
# 1. BASIC STRING INPUT
# ============================================================


# ------------------------------------------------------------
# Example 1: Take name as input
# ------------------------------------------------------------

name = input("Enter your name: ")

print("Hello", name)

# Example Input:
# Enter your name: Sudhanshu

# Output:
# Hello Sudhanshu

# Reason:
# input() takes the user's name and stores it in name.


# ------------------------------------------------------------
# Example 2: Input with if
# ------------------------------------------------------------

name = input("Enter your name: ")

if name == "Sudhanshu":
    print("Welcome Sudhanshu")
else:
    print("Welcome User")

# Example Input:
# Enter your name: Sudhanshu

# Output:
# Welcome Sudhanshu

# Reason:
# The entered name is equal to "Sudhanshu".
# Therefore, the if condition is True.


# ============================================================
# 2. INTEGER INPUT
# ============================================================


# ------------------------------------------------------------
# Example 3: Take age as integer
# ------------------------------------------------------------

age = int(input("Enter your age: "))

print(age)

# Example Input:
# Enter your age: 20

# Output:
# 20

# Reason:
# int() converts the input from string to integer.


# ------------------------------------------------------------
# Example 4: Age condition
# ------------------------------------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Example Input:
# Enter your age: 20

# Output:
# Adult

# Reason:
# 20 >= 18 is True.
# Therefore, the if block executes.


# ------------------------------------------------------------
# Example 5: Even or odd
# ------------------------------------------------------------

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example Input:
# Enter a number: 14

# Output:
# Even

# Reason:
# 14 % 2 gives 0.
# Therefore, the number is even.


# ============================================================
# 3. MARKS + CONDITIONS
# ============================================================


# ------------------------------------------------------------
# Example 6: Pass or fail
# ------------------------------------------------------------

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Example Input:
# Enter your marks: 65

# Output:
# Pass

# Reason:
# 65 >= 40 is True.


# ------------------------------------------------------------
# Example 7: Grade system
# ------------------------------------------------------------

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")

# Example Input:
# Enter your marks: 85

# Output:
# Grade A

# Reason:
# 85 >= 90 is False.
# 85 >= 80 is True.
# Therefore, Grade A is printed.


# ------------------------------------------------------------
# Example 8: Performance level
# ------------------------------------------------------------

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Very Good")
elif marks >= 50:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

# Example Input:
# Enter your marks: 55

# Output:
# Good

# Reason:
# 55 >= 90 -> False
# 55 >= 75 -> False
# 55 >= 50 -> True
# Therefore, "Good" is printed.


# ============================================================
# 4. FLOAT INPUT
# ============================================================


# ------------------------------------------------------------
# Example 9: Temperature
# ------------------------------------------------------------

temperature = float(input("Enter temperature: "))

if temperature >= 30:
    print("Hot")
else:
    print("Normal")

# Example Input:
# Enter temperature: 32.5

# Output:
# Hot

# Reason:
# 32.5 >= 30 is True.


# ------------------------------------------------------------
# Example 10: Decimal price
# ------------------------------------------------------------

price = float(input("Enter price: "))

if price >= 1000:
    print("Expensive")
else:
    print("Affordable")

# Example Input:
# Enter price: 750.50

# Output:
# Affordable

# Reason:
# 750.50 >= 1000 is False.
# Therefore, else executes.


# ============================================================
# 5. STRING INPUT + CONDITIONS
# ============================================================


# ------------------------------------------------------------
# Example 11: Check programming language
# ------------------------------------------------------------

language = input("Enter your programming language: ")

if language == "Python":
    print("Python selected")
else:
    print("Another language selected")

# Example Input:
# Enter your programming language: Python

# Output:
# Python selected

# Reason:
# The entered value is exactly "Python".


# ------------------------------------------------------------
# Example 12: Case-insensitive input
# ------------------------------------------------------------

language = input("Enter your language: ")

if language.lower() == "python":
    print("Python selected")
else:
    print("Different language")

# Example Input:
# Enter your language: PYTHON

# Output:
# Python selected

# Reason:
# .lower() converts "PYTHON" into "python".
# Therefore, the comparison becomes True.


# ------------------------------------------------------------
# Example 13: Yes or No
# ------------------------------------------------------------

answer = input("Do you like Python? ")

if answer.lower() == "yes":
    print("Great!")
else:
    print("Keep practicing!")

# Example Input:
# Do you like Python? YES

# Output:
# Great!

# Reason:
# answer.lower() converts "YES" into "yes".
# Therefore, the condition is True.


# ============================================================
# 6. MULTIPLE CONDITIONS WITH USER INPUT
# ============================================================


# ------------------------------------------------------------
# Example 14: Age + ID
# ------------------------------------------------------------

age = int(input("Enter your age: "))
has_id = input("Do you have ID? ")

if age >= 18 and has_id.lower() == "yes":
    print("Entry allowed")
else:
    print("Entry denied")

# Example Input:
# Enter your age: 20
# Do you have ID? yes

# Output:
# Entry allowed

# Reason:
# age >= 18 is True.
# has_id == "yes" is True.
# True and True = True.


# ------------------------------------------------------------
# Example 15: Marks + attendance
# ------------------------------------------------------------

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

if marks >= 40 and attendance >= 75:
    print("Eligible for exam")
else:
    print("Not eligible for exam")

# Example Input:
# Enter marks: 70
# Enter attendance: 80

# Output:
# Eligible for exam

# Reason:
# Both conditions are True.


# ------------------------------------------------------------
# Example 16: Scholarship condition
# ------------------------------------------------------------

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

if marks >= 80 and attendance >= 75:
    print("Scholarship eligible")
else:
    print("Scholarship not available")

# Example Input:
# Enter marks: 85
# Enter attendance: 80

# Output:
# Scholarship eligible

# Reason:
# 85 >= 80 is True.
# 80 >= 75 is True.
# Therefore, both conditions are True.


# ============================================================
# 7. USER INPUT + IN / NOT IN
# ============================================================


# ------------------------------------------------------------
# Example 17: Check allowed language
# ------------------------------------------------------------

language = input("Enter language: ")

if language in ["Python", "Java", "C++"]:
    print("Supported language")
else:
    print("Unsupported language")

# Example Input:
# Enter language: Python

# Output:
# Supported language

# Reason:
# "Python" exists inside the list.


# ------------------------------------------------------------
# Example 18: Check username
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
# 8. USER INPUT + CALCULATOR
# ============================================================


# ------------------------------------------------------------
# Example 19: Simple calculator
# ------------------------------------------------------------

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

# Example Input:
# Enter first number: 10
# Enter second number: 5
# Enter operator (+, -, *, /): *

# Output:
# Result: 50.0

# Reason:
# operator is "*".
# Therefore, multiplication is performed.


# ============================================================
# 9. USER INPUT + RANGE
# ============================================================


# ------------------------------------------------------------
# Example 20: Age category
# ------------------------------------------------------------

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Example Input:
# Enter your age: 20

# Output:
# Adult

# Reason:
# 20 is not less than 13.
# 20 is not less than 18.
# 20 is less than 60.
# Therefore, Adult is printed.


# ------------------------------------------------------------
# Example 21: Number range
# ------------------------------------------------------------

num = int(input("Enter a number: "))

if 1 <= num <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is outside the range")

# Example Input:
# Enter a number: 50

# Output:
# Number is between 1 and 100

# Reason:
# 1 <= 50 is True.
# 50 <= 100 is also True.
# Therefore, the number is inside the range.


# ============================================================
# 10. USER INPUT + STRING METHODS
# ============================================================


# ------------------------------------------------------------
# Example 22: Check email
# ------------------------------------------------------------

email = input("Enter your email: ")

if "@" in email:
    print("Valid format")
else:
    print("Invalid format")

# Example Input:
# Enter your email: student@gmail.com

# Output:
# Valid format

# Reason:
# "@" exists inside the entered string.


# ------------------------------------------------------------
# Example 23: Check password length
# ------------------------------------------------------------

password = input("Enter password: ")

if len(password) >= 8:
    print("Password length is valid")
else:
    print("Password is too short")

# Example Input:
# Enter password: python123

# Output:
# Password length is valid

# Reason:
# "python123" contains 9 characters.
# 9 >= 8 is True.


# ------------------------------------------------------------
# Example 24: Check digits
# ------------------------------------------------------------

text = input("Enter something: ")

if text.isdigit():
    print("Only digits")
else:
    print("Contains non-digit characters")

# Example Input:
# Enter something: 12345

# Output:
# Only digits

# Reason:
# .isdigit() returns True because every character is a digit.


# ============================================================
# 11. INTERVIEW-STYLE EXAMPLE
# ============================================================


# ------------------------------------------------------------
# Example 25: Student result system
# ------------------------------------------------------------

name = input("Enter student name: ")
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

if marks >= 40 and attendance >= 75:
    print(name, "has passed and is eligible.")
elif marks < 40:
    print(name, "has failed.")
else:
    print(name, "has passed but attendance is low.")

# Example Input:
# Enter student name: Rahul
# Enter marks: 65
# Enter attendance: 80

# Output:
# Rahul has passed and is eligible.

# Reason:
# marks >= 40 is True.
# attendance >= 75 is True.
# Therefore, the first condition executes.


# ============================================================
# IMPORTANT CONCEPT
# ============================================================

# input() always returns a STRING.

age = input("Enter age: ")

# Even if the user enters:
# 20
#
# Python initially receives:
# "20"
#
# So for mathematical comparison, convert it:

age = int(input("Enter age: "))

# Now age becomes:
# 20
#
# and we can do:
#
# age >= 18
#
# correctly.


# ============================================================
# QUICK REVISION
# ============================================================

# String input:
# name = input("Enter name: ")
#
# Integer input:
# age = int(input("Enter age: "))
#
# Decimal input:
# price = float(input("Enter price: "))
#
# Condition:
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")










'''NOTE:---Sabse important concept

age = input("Enter age: ")


Yahan user 20 enter karega, 
lekin Python ko initially "20" string milega.



ISLIYE:--  

age = int(input("Enter age: "))

karne se "20" → 20 integer ban jaata hai.

'''



# Yaad rakh:

'''
input()       → String
int(input())  → Integer
float(input()) → Decimal number

'''




