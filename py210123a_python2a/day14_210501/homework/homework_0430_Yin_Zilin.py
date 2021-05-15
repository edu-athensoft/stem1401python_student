"""
1. Write a Python program to get a string made of the first 2
 and the last 2 chars from a given a string.
  If the string length is less than 2, return instead of the empty string.
Sample String : 'w3abcdce'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String

2. rewrite number 4 of last week's homework
4. Write a Python program to convert a tuple to a string.
"""

# 1
string1 = ("aasdfasdf")
string1 = ("12345678")
string1 = ("12")
string1 = ("123")
# string1 = ("1")


for i in string1:
    if len(string1) > 1:
        string2 = string1[0:2] + string1[-2:]
    else:
        string2=''

print(string2)
print("===============")


#2 convert a tuple to a string
tuple1 = (1,2,3,4)
print(str(tuple1))

tuple2 = ('a','b','c','d')
result = ''.join(tuple2)
print(result)




