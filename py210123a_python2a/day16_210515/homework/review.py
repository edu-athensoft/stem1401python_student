"""
Problem: find the second substring
problem-solving

string.find(substring)
string.find(substring, start)
string.find(substring, start, end)


idea

"""

str1 = "abc abc abb bcd"

# target: 'abc'
# goal: to find the position of the second substring
# tool, technique:   find the first one

# find, index
# find() - searching from beginning at the most left position
# rfind()

# logical thinking
# basic idea

substring = 'abc'
pos = str1.find(substring)
print(pos)

start = pos + len(substring)
pos = str1.find(substring, start)
print(pos)

# termination condition















