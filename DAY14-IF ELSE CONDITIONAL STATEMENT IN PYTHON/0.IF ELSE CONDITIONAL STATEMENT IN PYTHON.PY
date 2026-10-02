# ============================================================
# PYTHON CONDITIONAL STATEMENTS
# ============================================================


# ============================================================
# 1. IF STATEMENT
# ============================================================

# Definition:
# if is used to execute a block of code
# when a condition is True.

age = 20

if age >= 18:
    print("Adult")


# Output:
# Adult


# Reason:
# 20 >= 18 is True, so the if block executes.



# ============================================================
# 2. IF WITH COMPARISON OPERATORS
# ============================================================

# Comparison operators:
# ==   Equal to
# !=   Not equal to
# >    Greater than
# <    Less than
# >=   Greater than or equal to
# <=   Less than or equal to


a = 20
b = 10

if a > b:
    print("a is greater")


# Output:
# a is greater


# Reason:
# 20 is greater than 10.



# ============================================================
# 3. IF WITH ==
# ============================================================

number = 10

if number == 10:
    print("Number is 10")


# Output:
# Number is 10


# Reason:
# number is equal to 10.



# ============================================================
# 4. IF WITH !=
# ============================================================

age = 20

if age != 18:
    print("Age is not 18")


# Output:
# Age is not 18


# Reason:
# 20 is not equal to 18.



# ============================================================
# 5. IF WITH >=
# ============================================================

marks = 40

if marks >= 40:
    print("Passing marks")


# Output:
# Passing marks


# Reason:
# 40 is equal to the minimum required marks.



# ============================================================
# 6. IF WITH <=
# ============================================================

age = 18

if age <= 18:
    print("Allowed")


# Output:
# Allowed


# Reason:
# 18 is equal to 18.



# ============================================================
# 7. IF WITH MODULUS
# ============================================================

number = 10

if number % 2 == 0:
    print("Even number")


# Output:
# Even number


# Reason:
# 10 % 2 gives 0, so the number is even.



# ============================================================
# 8. IF-ELSE
# ============================================================

# Definition:
# if-else executes one block when the condition is True
# and another block when the condition is False.

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Output:
# Minor


# Reason:
# 16 >= 18 is False, so the else block executes.



# ============================================================
# 9. EVEN OR ODD USING IF-ELSE
# ============================================================

number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Output:
# Odd


# Reason:
# 7 % 2 gives 1, so the number is odd.



# ============================================================
# 10. POSITIVE OR NEGATIVE
# ============================================================

number = -5

if number >= 0:
    print("Positive")
else:
    print("Negative")


# Output:
# Negative


# Reason:
# -5 is less than 0.



# ============================================================
# 11. PASS OR FAIL
# ============================================================

marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# Output:
# Pass


# Reason:
# 75 is greater than or equal to 40.



# ============================================================
# 12. IF-ELIF-ELSE
# ============================================================

# Definition:
# elif means "else if".
# It is used when there are multiple conditions.

marks = 85

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("D")


# Output:
# B


# Reason:
# 85 is not >= 90.
# 85 >= 80 is True, so B is printed.



# ============================================================
# 13. MULTIPLE ELIF
# ============================================================

marks = 65

if marks >= 90:
    print("Excellent")
elif marks >= 80:
    print("Very Good")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")


# Output:
# Good


# Reason:
# 65 >= 60 is True.



# ============================================================
# 14. COMPARISON OPERATORS TOGETHER
# ============================================================

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# Output:
# False
# True
# False
# True
# False
# True


# Reason:
# Each operator compares a and b in a different way.



# ============================================================
# 15. LOGICAL OPERATOR - AND
# ============================================================

# and:
# Both conditions must be True.

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")


# Output:
# Entry allowed


# Reason:
# Both conditions are True.



# ============================================================
# 16. LOGICAL OPERATOR - OR
# ============================================================

# or:
# At least one condition must be True.

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")


# Output:
# Weekend


# Reason:
# day == "Sunday" is True.



# ============================================================
# 17. LOGICAL OPERATOR - NOT
# ============================================================

# not:
# It reverses the Boolean value.

logged_in = False

if not logged_in:
    print("Please login")


# Output:
# Please login


# Reason:
# logged_in is False.
# not False becomes True.



# ============================================================
# 18. AND WITH MULTIPLE CONDITIONS
# ============================================================

marks = 80
attendance = 85
assignment = True

if marks >= 40 and attendance >= 75 and assignment:
    print("Eligible")


# Output:
# Eligible


# Reason:
# All three conditions are True.



# ============================================================
# 19. AND + OR
# ============================================================

age = 20
student = True
working = False

if age >= 18 and (student or working):
    print("Eligible")


# Output:
# Eligible


# Reason:
# age >= 18 is True.
# student or working is True because student is True.



# ============================================================
# 20. NOT IN
# ============================================================

numbers = [10, 20, 30]

if 50 not in numbers:
    print("50 is not present")


# Output:
# 50 is not present


# Reason:
# 50 does not exist in the list.



# ============================================================
# 21. IN OPERATOR
# ============================================================

numbers = [10, 20, 30]

if 20 in numbers:
    print("20 is present")


# Output:
# 20 is present


# Reason:
# 20 exists in the list.



# ============================================================
# 22. STRING CONDITION
# ============================================================

username = "admin"

if username == "admin":
    print("Welcome Admin")
else:
    print("Access denied")


# Output:
# Welcome Admin


# Reason:
# username matches "admin".



# ============================================================
# 23. STRING METHOD + CONDITION
# ============================================================

name = "PYTHON"

if name.lower() == "python":
    print("Correct")


# Output:
# Correct


# Reason:
# lower() converts PYTHON to python.



# ============================================================
# 24. startswith() + CONDITION
# ============================================================

text = "Python Programming"

if text.startswith("Python"):
    print("Starts with Python")


# Output:
# Starts with Python


# Reason:
# The string starts with "Python".



# ============================================================
# 25. endswith() + CONDITION
# ============================================================

filename = "program.py"

if filename.endswith(".py"):
    print("Python file")


# Output:
# Python file


# Reason:
# The filename ends with ".py".



# ============================================================
# 26. isdigit() + CONDITION
# ============================================================

text = "12345"

if text.isdigit():
    print("Only digits")


# Output:
# Only digits


# Reason:
# The string contains only digits.



# ============================================================
# 27. isalpha() + CONDITION
# ============================================================

text = "Python"

if text.isalpha():
    print("Only alphabets")


# Output:
# Only alphabets


# Reason:
# The string contains only alphabetic characters.



# ============================================================
# 28. len() + CONDITION
# ============================================================

password = "python123"

if len(password) >= 8:
    print("Password length is valid")


# Output:
# Password length is valid


# Reason:
# The password contains 9 characters.



# ============================================================
# 29. USER INPUT + IF-ELSE
# ============================================================

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Example Input:
# 20

# Output:
# Adult


# Reason:
# 20 >= 18 is True.



# ============================================================
# 30. USER INPUT - EVEN OR ODD
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
# 24 % 2 gives 0.



# ============================================================
# 31. USER INPUT - PASS OR FAIL
# ============================================================

marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# Example Input:
# 75

# Output:
# Pass


# Reason:
# 75 >= 40 is True.



# ============================================================
# 32. GRADE SYSTEM
# ============================================================

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
else:
    print("Fail")


# Output:
# Grade B


# Reason:
# 85 is >= 80 but < 90.



# ============================================================
# 33. CONDITIONAL / TERNARY OPERATOR
# ============================================================

# Syntax:
# value_if_true if condition else value_if_false

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)


# Output:
# Adult


# Reason:
# age >= 18 is True,
# so "Adult" is selected.



# ============================================================
# 34. TERNARY - EVEN OR ODD
# ============================================================

number = 7

result = "Even" if number % 2 == 0 else "Odd"

print(result)


# Output:
# Odd


# Reason:
# 7 % 2 is 1, so "Odd" is selected.



# ============================================================
# 35. TERNARY - PASS OR FAIL
# ============================================================

marks = 75

result = "Pass" if marks >= 40 else "Fail"

print(result)


# Output:
# Pass


# Reason:
# marks >= 40 is True.



# ============================================================
# 36. NESTED IF
# ============================================================

# Definition:
# A nested if is an if statement inside another if statement.

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Not eligible")


# Output:
# Entry allowed


# Reason:
# First age >= 18 is True.
# Then has_id is also True.



# ============================================================
# 37. NESTED IF - ELSE CASE
# ============================================================

age = 20
has_id = False

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Not eligible")


# Output:
# ID required


# Reason:
# Age is valid but has_id is False.



# ============================================================
# 38. NESTED IF - LOGIN
# ============================================================

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")


# Output:
# Login successful


# Reason:
# Both username and password are correct.



# ============================================================
# 39. NESTED IF - MARKS
# ============================================================

marks = 85

if marks >= 40:
    if marks >= 75:
        print("Pass with distinction")
    else:
        print("Pass")
else:
    print("Fail")


# Output:
# Pass with distinction


# Reason:
# 85 is >= 40 and also >= 75.



# ============================================================
# 40. NESTED IF + LOGICAL OPERATOR
# ============================================================

age = 21
student = True

if age >= 18:
    if student and age <= 25:
        print("Eligible student")


# Output:
# Eligible student


# Reason:
# age >= 18 is True.
# student is True.
# age <= 25 is also True.



# ============================================================
# 41. MAXIMUM OF TWO NUMBERS
# ============================================================

a = 50
b = 30

if a > b:
    print("a is greater")
else:
    print("b is greater")


# Output:
# a is greater


# Reason:
# 50 is greater than 30.



# ============================================================
# 42. MAXIMUM OF THREE NUMBERS
# ============================================================

a = 50
b = 70
c = 40

if a > b and a > c:
    print("a is greatest")
elif b > a and b > c:
    print("b is greatest")
else:
    print("c is greatest")


# Output:
# b is greatest


# Reason:
# 70 is greater than both 50 and 40.



# ============================================================
# 43. RANGE CHECK
# ============================================================

number = 50

if number >= 1 and number <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is outside the range")


# Output:
# Number is between 1 and 100


# Reason:
# 50 satisfies both conditions.



# ============================================================
# 44. CHAINED COMPARISON
# ============================================================

age = 20

if 18 <= age <= 25:
    print("Age is between 18 and 25")


# Output:
# Age is between 18 and 25


# Reason:
# 20 satisfies both comparisons.



# ============================================================
# 45. LEAP YEAR
# ============================================================

year = 2024

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# Output:
# Leap year


# Reason:
# 2024 is divisible by 4 and is not a century year.



# ============================================================
# 46. DIVISIBILITY CHECK
# ============================================================

number = 50

if number % 10 == 0:
    print("Divisible by 10")
elif number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5 or 10")


# Output:
# Divisible by 10


# Reason:
# 50 % 10 gives 0.



# ============================================================
# 47. LOGIN SYSTEM
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
# Username and password both match.



# ============================================================
# 48. ELIGIBILITY CHECK
# ============================================================

marks = 85
attendance = 80
project_completed = True

if marks >= 40:
    if attendance >= 75:
        if project_completed:
            print("Eligible")
        else:
            print("Complete the project")
    else:
        print("Attendance is low")
else:
    print("Marks are low")


# Output:
# Eligible


# Reason:
# Marks, attendance and project requirements
# are all satisfied.



# ============================================================
# 49. MIXED CONDITIONAL PROGRAM
# ============================================================

marks = 85
attendance = 82
assignment = True

if marks >= 40:
    if attendance >= 75:
        if assignment:
            if marks >= 80:
                print("Excellent performance")
            elif marks >= 60:
                print("Good performance")
            else:
                print("Pass")
        else:
            print("Assignment incomplete")
    else:
        print("Attendance is low")
else:
    print("Failed")


# Output:
# Excellent performance


# Reason:
# marks >= 40        -> True
# attendance >= 75   -> True
# assignment         -> True
# marks >= 80        -> True
# Therefore the final block executes.



# ============================================================
# 50. FINAL INTERVIEW-STYLE QUESTION
# ============================================================

number = 120

if number > 0:
    if number % 2 == 0:
        if number % 5 == 0:
            print("Positive even number divisible by 5")


# Output:
# Positive even number divisible by 5


# Reason:
# 120 is positive.
# 120 is even.
# 120 is divisible by 5.
# Therefore all conditions are True.