"""
original_list [1,2,3,4,5,6,7,8,9,10]
expect_list [1,9,25,49,81]
"""

"""
original list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
expected list = [1, 9, 25, 49, 81]
"""

# default_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = filter(lambda x: x%2 != 0, default_list)
# y = map(lambda x: x**2, x)
# y = list(y)
# print(y)

# default_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = filter(lambda x: x % 2 != 0, default_list)
# y = list(map(lambda x: x ** 2, x))
# print(y)

#
# original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = filter(lambda x: a % 2 == 1, original_list)
# expected_list = list[map(lambda x: a*a, a)]
# print(expected_list)

def foo(x):
    # print(2*a)
    return 2*x

default_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = filter(lambda x: x % 2 != 0, default_list)
y = list(map(lambda x: x**2, a))
print(y)
