"""
lambda function

syntax

lambda arg1,[arg2,arg3,...] : expr

arg = argument
0 or has/have, optional

high-order function

x % 2 == 0

"""

list1 = [1, 2, 3, 4, 5, 6]
a = filter(lambda x: x % 2 == 0, list1)
print(a, type(a))

b = list(a)
print(b, type(b))
