# ============================================================
# COMPARISON OPERATORS
# ============================================================

# Definition:
# Comparison operators are used to compare two values.
# The result of a comparison is always either True or False.


# Main Comparison Operators:
#
# ==   Equal to
# !=   Not equal to
# >    Greater than
# <    Less than
# >=   Greater than or equal to
# <=   Less than or equal to


# ------------------------------------------------------------
# Example 1: Equal to (==)
# ------------------------------------------------------------

a = 10
b = 10

print(a == b)

# Output:
# True

# Reason:
# Both a and b have the value 10.
# Therefore, 10 == 10 is True.


# ------------------------------------------------------------
# Example 2: Equal to - False
# ------------------------------------------------------------

a = 10
b = 20

print(a == b)

# Output:
# False

# Reason:
# 10 and 20 are different values.
# Therefore, 10 == 20 is False.


# ------------------------------------------------------------
# Example 3: Not equal to (!=)
# ------------------------------------------------------------

a = 10
b = 20

print(a != b)

# Output:
# True

# Reason:
# 10 and 20 are different.
# Therefore, they are not equal.


# ------------------------------------------------------------
# Example 4: Not equal to - False
# ------------------------------------------------------------

a = 10
b = 10

print(a != b)

# Output:
# False

# Reason:
# Both values are 10.
# Therefore, they are equal, so != is False.


# ------------------------------------------------------------
# Example 5: Greater than (>)
# ------------------------------------------------------------

a = 20
b = 10

print(a > b)

# Output:
# True

# Reason:
# 20 is greater than 10.
# Therefore, 20 > 10 is True.


# ------------------------------------------------------------
# Example 6: Greater than - False
# ------------------------------------------------------------

a = 10
b = 20

print(a > b)

# Output:
# False

# Reason:
# 10 is not greater than 20.


# ------------------------------------------------------------
# Example 7: Less than (<)
# ------------------------------------------------------------

a = 10
b = 20

print(a < b)

# Output:
# True

# Reason:
# 10 is less than 20.


# ------------------------------------------------------------
# Example 8: Less than - False
# ------------------------------------------------------------

a = 20
b = 10

print(a < b)

# Output:
# False

# Reason:
# 20 is not less than 10.


# ------------------------------------------------------------
# Example 9: Greater than or equal to (>=)
# ------------------------------------------------------------

marks = 80

print(marks >= 80)

# Output:
# True

# Reason:
# marks is exactly 80.
# >= allows both greater than and equal to.


# ------------------------------------------------------------
# Example 10: Greater than or equal to
# ------------------------------------------------------------

marks = 90

print(marks >= 80)

# Output:
# True

# Reason:
# 90 is greater than 80.
# Therefore, the result is True.


# ------------------------------------------------------------
# Example 11: Greater than or equal to - False
# ------------------------------------------------------------

marks = 70

print(marks >= 80)

# Output:
# False

# Reason:
# 70 is neither greater than nor equal to 80.


# ------------------------------------------------------------
# Example 12: Less than or equal to (<=)
# ------------------------------------------------------------

age = 18

print(age <= 18)

# Output:
# True

# Reason:
# age is exactly 18.
# <= allows both less than and equal to.


# ------------------------------------------------------------
# Example 13: Less than or equal to
# ------------------------------------------------------------

age = 15

print(age <= 18)

# Output:
# True

# Reason:
# 15 is less than 18.


# ------------------------------------------------------------
# Example 14: Less than or equal to - False
# ------------------------------------------------------------

age = 25

print(age <= 18)

# Output:
# False

# Reason:
# 25 is greater than 18.


# ------------------------------------------------------------
# Example 15: Comparing strings
# ------------------------------------------------------------

name1 = "Python"
name2 = "Python"

print(name1 == name2)

# Output:
# True

# Reason:
# Both strings contain the same text.


# ------------------------------------------------------------
# Example 16: Different strings
# ------------------------------------------------------------

name1 = "Python"
name2 = "Java"

print(name1 == name2)

# Output:
# False

# Reason:
# "Python" and "Java" are different strings.


# ------------------------------------------------------------
# Example 17: String not equal
# ------------------------------------------------------------

language = "Python"

print(language != "Java")

# Output:
# True

# Reason:
# "Python" is not equal to "Java".


# ------------------------------------------------------------
# Example 18: Comparison inside if
# ------------------------------------------------------------

age = 20

if age >= 18:
    print("Adult")

# Output:
# Adult

# Reason:
# The comparison age >= 18 produces True.
# Therefore, the if block executes.


# ------------------------------------------------------------
# Example 19: Multiple comparisons
# ------------------------------------------------------------

a = 10
b = 20
c = 30

print(a < b)
print(b < c)
print(a < c)

# Output:
# True
# True
# True

# Reason:
# 10 < 20 is True.
# 20 < 30 is True.
# 10 < 30 is True.


# ------------------------------------------------------------
# Example 20: Compare two numbers using if-else
# ------------------------------------------------------------

a = 50
b = 30

if a > b:
    print("a is greater")
else:
    print("b is greater or equal")

# Output:
# a is greater

# Reason:
# 50 > 30 is True.
# Therefore, the if block executes.


# ------------------------------------------------------------
# Example 21: Check passing marks
# ------------------------------------------------------------

marks = 40

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Output:
# Pass

# Reason:
# 40 is exactly equal to the passing marks.
# >= includes equality.


# ------------------------------------------------------------
# Example 22: Check age range
# ------------------------------------------------------------

age = 20

print(age >= 18)
print(age <= 60)

# Output:
# True
# True

# Reason:
# 20 is greater than or equal to 18.
# 20 is also less than or equal to 60.


# ------------------------------------------------------------
# Example 23: Chained comparison
# ------------------------------------------------------------

age = 25

print(18 <= age <= 60)

# Output:
# True

# Reason:
# Python checks both conditions:
# 18 <= 25
# 25 <= 60
# Both are True.


# ------------------------------------------------------------
# Example 24: Chained comparison - False
# ------------------------------------------------------------

age = 70

print(18 <= age <= 60)

# Output:
# False

# Reason:
# 18 <= 70 is True.
# But 70 <= 60 is False.
# Therefore, the complete comparison is False.


# ------------------------------------------------------------
# Example 25: User input comparison
# ------------------------------------------------------------

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
else:
    print("Zero or Negative")

# Example Input:
# Enter a number: 15

# Output:
# Positive

# Reason:
# 15 > 0 is True.


# ------------------------------------------------------------
# Example 26: Compare marks
# ------------------------------------------------------------

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("You passed")
else:
    print("You failed")

# Example Input:
# Enter your marks: 35

# Output:
# You failed

# Reason:
# 35 >= 40 is False.
# Therefore, the else block executes.


# ============================================================
# VERY IMPORTANT DIFFERENCE
# ============================================================

# =   means assignment
# ==  means comparison


x = 10

# Here = assigns 10 to x.

print(x == 10)

# Output:
# True

# Reason:
# == checks whether x is equal to 10.











'''NOTE:-----Sabse important table

| Operator   |   Meaning   |   Example    |  Result |


| `==`       |    Equal to | `10 == 10`   | `True` |

| `!=`       | Not equal   | `10 != 20`   | `True` |

| `>`        | Greater than | `20 > 10`   | `True` |

| `<`        | Less than    | `10 < 20`   | `True` |

| `>=`       | Greater/equal | `20 >= 20` | `True` |

| `<=`        | Less/equal   | `20 <= 20` | `True` |


'''




# #Ek mistake bilkul mat karna:

# x = 10      # value assign karna

# x == 10     # value compare karna

# = → assign
# == → compare