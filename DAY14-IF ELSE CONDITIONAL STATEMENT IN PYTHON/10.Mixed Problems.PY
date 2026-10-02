# ============================================================
# PYTHON CONDITIONAL STATEMENTS - MIXED PROBLEMS
# ============================================================


# ============================================================
# QUESTION 1 - POSITIVE / NEGATIVE / ZERO
# ============================================================

number = 10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Output:
# Positive

# Reason:
# 10 is greater than 0, so the first condition is True.


# ============================================================
# QUESTION 2 - EVEN OR ODD
# ============================================================

number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output:
# Odd

# Reason:
# 17 % 2 is 1, so the number is odd.


# ============================================================
# QUESTION 3 - PASS OR FAIL
# ============================================================

marks = 65

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Output:
# Pass

# Reason:
# 65 is greater than or equal to 40.


# ============================================================
# QUESTION 4 - GRADE SYSTEM
# ============================================================

marks = 86

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

# Output:
# Grade: A

# Reason:
# 86 is less than 90 but greater than or equal to 80.


# ============================================================
# QUESTION 5 - AGE CATEGORY
# ============================================================

age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# Output:
# Adult

# Reason:
# 20 is greater than or equal to 18 and less than 60.


# ============================================================
# QUESTION 6 - GREATER NUMBER
# ============================================================

a = 50
b = 30

if a > b:
    print("A is greater")
elif b > a:
    print("B is greater")
else:
    print("Both are equal")

# Output:
# A is greater

# Reason:
# 50 is greater than 30.


# ============================================================
# QUESTION 7 - LARGEST OF THREE NUMBERS
# ============================================================

a = 20
b = 50
c = 35

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)

# Output:
# Largest: 50

# Reason:
# 50 is greater than both 20 and 35.


# ============================================================
# QUESTION 8 - AGE + ID CHECK
# ============================================================

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Age requirement not satisfied")

# Output:
# Entry allowed

# Reason:
# Age is 18+ and the person has an ID.


# ============================================================
# QUESTION 9 - MARKS + ATTENDANCE
# ============================================================

marks = 70
attendance = 80

if marks >= 40:
    if attendance >= 75:
        print("Eligible")
    else:
        print("Attendance too low")
else:
    print("Marks too low")

# Output:
# Eligible

# Reason:
# Marks are 40+ and attendance is 75+.


# ============================================================
# QUESTION 10 - LOGIN SYSTEM
# ============================================================

username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# Output:
# Login successful

# Reason:
# Both username and password match the expected values.


# ============================================================
# QUESTION 11 - USER INPUT EVEN / ODD
# ============================================================

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example Input:
# 24

# Output:
# Even

# Reason:
# 24 is completely divisible by 2.


# ============================================================
# QUESTION 12 - USER INPUT PASS / FAIL
# ============================================================

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Example Input:
# 35

# Output:
# Fail

# Reason:
# 35 is less than the passing mark 40.


# ============================================================
# QUESTION 13 - USER INPUT GRADE
# ============================================================

marks = int(input("Enter marks: "))

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")

# Example Input:
# 92

# Output:
# A+

# Reason:
# 92 is greater than or equal to 90.


# ============================================================
# QUESTION 14 - NUMBER RANGE
# ============================================================

number = 75

if 1 <= number <= 100:
    print("Number is in range")
else:
    print("Number is out of range")

# Output:
# Number is in range

# Reason:
# 75 is between 1 and 100.


# ============================================================
# QUESTION 15 - LOGIN + ROLE
# ============================================================

username = "admin"
password = "1234"
role = "admin"

if username == "admin" and password == "1234":
    if role == "admin":
        print("Welcome Admin")
    else:
        print("Welcome User")
else:
    print("Login failed")

# Output:
# Welcome Admin

# Reason:
# Login details are correct and the role is admin.


# ============================================================
# QUESTION 16 - MEMBERSHIP OPERATOR
# ============================================================

languages = ["Python", "Java", "C++"]

language = "Python"

if language in languages:
    print("Language is available")
else:
    print("Language is not available")

# Output:
# Language is available

# Reason:
# "Python" exists inside the list.


# ============================================================
# QUESTION 17 - NOT IN
# ============================================================

blocked_users = ["Rahul", "Aman", "Rohit"]

username = "Sudhanshu"

if username not in blocked_users:
    print("User is allowed")
else:
    print("User is blocked")

# Output:
# User is allowed

# Reason:
# "Sudhanshu" is not present in blocked_users.


# ============================================================
# QUESTION 18 - STRING CHECK
# ============================================================

email = "student@gmail.com"

if "@" in email:
    print("Valid email format")
else:
    print("Invalid email format")

# Output:
# Valid email format

# Reason:
# The email contains the "@" character.


# ============================================================
# QUESTION 19 - TERNARY OPERATOR
# ============================================================

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)

# Output:
# Adult

# Reason:
# age >= 18 is True, so "Adult" is selected.


# ============================================================
# QUESTION 20 - EVEN / ODD USING TERNARY
# ============================================================

number = 11

result = "Even" if number % 2 == 0 else "Odd"

print(result)

# Output:
# Odd

# Reason:
# 11 is not completely divisible by 2.


# ============================================================
# QUESTION 21 - LOGICAL OPERATORS
# ============================================================

age = 22
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# Output:
# Entry allowed

# Reason:
# Both conditions are True.


# ============================================================
# QUESTION 22 - OR OPERATOR
# ============================================================

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

# Output:
# Weekend

# Reason:
# Saturday is one of the two weekend days.


# ============================================================
# QUESTION 23 - NOT OPERATOR
# ============================================================

is_blocked = False

if not is_blocked:
    print("Access allowed")
else:
    print("Access denied")

# Output:
# Access allowed

# Reason:
# is_blocked is False.
# not False becomes True.


# ============================================================
# QUESTION 24 - DIVISIBLE BY 3 AND 5
# ============================================================

number = 30

if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5")
elif number % 3 == 0:
    print("Divisible by 3")
elif number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")

# Output:
# Divisible by both 3 and 5

# Reason:
# 30 % 3 = 0 and 30 % 5 = 0.


# ============================================================
# QUESTION 25 - STUDENT ELIGIBILITY
# ============================================================

marks = 75
attendance = 82
assignment_submitted = True

if marks >= 40:
    if attendance >= 75:
        if assignment_submitted:
            print("Student is eligible")
        else:
            print("Submit assignment")
    else:
        print("Attendance too low")
else:
    print("Marks too low")

# Output:
# Student is eligible

# Reason:
# Marks, attendance and assignment conditions are all satisfied.


# ============================================================
# QUESTION 26 - NUMBER CLASSIFICATION
# ============================================================

number = -10

if number > 0:
    if number % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif number < 0:
    if number % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero")

# Output:
# Negative Even

# Reason:
# -10 is negative and divisible by 2.


# ============================================================
# QUESTION 27 - PASSWORD STRENGTH
# ============================================================

password = "python123"

if len(password) >= 8:
    if any(char.isdigit() for char in password):
        print("Password meets basic requirements")
    else:
        print("Password should contain a number")
else:
    print("Password is too short")

# Output:
# Password meets basic requirements

# Reason:
# Password length is at least 8 and it contains a digit.


# ============================================================
# QUESTION 28 - SIMPLE CALCULATOR
# ============================================================

a = 20
b = 5
operator = "/"

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

# Output:
# 4.0

# Reason:
# Operator is "/" and b is not zero, so division is performed.


# ============================================================
# QUESTION 29 - INTERVIEW STYLE PROBLEM
# ============================================================

age = 21
marks = 78
skills = ["Python", "HTML"]

if age >= 18:
    if marks >= 60:
        if "Python" in skills:
            print("Candidate meets the basic criteria")
        else:
            print("Python skill required")
    else:
        print("Marks requirement not satisfied")
else:
    print("Age requirement not satisfied")

# Output:
# Candidate meets the basic criteria

# Reason:
# Age, marks and Python-skill conditions are all satisfied.


# ============================================================
# QUESTION 30 - FINAL MIXED PROBLEM
# ============================================================

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif attendance < 0 or attendance > 100:
    print("Invalid attendance")
else:
    if marks >= 40:
        if attendance >= 75:
            if marks >= 80:
                print("Pass - Excellent performance")
            else:
                print("Pass - Good performance")
        else:
            print("Not eligible due to low attendance")
    else:
        print("Fail")

# Example Input:
# Enter marks: 85
# Enter attendance: 80

# Output:
# Pass - Excellent performance

# Reason:
# Marks valid hain, attendance valid hai,
# marks 40+ hain, attendance 75+ hai,
# aur marks 80+ hain.


# ============================================================
# FINAL CONCEPT REVISION
# ============================================================

# 1. if
#    Ek condition check karta hai.
#
# 2. if-else
#    True ya False ke basis par decision leta hai.
#
# 3. if-elif-else
#    Multiple conditions me se suitable block choose karta hai.
#
# 4. Comparison operators
#    ==, !=, >, <, >=, <=
#
# 5. Logical operators
#    and, or, not
#
# 6. Membership operators
#    in, not in
#
# 7. User input
#    input(), int(input()), float(input())
#
# 8. Ternary
#    value_if_true if condition else value_if_false
#
# 9. Nested if
#    Ek if ke andar doosra if.
#
# 10. Mixed problems
#     In sab concepts ko ek problem me combine karna.


# ============================================================
# GOLDEN RULE
# ============================================================

# Condition ko pehle samjho.
# Phir operators choose karo.
# Phir if/elif/else structure banao.
# Input ho to input ka datatype check karo.
# Complex condition ho to logical operators use karo.
# Multiple dependent checks ho to nested if use kar sakte ho.