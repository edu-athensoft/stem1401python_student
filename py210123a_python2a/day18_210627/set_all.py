"""
all()  built-in function
Return True if all elements of the set are true (or if the set is empty).
"""

# set all
# True == 1,  False = 0

my_set = {1,2,3}
result = all(my_set)
print(result)

my_set = {1,2,0}
result = all(my_set)
print(result)


my_set = {'a','b'}
result = all(my_set)
print(result)

my_set = {'a',''}
result = all(my_set)
print(result)

my_set = set()
result = all(my_set)
print(result)

#
print('========================')
my_list = [1, 2, 3, 4, 5]
print(all(my_list))

my_list = [1, 2, 3, 4, 0]
print(all(my_list))

my_list = [-1, -2, -3, -4, -5]
print(all(my_list))

my_list = [-1, -2, -3, -4, False]
print(all(my_list))

my_list = []
print(all(my_list))