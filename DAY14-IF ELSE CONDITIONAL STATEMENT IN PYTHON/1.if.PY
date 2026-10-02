# ============================================================
# IF STATEMENT
# ============================================================

# Definition:
# The if statement is used to execute a block of code
# only when a given condition is True.


# Syntax:
#
# if condition:
#     statement


# ============================================================
# 1. BASIC IF
# ============================================================

age = 20

if age >= 18:
    print("Adult")


# Output:
# Adult


# Reason:
# age is 20 and 20 >= 18 is True,
# so the if block executes.



# ============================================================
# 2. IF WITH GREATER THAN
# ============================================================

a = 20
b = 10

if a > b:
    print("a is greater than b")


# Output:
# a is greater than b


# Reason:
# 20 is greater than 10.



# ============================================================
# 3. IF WITH LESS THAN
# ============================================================

a = 10
b = 20

if a < b:
    print("a is smaller than b")


# Output:
# a is smaller than b


# Reason:
# 10 is less than 20.



# ============================================================
# 4. IF WITH EQUAL TO
# ============================================================

number = 10

if number == 10:
    print("Number is 10")


# Output:
# Number is 10


# Reason:
# number is equal to 10.



# ============================================================
# 5. IF WITH NOT EQUAL TO
# ============================================================

age = 20

if age != 18:
    print("Age is not 18")


# Output:
# Age is not 18


# Reason:
# 20 is not equal to 18.



# ============================================================
# 6. IF WITH GREATER THAN OR EQUAL TO
# ============================================================

marks = 40

if marks >= 40:
    print("Passing marks reached")


# Output:
# Passing marks reached


# Reason:
# 40 is equal to 40,
# so the condition is True.



# ============================================================
# 7. IF WITH LESS THAN OR EQUAL TO
# ============================================================

age = 18

if age <= 18:
    print("Age is 18 or below")


# Output:
# Age is 18 or below


# Reason:
# 18 is equal to 18.



# ============================================================
# 8. IF CONDITION IS FALSE
# ============================================================

marks = 30

if marks >= 40:
    print("Pass")


# Output:
# No output


# Reason:
# 30 >= 40 is False,
# so the if block does not execute.



# ============================================================
# 9. IF WITH MODULUS
# ============================================================

number = 10

if number % 2 == 0:
    print("Even number")


# Output:
# Even number


# Reason:
# 10 % 2 gives 0,
# so the condition is True.



# ============================================================
# 10. CHECK POSITIVE NUMBER
# ============================================================

number = 25

if number > 0:
    print("Positive number")


# Output:
# Positive number


# Reason:
# 25 is greater than 0.



# ============================================================
# 11. CHECK NEGATIVE NUMBER
# ============================================================

number = -10

if number < 0:
    print("Negative number")


# Output:
# Negative number


# Reason:
# -10 is less than 0.



# ============================================================
# 12. CHECK ZERO
# ============================================================

number = 0

if number == 0:
    print("Number is zero")


# Output:
# Number is zero


# Reason:
# number is exactly equal to 0.



# ============================================================
# 13. IF WITH STRING
# ============================================================

name = "Sudhanshu"

if name == "Sudhanshu":
    print("Name matched")


# Output:
# Name matched


# Reason:
# The value of name is exactly "Sudhanshu".



# ============================================================
# 14. IF WITH STRING METHOD
# ============================================================

name = "PYTHON"

if name.lower() == "python":
    print("Correct")


# Output:
# Correct


# Reason:
# lower() converts "PYTHON" into "python",
# so the condition becomes True.



# ============================================================
# 15. IF WITH startswith()
# ============================================================

text = "Python Programming"

if text.startswith("Python"):
    print("Starts with Python")


# Output:
# Starts with Python


# Reason:
# The string starts with "Python".



# ============================================================
# 16. IF WITH endswith()
# ============================================================

filename = "program.py"

if filename.endswith(".py"):
    print("Python file")


# Output:
# Python file


# Reason:
# The filename ends with ".py".



# ============================================================
# 17. IF WITH isdigit()
# ============================================================

text = "12345"

if text.isdigit():
    print("Only digits")


# Output:
# No output


# Reason:
# isdigit is a method.
# It must be called using isdigit().



# Correct version:

text = "12345"

if text.isdigit():
    print("Only digits")


# Output:
# Only digits


# Reason:
# isdigit() returns True because the string
# contains only digits.



# ============================================================
# 18. IF WITH isalpha()
# ============================================================

text = "Python"

if text.isalpha():
    print("Only alphabets")


# Output:
# Only alphabets


# Reason:
# The string contains only alphabetic characters.



# ============================================================
# 19. IF WITH len()
# ============================================================

password = "python123"

if len(password) >= 8:
    print("Password length is valid")


# Output:
# Password length is valid


# Reason:
# password contains 9 characters,
# which is greater than or equal to 8.



# ============================================================
# 20. IF WITH IN
# ============================================================

numbers = [10, 20, 30]

if 20 in numbers:
    print("20 is present")


# Output:
# 20 is present


# Reason:
# 20 exists inside the list.



# ============================================================
# 21. IF WITH USER INPUT
# ============================================================

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible")


# Example Input:
# 20

# Output:
# Eligible


# Reason:
# 20 >= 18 is True.



# ============================================================
# 22. USER INPUT - EVEN NUMBER
# ============================================================

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")


# Example Input:
# 24

# Output:
# Even


# Reason:
# 24 % 2 gives 0.



# ============================================================
# 23. USER INPUT - PASSING MARKS
# ============================================================

marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")


# Example Input:
# 75

# Output:
# Pass


# Reason:
# 75 is greater than or equal to 40.



# ============================================================
# 24. IF WITH MULTIPLE CONDITIONS
# ============================================================

marks = 85
attendance = 80

if marks >= 40 and attendance >= 75:
    print("Eligible")


# Output:
# Eligible


# Reason:
# Both conditions are True.



# ============================================================
# 25. INTERVIEW-STYLE IF
# ============================================================

number = 120

if number > 0 and number % 2 == 0 and number % 5 == 0:
    print("Positive even number divisible by 5")


# Output:
# Positive even number divisible by 5


# Reason:
# 120 is positive,
# 120 is even,
# and 120 is divisible by 5.
# Therefore all conditions are True.



'''RULE:-----
 1. Condition ke baad colon :
    if age >= 18:

 2. Code indented hona chahiye
    if age >= 18:
    print("Adult")

 3. True condition par block chalega

 4. False condition par if block skip ho jayega
'''