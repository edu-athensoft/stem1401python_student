"""
list and lambda
"""


mylist = [1,2,3,4,5]

def f(n):
    return lambda list1 : list1[n] * 2

result = f(1)
print(result(mylist))
