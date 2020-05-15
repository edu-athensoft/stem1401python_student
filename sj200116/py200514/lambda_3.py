"""
my_list1 = [1,2,3,4,5,6,7,8,9,10]
result = [2,4,6,8,10]

filter()
"""
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list1)

a = filter(lambda x: x%2==0, my_list1)
# print(a, type(a))

b = list(a)
print(b)
print()

#
print(list(filter(lambda x: x%2==0, my_list1)))
print()

# import sys
# # print(sys.path)
# for path in sys.path:
#     print(path)



