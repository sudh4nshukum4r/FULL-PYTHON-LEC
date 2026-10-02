# Q1. Predict the output

text = "Python"
print(text.upper().lower())


# Q2. Predict the output

text = "  Python Programming  "
print(text.strip().upper())


# Q3. Predict the output

text = "python is powerful"
print(text.title().replace("Powerful", "Easy"))


# Q4. Predict the output

text = "banana"
print(text.count("a"))


# Q5. Predict the output

text = "Python123"
print(text.isalpha())
print(text.isalnum())


# Q6. Predict the output

text = "Python Programming"
print(text.find("gram"))
print(text.startswith("Py"))
print(text.endswith("ing"))


# Q7. Predict the output

text = "Python"
print(text[0].upper() + text[1:])


# Q8. Predict the output

text = "Python is easy"
words = text.split()
print("-".join(words))


# Q9. Find the mistake

text = "Python"
text[0] = "J"
print(text)


# Q10. Write a program

# Take a string from the user and:
# 1. Remove extra spaces
# 2. Convert it into lowercase
# 3. Count the number of 'a' characters
# 4. Check whether it starts with "python"