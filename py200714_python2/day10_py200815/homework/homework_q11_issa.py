"""
11. Write a Python program to remove the characters which have odd index values of a given string.
"""
# final_string = ""
# user_string = input("Input your string: ")
# for x in range(len(user_string)):
#     if x % 2 == 0:
#         # final_string = final_string + user_string[x + 1]
#         final_string = final_string + user_string[x]
# print(final_string)



# solution 2
str1 = "01234567"
print(str1[::2])


# solution 3
# iteration, index()
str1 = "01234567"
for char in str1:
    if str1.index(char) %2 == 1:
        str1 = str1.replace(str1[str1.index(char)],"_")
print(str1.replace('_',''))




