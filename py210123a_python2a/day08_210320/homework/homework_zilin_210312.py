"""
1. Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are the same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
hints:
creating at least 8 strings of item for a list
input a string from keyboard at one time

2. Write a Python function that takes two lists and returns True
 if they have at least one common member.
"""

# 1
stringlist = ['1221','2323','asdf','adda','asdfasdf','1111']

for string in stringlist:
    if len(string) >= 2 and string[0] == string[3]:
        print("string")


# 2
list1 = ['a','b','c']
list2 = ['a','2','3']

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            print("True")
            break
    if item1 == item2:
        break





