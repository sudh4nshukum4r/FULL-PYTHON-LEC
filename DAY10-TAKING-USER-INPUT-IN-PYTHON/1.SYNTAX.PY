# SYNTAX
# input(prompt)
# - prompt: A string to be displayed as a message to the user.
# - Returns the user's input as a string.

# VARIABLES = INPUT("MESSAGE")


# EXAMPLE OF USER INPUT
name = input("Enter your name: ")  # Taking user input for name
print("Hello, " + name + "!")  # Output: Hello, [name]!+



''' very important to note that the input() function always returns a string,
 so if you need a different data type, you must convert it using typecasting functions 
like int(), float(), etc.'''


# exmaple of taking user input for age and converting it to an integer
age = int(input("Enter your age: "))  # Taking user input for age and converting it to an integer
print("You are " + str(age) + " years old.")  # Output: You are [age] years old.
print(type(age))  # Output: <class 'int'> 
                 #because we have converted the input to an integer using int() function,
                #the type of age variable is now in

# Taking float input:

price = float(input("Enter the price: "))  # Taking user input for price and converting it to a float
print("The price is $" + str(price))  # Output: The price is $[price]
                
