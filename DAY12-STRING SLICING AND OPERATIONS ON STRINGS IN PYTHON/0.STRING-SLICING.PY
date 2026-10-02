# STRING SLICING AND OPERATIONS ON STRINGS IN PYTHON.


#1). WHAT IS STRING SLICING ?

'''STRING SLICING IS A METHOD TO EXTRACT A SUBSTRING FROM A STRING USING INDEXES.
IN PYTHON, STRINGS ARE SEQUENCES OF CHARACTERS, AND YOU CAN ACCESS INDIVIDUAL CHARACTERS OR SUBSTRINGS USING SLICING SYNTAX.
'''

# 2). SYNTAX OF STRING SLICING:

'''string[start:end:step]'''

# END INDEX INCLUDE NHI HOTA HAI, START INDEX INCLUDE HOTA HAI. STEP OPTIONAL HAI, DEFAULT VALUE 1 HAI.


# 1). EXAMPLES:-

NAME = "PYTHON"
print(NAME[0:2])  # OUTPUT: PY
print(NAME[2:4])  # OUTPUT: TH
print(NAME[4:6])  # OUTPUT: ON

# because end index is not included, so it will print characters from index 0 to 1, 2 to 3, and 4 to 5 respectively.

'''Note:-
          index 3 exclude hoga, index 5 exclude hoga, index 1 include hoga, index 4 include hoga.

'''



