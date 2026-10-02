# loop Through A String:-
# string are arrays and array are iterable. Thus we can loop through strings.

# 1. EXAMPLE
a = "abcde"
for i in a:
    print(i)



# METHOD 1:-  Direct for loop

word = "CODE"

for char in word:
    print(char)




# 1. FOR LOOP SE STRING KE CHARACTERS NIKALA JATA HAI.
# 2. CHAR Means CHARACTERS.
# 3. for char in word:    MEANING:-  "WORD KE ANDAR JO CHARACTERS HAIN, UNKO EK-EK KAEKE CHAR VARIABLE MEIN DAALO."


'''NOTE:-
          1) YAHAN char KOI SPECIAL PYTHON KEYWORD NAHI HAI.
          2) TUM ISKA NAAM KUCH BHI RAKH SAKTE HO.
'''



# METHOD 2:- USING INDEX

word = "KRITIKA"

for i in range(len(word)):
    # print(word)
    print(word[i])




for i in range(len(word)):
    print(word)
    print(word[i])





'''NOTE:-
         1) CHARACTER chahiye:-- for char in word
         -- yahan dirctly character milta hai.
         
         2)INDEX  chahiye:-- for char in range(len(word))
         -- yahan pehle index milta hai.

'''