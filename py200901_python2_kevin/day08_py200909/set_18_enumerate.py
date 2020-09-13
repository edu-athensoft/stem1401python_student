"""
built in

enumerate()	Return an enumerate object.
It contains the index and value of all the items of set as a pair.

"""

s1 = {'a','b','c'}
result = enumerate(s1)

# result = set(result)
result = list(result)
print(result)

# {(2, 'a'), (0, 'c'), (1, 'b')}
# {(1, 'a'), (2, 'b'), (0, 'c')}
# {(2, 'b'), (0, 'c'), (1, 'a')}



list1 = ['a','b','c']
result = enumerate(list1)
result = list(result)
print(result)



