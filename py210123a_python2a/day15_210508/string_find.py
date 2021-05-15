"""
String
find() - returns the index of the 1st occurrence of the substring (if found).
       - return -1 if not found
v.s. index()

"""


str1 = "abc abc abd bcd bca"

# case 1. find()
pos = str1.find('abc')
print(pos)

pos = str1.find('bc')
print(pos)

pos = str1.find('xyz')
print(pos)

# case 2. find(substring, start)
pos2 = str1.find('abc', 3)
print(pos2)

# case 3. find(substring, start, end)
pos3 = str1.find('abc', 3, 6)
print(pos3)


# Homework
# Date: 2021-05-08
# question?
# how can I find the second substring?
# next substring
# Due date: by the end of next Fri.
print("======")
substring = 'abc'
pos = str1.find(substring)
print(pos, len(substring))

start = None
pos = str1.find(substring, start)
print(pos)


