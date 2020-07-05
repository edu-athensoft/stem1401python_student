"""
list comprehension

List comprehension is an elegant and concise way to create a new list from an existing list in Python.

v.s.

lambda expression/function
filter()
map()
"""

mylist = [1,2,3,4,5,6,7,8,9,10]

# map()
a = [2 * x for x in mylist]
print(a)


# filter()
# odd number
b = [2 * x for x in mylist if x%2 == 1]
print(b)
