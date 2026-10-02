# STRING ERROR:-

# In Python, when you try to access a character in a string using an index that is out of range, it raises an IndexError.

# For example, if you have a string "Hello" and you try to access the character at index 5 (which does not exist), it will raise an IndexError.

# Example of IndexError:

# Name = "Hello"
# print(Name[5])  # Trying to access the character at index 5 (which does not exist)
                #Output: IndexError: string index out of range
                #Because the string "Hello" has only 5 characters, the valid indices are 0 to 4.

'''NOTE:- STRING ARE IMMUTABLE IN PYTHON,
          WHICH MEANS THAT ONCE A STRING IS CREATED, 
          IT CANNOT BE CHANGED. 
          IF YOU TRY TO CHANGE A CHARACTER IN A STRING USING INDEXING, 
          IT WILL RAISE A TYPEERROR.'''

# Example of TypeError:
# Name = "Hello"
# Name[0] = "h"  # Trying to change the first character (which is not allowed)
#                # Output: TypeError: 'str' object does not support item assignment

