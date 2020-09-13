"""
lambda function

iterable:
my_list1 = [1,2,3,4,5,6,7,8,9,10]

result = [1,4,9,16,25,36, 49,64, 81,100]

function:
lambda x : x**2
lambda x : x * x

map(function, iterable)
"""

my_list1 = [1,2,3,4,5,6,7,8,9,10]
print("original list is",my_list1)

a = map(lambda x : x**2, my_list1)
# print(a, type(a))

b = list(a)
print("result list is ",b)
