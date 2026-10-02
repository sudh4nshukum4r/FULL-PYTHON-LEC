# TYPE OF TYPECASTING
# 1. Implicit Typecasting
# 2. Explicit Typecasting




#----Implicit Typecasting----
# Implicit typecasting is automatically performed by Python when it converts a smaller data type to a larger data type.
a = 5  # integer
b = 2.0  # float
c = a + b  # Python automatically converts 'a' to a float before addition
print(c)  # Output: 7.0

# EXAMPLE OF EXPLICIT TYPECASTING
x = '10'  # String
y = int(x)  # Typecasting string to integer
print(y)  # Output: 10


#----Explicit Typecasting----
# Explicit typecasting is manually performed by the programmer when they want to convert a value from one data type to another.
x = '10'
y = int(x)  # Typecasting string to integer
print(y)  # Output: 10

# EXAMPLE OF IMPLICIT TYPECASTING
x = 5  # integer
y = 2.0  # float
z = x + y  # Python automatically converts 'x' to a float before addition
print(z)  # Output: 7.0



# NOTE: 1).Implicit typecasting is done automatically by Python, 
#          while explicit typecasting requires the programmer to specify the desired data type conversion.

# EXPLICIT=I CONVERTING ONE DATA TYPE TO ANOTHER DATA TYPE MANUALLY BY THE PROGRAMMER.
# IMPICIT=I CONVERTING ONE DATA TYPE TO ANOTHER DATA TYPE AUTOMATICALLY BY PYTHON.