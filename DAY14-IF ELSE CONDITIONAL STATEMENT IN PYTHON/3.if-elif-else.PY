# ============================================================
# IF-ELIF-ELSE STATEMENT
# ============================================================

# Definition:
# The if-elif-else statement is used when we need to
# check multiple conditions.
#
# Python checks the conditions from top to bottom.
# The first condition that becomes True is executed.
# After that, the remaining conditions are skipped.


# Syntax:
#
# if condition1:
#     statement
# elif condition2:
#     statement
# elif condition3:
#     statement
# else:
#     statement


# ------------------------------------------------------------
# Example 1: Basic if-elif-else
# ------------------------------------------------------------

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# Output:
# Grade B

# Reason:
# 75 >= 90 is False.
# 75 >= 60 is True.
# Therefore, "Grade B" is printed.


# ------------------------------------------------------------
# Example 2: Three conditions
# ------------------------------------------------------------

age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

# Output:
# Adult

# Reason:
# 20 < 13 is False.
# 20 < 18 is also False.
# Therefore, else executes.


# ------------------------------------------------------------
# Example 3: Positive, negative or zero
# ------------------------------------------------------------

num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Output:
# Negative

# Reason:
# -5 > 0 is False.
# -5 < 0 is True.
# Therefore, "Negative" is printed.


# ------------------------------------------------------------
# Example 4: Check zero
# ------------------------------------------------------------

num = 0

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Output:
# Zero

# Reason:
# 0 > 0 is False.
# 0 < 0 is also False.
# Therefore, else executes.


# ------------------------------------------------------------
# Example 5: Grade system
# ------------------------------------------------------------

marks = 85

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")

# Output:
# A

# Reason:
# 85 >= 90 is False.
# 85 >= 80 is True.
# So Python prints "A" and stops checking further conditions.


# ------------------------------------------------------------
# Example 6: Multiple marks ranges
# ------------------------------------------------------------

marks = 55

if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Very Good")
elif marks >= 50:
    print("Good")
else:
    print("Needs Improvement")

# Output:
# Good

# Reason:
# 55 >= 90 is False.
# 55 >= 75 is False.
# 55 >= 50 is True.
# Therefore, "Good" is printed.


# ------------------------------------------------------------
# Example 7: Day number
# ------------------------------------------------------------

day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
else:
    print("Other day")

# Output:
# Wednesday

# Reason:
# day is 3.
# day == 3 is True.
# Therefore, "Wednesday" is printed.


# ------------------------------------------------------------
# Example 8: Traffic light
# ------------------------------------------------------------

light = "yellow"

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("Go")
else:
    print("Invalid light")

# Output:
# Wait

# Reason:
# light is "yellow".
# The second condition is True.
# Therefore, "Wait" is printed.


# ------------------------------------------------------------
# Example 9: Temperature
# ------------------------------------------------------------

temperature = 25

if temperature >= 35:
    print("Very Hot")
elif temperature >= 25:
    print("Warm")
elif temperature >= 15:
    print("Cool")
else:
    print("Cold")

# Output:
# Warm

# Reason:
# 25 >= 35 is False.
# 25 >= 25 is True.
# Therefore, "Warm" is printed.


# ------------------------------------------------------------
# Example 10: Number comparison
# ------------------------------------------------------------

a = 20
b = 20

if a > b:
    print("a is greater")
elif a < b:
    print("b is greater")
else:
    print("Both are equal")

# Output:
# Both are equal

# Reason:
# 20 > 20 is False.
# 20 < 20 is also False.
# Therefore, both numbers are equal.


# ------------------------------------------------------------
# Example 11: Check character
# ------------------------------------------------------------

letter = "B"

if letter == "A":
    print("First letter")
elif letter == "B":
    print("Second letter")
elif letter == "C":
    print("Third letter")
else:
    print("Other letter")

# Output:
# Second letter

# Reason:
# letter is "B".
# The second condition is True.


# ------------------------------------------------------------
# Example 12: User input grade system
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
# Enter your marks: 82

# Output:
# Grade A

# Reason:
# 82 >= 90 is False.
# 82 >= 80 is True.
# Therefore, Grade A is printed.


# ------------------------------------------------------------
# Example 13: User input age category
# ------------------------------------------------------------

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# Example Input:
# Enter your age: 20

# Output:
# Adult

# Reason:
# 20 is not less than 13.
# 20 is not less than 18.
# 20 is less than 60.
# Therefore, "Adult" is printed.


# ------------------------------------------------------------
# Example 14: Even, odd and zero
# ------------------------------------------------------------

num = 8

if num == 0:
    print("Zero")
elif num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output:
# Even

# Reason:
# num is not zero.
# 8 % 2 gives 0.
# Therefore, the number is even.


# ------------------------------------------------------------
# Example 15: Divisibility
# ------------------------------------------------------------

num = 15

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")

# Output:
# Divisible by both 3 and 5

# Reason:
# 15 is divisible by 3.
# 15 is also divisible by 5.
# Therefore, the first condition is True.


# ------------------------------------------------------------
# Example 16: Login status
# ------------------------------------------------------------

username = "admin"

if username == "admin":
    print("Admin Login")
elif username == "student":
    print("Student Login")
elif username == "teacher":
    print("Teacher Login")
else:
    print("Unknown User")

# Output:
# Admin Login

# Reason:
# username is "admin".
# The first condition is True.


# ------------------------------------------------------------
# Example 17: Simple calculator
# ------------------------------------------------------------

a = 10
b = 5
operator = "*"

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid operator")

# Output:
# 50

# Reason:
# operator is "*".
# Therefore, the multiplication condition executes.


# ------------------------------------------------------------
# Example 18: Month number
# ------------------------------------------------------------

month = 4

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
else:
    print("Other month")

# Output:
# April

# Reason:
# month is 4.
# Therefore, month == 4 is True.


# ------------------------------------------------------------
# Example 19: Performance level
# ------------------------------------------------------------

score = 92

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 50:
    print("Average")
else:
    print("Poor")

# Output:
# Excellent

# Reason:
# 92 >= 90 is True.
# Python executes the first block and skips the remaining elif blocks.


# ------------------------------------------------------------
# Example 20: Interview-style question
# ------------------------------------------------------------

marks = 78
attendance = 85

if marks >= 80 and attendance >= 75:
    print("Excellent performance")
elif marks >= 60 and attendance >= 75:
    print("Good performance")
elif marks >= 40:
    print("Average performance")
else:
    print("Needs improvement")

# Output:
# Good performance

# Reason:
# marks >= 80 is False.
# marks >= 60 is True.
# attendance >= 75 is also True.
# Therefore, the second condition executes.


# ------------------------------------------------------------
# IMPORTANT CONCEPT
# ------------------------------------------------------------

# Python checks if, then elif conditions from TOP to BOTTOM.
#
# The first True condition is executed.
# After that, Python does NOT check the remaining elif blocks.
#
# Example:

marks = 95

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("Fail")

# Output:
# A+

# Reason:
# marks >= 90 is already True.
# So Python prints A+ and stops checking the remaining conditions.

















'''NOTE:----Ek line mein yaad rakho

  
if       → first condition
elif     → another condition
elif     → another condition
else     → none of the above conditions are True

Main difference:
...
# if-else
if condition:
    ...
else:
    ...



➡️ 2 possible paths
# if-elif-else
if condition1:
    ...
elif condition2:
    ...
elif condition3:
    ...
else:
    ...



➡️ Multiple possible paths

'''