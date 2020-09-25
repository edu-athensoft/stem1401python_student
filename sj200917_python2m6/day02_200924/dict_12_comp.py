"""
Python Dictionary Comprehension

Dictionary comprehension is an elegant and concise
way to create a new dictionary from an iterable in Python.

how to create a dictionary?
1. directly define with literal
2. directly define with dict()
3. copy()
4. {for}
5. fromkeys() and other methods (functions)
"""

# 1
mydict = {1:'a',2:'b'}

# 2
mydict = dict({3:'c'})
mydict = dict([[11,'a'],[22,'b']])
print(mydict)

# 3
mydict1 = mydict.copy()

# 4 for
mydict2 = {x: 2*x for x in range(15)}
print(mydict2)

mydict2 = {2*x: 4*x for x in range(3)}
print(mydict2)

# 5. method
# fromkeys(seq)


mydict1 = {1:1, 2:2, 3:3, 4:4}
# {1:1, 2:2, ....  n-1:n-1,  n:n}

# key = value
# key from 1..n
# value from 1..n
# n = 10
for key in range(1,11):
    value = key
    print(key, value)

mydict4 = {key: key for key in range(1,11)}
print(mydict4)

mydict4 = {key: 2*key for key in range(1,11)}
print(mydict4)

mydict4 = {i+1: 2*i for i in range(1,11)}
print(mydict4)

#
mydict5 = {key: key for key in range(1,11) if key % 2 == 1}
print(mydict5)
