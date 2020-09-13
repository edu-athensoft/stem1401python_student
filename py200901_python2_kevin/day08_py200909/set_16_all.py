"""
built-in

all() - Return True if all elements of the set are true (or if the set is empty)

"""

# case 1. empty set
s1 = set()
print(all(s1))
print()

# case 2. normal set
s2 = {True, True}
print(all(s2))

s2 = {True, False}
print(all(s2))
print()

# case 3.
s2 = {1,1}
print(all(s2))

s2 = {1,2,-1}
print(all(s2))

s2 = {1,2,-1,0}
print(all(s2))

s2 = {'a','b'}
print(all(s2))

s2 = {'a','b',' '}
print(all(s2))

s2 = {'a','b',''}
print(all(s2))





