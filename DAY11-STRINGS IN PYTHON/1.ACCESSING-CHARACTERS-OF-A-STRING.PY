# STRING CHARACTER:-

# CONSIDER A NAME "Hello" AND ACCESSING ITS CHARACTERS USING INDEXING:


Name = "Hello"
print(Name[0])  # Output: H (character at index 0)
print(Name[1])  # Output: e (character at index 1)
print(Name[2])  # Output: l (character at index 2)
print(Name[3])  # Output: l (character at index 3)
print(Name[4])  # Output: o (character at index 4)

'''NOTE: In Python, string indexing starts at 0, so the first character of a string is at index 0,
         the second character is at index 1, and so on. 
         You can also use negative indexing to access characters from the end of the string,
         where -1 refers to the last character, -2 refers to the second last character, and so on.'''



# ACCESSING CHARACTERS OF A STRING USING POSITIVE INDEXING:

Name = "Hello"
print(Name[0])  # Output: H (first character)
print(Name[1])  # Output: e (second character)
print(Name[2])  # Output: l (third character)
print(Name[3])  # Output: l (fourth character)
print(Name[4])  # Output: o (fifth character)

# print(Name[5])  # Output: IndexError: string index out of range (since the string has only 5 characters)


# ACCESSING CHARACTERS OF A STRING USING NEGATIVE INDEXING:

Name = "Hello"
print(Name[-1])  # Output: o (last character)
print(Name[-2])  # Output: l (second last character)
print(Name[-3])  # Output: l (third last character)
print(Name[-4])  # Output: e (fourth last character)
print(Name[-5])  # Output: H (fifth last character)

# print(Name[-6])  # Output: IndexError: string index out of range (since the string has only 5 characters)




'''Note: 
        1). 0 is the index of the first character in a string.
        2). -1 is the index of the last character in a string.
        3). You can use both positive and negative indexing to access characters in a string.
        4). If you try to access an index that is out of range, Python will raise an IndexError.
'''





