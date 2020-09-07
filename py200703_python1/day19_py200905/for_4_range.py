"""
range() - to generate a number sequence

range(n) - from 0 to n-1, n numbers
range(start, stop)
range(start, stop, step)

"""

result = range(10)
print(result, type(result))

mylist = list(result)
print(mylist, type(mylist))


#
result = range(100)
mylist = list(result)
print(mylist, type(mylist))

result = range(101)
mylist = list(result)
print(mylist, type(mylist))


#
result = list(range(1,101))
print(result)


#
result = list(range(1, 20, 2))
print(result)