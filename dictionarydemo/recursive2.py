patten="ABABACDE"

# first recursive
# char_count={}
# for char in patten:
#     if char in char_count:
#         print("first recursive",char)
#         break
#     else:
#         char_count[char]=1


# second recursive
rec_char=[]
char_count={}
for char in patten:
    if char in char_count:
        rec_char.append(char)
    else:
        char_count[char]=1
print(rec_char[1],"second recurcive")

#word count
# first recursive character
# second character
# #most recursive character



