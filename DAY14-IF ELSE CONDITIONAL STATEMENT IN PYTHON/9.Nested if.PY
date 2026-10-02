# ============================================================
# PYTHON - NESTED IF
# ============================================================

# ------------------------------------------------------------
# DEFINITION
# ------------------------------------------------------------
# Nested if means putting one if statement inside another if.
#
# Simple meaning:
# Ek condition ke andar doosri condition check karna.
#
# Example:
#
# if condition1:
#     if condition2:
#         statement
#
# Pehle outer condition check hogi.
# Agar outer condition True hai tabhi inner if check hoga.


# ------------------------------------------------------------
# SYNTAX
# ------------------------------------------------------------

# if condition1:
#     if condition2:
#         statement
#     else:
#         statement
# else:
#     statement


# ============================================================
# EXAMPLE 1 - BASIC NESTED IF
# ============================================================

age = 20

if age >= 18:
    if age >= 21:
        print("You are 21 or above")
    else:
        print("You are an adult but below 21")
else:
    print("You are a minor")

# Output:
# You are an adult but below 21
# Reason: age 20 hai, outer condition True hai.
# Inner condition 20 >= 21 False hai, isliye inner else execute hua.


# ============================================================
# EXAMPLE 2 - BOTH CONDITIONS TRUE
# ============================================================

age = 25

if age >= 18:
    if age >= 21:
        print("You are an adult and 21 or above")
    else:
        print("You are an adult but below 21")
else:
    print("You are a minor")

# Output:
# You are an adult and 21 or above
# Reason: 25 >= 18 True aur 25 >= 21 bhi True hai.


# ============================================================
# EXAMPLE 3 - OUTER CONDITION FALSE
# ============================================================

age = 16

if age >= 18:
    if age >= 21:
        print("You are 21 or above")
    else:
        print("You are an adult but below 21")
else:
    print("You are a minor")

# Output:
# You are a minor
# Reason: outer condition 16 >= 18 False hai.
# Isliye inner if check hi nahi hoga.


# ============================================================
# EXAMPLE 4 - NESTED IF-ELSE
# ============================================================

number = 10

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is not positive")

# Output:
# Positive even number
# Reason: 10 positive hai aur 10 % 2 = 0, so number even hai.


# ============================================================
# EXAMPLE 5 - NEGATIVE NUMBER
# ============================================================

number = -7

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is not positive")

# Output:
# Number is not positive
# Reason: -7 > 0 False hai, isliye inner if execute nahi hua.


# ============================================================
# EXAMPLE 6 - PASS + HIGH SCORE
# ============================================================

marks = 85

if marks >= 40:
    if marks >= 80:
        print("Pass with excellent marks")
    else:
        print("Pass")
else:
    print("Fail")

# Output:
# Pass with excellent marks
# Reason: 85 >= 40 True, then 85 >= 80 bhi True.


# ============================================================
# EXAMPLE 7 - PASS BUT LOWER SCORE
# ============================================================

marks = 60

if marks >= 40:
    if marks >= 80:
        print("Excellent")
    else:
        print("Pass")
else:
    print("Fail")

# Output:
# Pass
# Reason: Student pass hai, but marks 80 se kam hain.


# ============================================================
# EXAMPLE 8 - FAIL
# ============================================================

marks = 30

if marks >= 40:
    if marks >= 80:
        print("Excellent")
    else:
        print("Pass")
else:
    print("Fail")

# Output:
# Fail
# Reason: 30 >= 40 False hai, so outer else execute hua.


# ============================================================
# EXAMPLE 9 - AGE + ID
# ============================================================

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Age not eligible")

# Output:
# Entry allowed
# Reason: Age eligible hai aur ID bhi available hai.


# ============================================================
# EXAMPLE 10 - AGE ELIGIBLE BUT NO ID
# ============================================================

age = 20
has_id = False

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Age not eligible")

# Output:
# ID required
# Reason: Age 18+ hai, lekin has_id False hai.


# ============================================================
# EXAMPLE 11 - LOGIN SYSTEM
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
# Reason: Username bhi correct hai aur password bhi correct hai.


# ============================================================
# EXAMPLE 12 - WRONG PASSWORD
# ============================================================

username = "admin"
password = "5678"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# Output:
# Wrong password
# Reason: Username correct hai, but password incorrect hai.


# ============================================================
# EXAMPLE 13 - WRONG USERNAME
# ============================================================

username = "student"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# Output:
# Wrong username
# Reason: Outer condition username == "admin" False hai.


# ============================================================
# EXAMPLE 14 - NESTED IF WITH STRING
# ============================================================

language = "Python"

if language == "Python":
    if len(language) > 5:
        print("Python has more than 5 characters")
    else:
        print("Python has 5 or fewer characters")
else:
    print("Different language")

# Output:
# Python has more than 5 characters
# Reason: Language Python hai aur len("Python") = 6.


# ============================================================
# EXAMPLE 15 - NUMBER RANGE
# ============================================================

number = 50

if number >= 1:
    if number <= 100:
        print("Number is between 1 and 100")
    else:
        print("Number is greater than 100")
else:
    print("Number is below 1")

# Output:
# Number is between 1 and 100
# Reason: 50 >= 1 True aur 50 <= 100 bhi True.


# ============================================================
# EXAMPLE 16 - EVEN + DIVISIBLE BY 5
# ============================================================

number = 20

if number % 2 == 0:
    if number % 5 == 0:
        print("Number is even and divisible by 5")
    else:
        print("Number is even but not divisible by 5")
else:
    print("Number is odd")

# Output:
# Number is even and divisible by 5
# Reason: 20 even hai aur 20 % 5 = 0.


# ============================================================
# EXAMPLE 17 - USER INPUT AGE
# ============================================================

age = int(input("Enter your age: "))

if age >= 18:
    if age >= 60:
        print("You are a senior citizen")
    else:
        print("You are an adult")
else:
    print("You are a minor")

# Example Input:
# 65
#
# Output:
# You are a senior citizen
#
# Reason: 65 >= 18 True, then 65 >= 60 bhi True.


# ============================================================
# EXAMPLE 18 - USER INPUT MARKS
# ============================================================

marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 75:
        print("Pass with good marks")
    else:
        print("Pass")
else:
    print("Fail")

# Example Input:
# 82
#
# Output:
# Pass with good marks
#
# Reason: Marks 40+ hain aur 75+ bhi hain.


# ============================================================
# EXAMPLE 19 - MARKS + ATTENDANCE
# ============================================================

marks = 70
attendance = 80

if marks >= 40:
    if attendance >= 75:
        print("Eligible for final exam")
    else:
        print("Attendance is low")
else:
    print("Marks are too low")

# Output:
# Eligible for final exam
# Reason: Marks 40+ aur attendance 75+ dono conditions True hain.


# ============================================================
# EXAMPLE 20 - SCHOLARSHIP CHECK
# ============================================================

marks = 90
income = 200000

if marks >= 80:
    if income <= 300000:
        print("Scholarship criteria satisfied")
    else:
        print("Income is too high")
else:
    print("Marks are too low")

# Output:
# Scholarship criteria satisfied
# Reason: Marks 90 >= 80 aur income 200000 <= 300000.


# ============================================================
# EXAMPLE 21 - NESTED IF WITH ELIF
# ============================================================

marks = 85

if marks >= 40:
    if marks >= 90:
        print("Grade A+")
    elif marks >= 80:
        print("Grade A")
    elif marks >= 70:
        print("Grade B")
    else:
        print("Grade C")
else:
    print("Fail")

# Output:
# Grade A
# Reason: Student pass hai.
# Inner conditions me 85 >= 90 False, 85 >= 80 True.


# ============================================================
# EXAMPLE 22 - THREE LEVEL NESTED IF
# ============================================================

age = 25
has_id = True
has_ticket = True

if age >= 18:
    if has_id:
        if has_ticket:
            print("Entry allowed")
        else:
            print("Ticket required")
    else:
        print("ID required")
else:
    print("Age not eligible")

# Output:
# Entry allowed
# Reason:
# 1. Age eligible hai.
# 2. ID available hai.
# 3. Ticket available hai.
# Teeno conditions satisfy hui.


# ============================================================
# EXAMPLE 23 - NESTED IF WITH INPUT
# ============================================================

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "python123":
        print("Welcome Admin")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")

# Example Input:
# admin
# python123
#
# Output:
# Welcome Admin
#
# Reason: Username aur password dono correct hain.


# ============================================================
# EXAMPLE 24 - INTERVIEW STYLE PROBLEM
# ============================================================

age = 22
marks = 75

if age >= 18:
    if marks >= 60:
        print("Eligible for interview")
    else:
        print("Marks requirement not satisfied")
else:
    print("Age requirement not satisfied")

# Output:
# Eligible for interview
# Reason: Age 18+ hai aur marks 60+ hain.


# ============================================================
# EXAMPLE 25 - MIXED NESTED IF
# ============================================================

number = 120

if number > 0:
    if number % 2 == 0:
        if number % 3 == 0:
            print("Positive, even and divisible by 3")
        else:
            print("Positive and even, but not divisible by 3")
    else:
        print("Positive and odd")
else:
    print("Number is zero or negative")

# Output:
# Positive, even and divisible by 3
# Reason:
# 120 positive hai.
# 120 even hai.
# 120 % 3 = 0 hai.
# Isliye final inner condition execute hui.


# ============================================================
# IMPORTANT DIFFERENCE
# ============================================================

# Normal IF:
#
# if condition:
#     statement
#
# Nested IF:
#
# if condition1:
#     if condition2:
#         statement
#
# Nested if ka matlab:
# "Agar pehli condition true hai, tab doosri condition check karo."


# ============================================================
# QUICK SUMMARY
# ============================================================

# Nested if = if ke andar if

# Flow:
#
# Outer if
#     ↓
# True?
#     ↓
# Inner if
#     ↓
# True / False
#     ↓
# Final output

# Important:
# Agar outer condition False hai,
# toh inner if execute nahi hota.


# ============================================================
# EXAM POINT
# ============================================================

# Question:
# What is nested if?
#
# Answer:
# A nested if statement is an if statement placed inside
# another if statement. It is used when one condition needs
# to be checked only after another condition is satisfied.


# ============================================================
# COMMON MISTAKE
# ============================================================

# WRONG:
#
# if age >= 18:
# if has_id:
#     print("Allowed")
#
# Python me indentation important hai.

# CORRECT:
#
# if age >= 18:
#     if has_id:
#         print("Allowed")


# ============================================================
# FINAL TAKEAWAY
# ============================================================

# if:
#       Ek condition check karta hai.
#
# if-else:
#       True / False ke according decision leta hai.
#
# if-elif-else:
#       Multiple conditions me se ek choose karta hai.
#
# nested if:
#       Ek condition ke andar doosri condition check karta hai.
#
# Example:
#
# if age >= 18:
#     if has_id:
#         print("Allowed")
#
# Pehle age check hogi.
# Agar age eligible hai tab ID check hogi.













'''NOTE:----    Yaad rakhne ka easiest way
                Nested if = “Pehle ye true ho,
                  tab uske andar ye check karo.”


Example:
if age >= 18:  # Step 1 
   if has_id:  # Step 2       
      print("Allowed")


Flow:

Age ≥ 18? → Yes → ID hai? → Yes → Allowed
Ab Topic 10: Mixed Problems mein in saare concepts ko combine karke proper coding questions karenge.


'''