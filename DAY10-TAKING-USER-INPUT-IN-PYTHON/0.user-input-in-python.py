# what is user input in python
# 1). User input in python refers to the ability to accept data from the user during the execution of a program.
# 2). This is typically done using the `input()` function, which allows the program to pause and wait for the user to enter some data. 
# 3). The `input()` function returns a string, so if you need a different data type, you must convert it using typecasting functions like `int()`, `float()`, etc.





# 1). python program to demonstrate user input
# taking user input for name
name = input("Enter your name: ")
print("Hello, " + name + "!")



# 2). taking user input for age and converting it to an integer
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")



# 3). taking user input for price and converting it to a float
price = float(input("Enter the price: "))
print("The price is $" + str(price))





# 4). taking user input for a number and converting it to an integer
number = int(input("Enter a number: "))
print("The number you entered is: " + str(number))





# 5). taking user input for a decimal number and converting it to a float
decimal_number = float(input("Enter a decimal number: "))
print("The decimal number you entered is: " + str(decimal_number))





# note: 1).The `input()` function always returns a string, so if you need a different data type,
#           you must convert it using typecasting functions like `int()`, `float()`, etc.



