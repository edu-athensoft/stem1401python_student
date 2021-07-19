"""
any()
Return True if any element of the set is true. If the set is empty, return False.
"""

my_set = {1,2,3}
result = any(my_set)
print(result)

my_set = {1,2,0}
result = any(my_set)
print(result)

my_set = {False, 0}
result = any(my_set)
print(result)

my_set = set()
result = any(my_set)
print(result)


# application
# fire-alarm and monitor


