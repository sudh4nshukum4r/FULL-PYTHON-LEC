# ============================================================
# LOGICAL OPERATORS
# ============================================================

# Definition:
# Logical operators are used to combine or modify conditions.
# They return either True or False.
#
# Python has three logical operators:
#
# and
# or
# not


# ============================================================
# 1. AND OPERATOR
# ============================================================

# Definition:
# The "and" operator returns True only when
# BOTH conditions are True.


# Syntax:
#
# condition1 and condition2


# ------------------------------------------------------------
# Example 1: Both conditions are True
# ------------------------------------------------------------

age = 20
has_id = True

print(age >= 18 and has_id)

# Output:
# True

# Reason:
# age >= 18 is True.
# has_id is also True.
# True and True = True.


# ------------------------------------------------------------
# Example 2: One condition is False
# ------------------------------------------------------------

age = 16
has_id = True

print(age >= 18 and has_id)

# Output:
# False

# Reason:
# age >= 18 is False.
# has_id is True.
# False and True = False.
# AND needs both conditions to be True.


# ------------------------------------------------------------
# Example 3: Both conditions are False
# ------------------------------------------------------------

age = 16
has_id = False

print(age >= 18 and has_id)

# Output:
# False

# Reason:
# Both conditions are False.
# Therefore, the complete result is False.


# ------------------------------------------------------------
# Example 4: AND with numbers
# ------------------------------------------------------------

num = 25

print(num > 10 and num < 30)

# Output:
# True

# Reason:
# 25 > 10 is True.
# 25 < 30 is also True.
# Therefore, True and True = True.


# ------------------------------------------------------------
# Example 5: AND inside if
# ------------------------------------------------------------

marks = 80
attendance = 90

if marks >= 40 and attendance >= 75:
    print("Eligible")

# Output:
# Eligible

# Reason:
# marks >= 40 is True.
# attendance >= 75 is True.
# Both conditions are True.


# ============================================================
# 2. OR OPERATOR
# ============================================================

# Definition:
# The "or" operator returns True when
# AT LEAST ONE condition is True.


# Syntax:
#
# condition1 or condition2


# ------------------------------------------------------------
# Example 6: One condition is True
# ------------------------------------------------------------

age = 20
has_id = False

print(age >= 18 or has_id)

# Output:
# True

# Reason:
# age >= 18 is True.
# has_id is False.
# True or False = True.
# OR needs at least one True condition.


# ------------------------------------------------------------
# Example 7: Both conditions are True
# ------------------------------------------------------------

a = 10
b = 20

print(a < 20 or b > 10)

# Output:
# True

# Reason:
# Both conditions are True.
# True or True = True.


# ------------------------------------------------------------
# Example 8: Both conditions are False
# ------------------------------------------------------------

a = 10
b = 20

print(a > 50 or b < 10)

# Output:
# False

# Reason:
# 10 > 50 is False.
# 20 < 10 is False.
# False or False = False.


# ------------------------------------------------------------
# Example 9: OR inside if
# ------------------------------------------------------------

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")

# Output:
# Weekend

# Reason:
# day == "Saturday" is False.
# day == "Sunday" is True.
# At least one condition is True.


# ============================================================
# 3. NOT OPERATOR
# ============================================================

# Definition:
# The "not" operator reverses the Boolean result.
#
# True  -> False
# False -> True


# Syntax:
#
# not condition


# ------------------------------------------------------------
# Example 10: NOT True
# ------------------------------------------------------------

is_raining = True

print(not is_raining)

# Output:
# False

# Reason:
# is_raining is True.
# not True becomes False.


# ------------------------------------------------------------
# Example 11: NOT False
# ------------------------------------------------------------

is_raining = False

print(not is_raining)

# Output:
# True

# Reason:
# is_raining is False.
# not False becomes True.


# ------------------------------------------------------------
# Example 12: NOT with comparison
# ------------------------------------------------------------

age = 20

print(not age < 18)

# Output:
# True

# Reason:
# age < 18 is False.
# not False becomes True.


# ------------------------------------------------------------
# Example 13: NOT inside if
# ------------------------------------------------------------

logged_in = False

if not logged_in:
    print("Please login")

# Output:
# Please login

# Reason:
# logged_in is False.
# not False becomes True.
# Therefore, the if block executes.


# ============================================================
# AND TRUTH TABLE
# ============================================================

# True  and True  -> True
# True  and False -> False
# False and True  -> False
# False and False -> False


# ============================================================
# OR TRUTH TABLE
# ============================================================

# True  or True  -> True
# True  or False -> True
# False or True  -> True
# False or False -> False


# ============================================================
# NOT TRUTH TABLE
# ============================================================

# not True  -> False
# not False -> True


# ============================================================
# MIXED LOGICAL OPERATORS
# ============================================================


# ------------------------------------------------------------
# Example 14: AND + OR
# ------------------------------------------------------------

age = 20
marks = 80

if age >= 18 and marks >= 40:
    print("Eligible")

# Output:
# Eligible

# Reason:
# Both conditions are True.


# ------------------------------------------------------------
# Example 15: OR + AND
# ------------------------------------------------------------

marks = 85
attendance = 60

if marks >= 80 or attendance >= 75:
    print("Selected")
else:
    print("Not selected")

# Output:
# Selected

# Reason:
# marks >= 80 is True.
# attendance >= 75 is False.
# True or False = True.


# ------------------------------------------------------------
# Example 16: NOT + AND
# ------------------------------------------------------------

is_blocked = False
has_account = True

if not is_blocked and has_account:
    print("Access allowed")
else:
    print("Access denied")

# Output:
# Access allowed

# Reason:
# is_blocked is False.
# not False becomes True.
# has_account is True.
# True and True = True.


# ============================================================
# LOGICAL OPERATORS WITH USER INPUT
# ============================================================


# ------------------------------------------------------------
# Example 17: Age and ID check
# ------------------------------------------------------------

age = int(input("Enter your age: "))
has_id = input("Do you have ID? ")

if age >= 18 and has_id == "yes":
    print("Entry allowed")
else:
    print("Entry denied")

# Example Input:
# Enter your age: 20
# Do you have ID? yes

# Output:
# Entry allowed

# Reason:
# Age is 20, so age >= 18 is True.
# ID is "yes", so the second condition is True.
# True and True = True.


# ------------------------------------------------------------
# Example 18: Student eligibility
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
# 70 >= 40 is True.
# 80 >= 75 is True.
# Therefore, both conditions are True.


# ------------------------------------------------------------
# Example 19: Weekend check
# ------------------------------------------------------------

day = input("Enter the day: ")

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

# Example Input:
# Enter the day: Sunday

# Output:
# Weekend

# Reason:
# day == "Sunday" is True.
# Therefore, OR gives True.


# ============================================================
# IMPORTANT EXAMPLE
# ============================================================


# ------------------------------------------------------------
# Example 20: Range checking using AND
# ------------------------------------------------------------

age = 25

if age >= 18 and age <= 60:
    print("Age is in the valid range")
else:
    print("Age is outside the range")

# Output:
# Age is in the valid range

# Reason:
# 25 >= 18 is True.
# 25 <= 60 is True.
# True and True = True.


# ------------------------------------------------------------
# Example 21: Multiple OR conditions
# ------------------------------------------------------------

language = "Python"

if language == "Python" or language == "Java" or language == "C++":
    print("Supported language")
else:
    print("Unsupported language")

# Output:
# Supported language

# Reason:
# language == "Python" is True.
# OR needs only one True condition.


# ============================================================
# INTERVIEW-STYLE EXAMPLE
# ============================================================


# ------------------------------------------------------------
# Example 22: Scholarship eligibility
# ------------------------------------------------------------

marks = 85
attendance = 80
discipline_issue = False

if marks >= 80 and attendance >= 75 and not discipline_issue:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")

# Output:
# Eligible for scholarship

# Reason:
# marks >= 80       -> True
# attendance >= 75  -> True
# discipline_issue  -> False
# not False         -> True
#
# Therefore:
# True and True and True = True







'''NOTE:---Sabse important shortcut



| Operator | Meaning | True kab hota hai? |

| `and`    | AND     | **Dono True** |
| `or`     | OR      | **At least one True** |
| `not`    | Reverse | True ↔ False |



'''



# AND → sabhi conditions True honi chahiye

# OR  → ek bhi condition True ho toh True

# # NOT → result ko ulta kar deta hai
