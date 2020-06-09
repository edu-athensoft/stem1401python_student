"""
string - accessing element (char)
"""

str1 = "athensoft inc."
print('str = ', str1)

# accessing by index
# 1st char
print("first char is: ",str1[0])
# last char
print("first char is: ",str1[-1])


# slicing
# print("index of space is ",str1.index(' '))
stop_pos = str1.index(' ')
print("company name: ",str1[:stop_pos])