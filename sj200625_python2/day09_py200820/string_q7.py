"""
7. Write a Python program to find the first appearance
of the substring 'not' and 'poor' from a given string,
if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string.

Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'

Expected Result : 'The lyrics is good!'
'The lyrics is poor!'

5 min

"""

"""
replace('not....poor', 'good')

find()
index()
"""
str1 = 'The lyrics is not that poor!'

start = str1.find('not')
print(f"start at {start}")

end = str1.find('poor')+len('poor')
print(f"end at {end}")

print(str1[start:end])
print(str1.replace(str1[start:end], 'good'))
print()


# youran
string = 'The lyrics are not that poor!'
a = string.find("not")
b = string.find("poor") + len('poor')
if string.find("not") != -1 and string.find("poor") != -1:
    result = string.replace(string[a:b], "good")
    print(result)
    print(string[a:b])
