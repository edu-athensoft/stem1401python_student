"""
lambda function
filter()
"""

# 1, 2, 3, 4, 5, 6, ...
# pick out all the even numbers from a list
mylist = [1,2,3,4,5,6,7,8,9,10]
for i in mylist:
    if i%2 == 0:
        print(i)


mylist = [1,2,3,4,5,6,7,8,9,10]
new_list = []

result = filter(lambda x: x%2==0 , mylist)
print(result, type(result))

result = list(result)
print(result)


# exercise
# to pick up all the odd numbers from the list

# kevin
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: x%2 != 0, my_list)
result = list(result)
print(result, type(result))


print(list(filter(lambda x: x%2 == 0, my_list)))


# qijun
list1 = [1,2,3,4,5,6,7,8,9,10]
a = filter(lambda x: x%2 != 0, list1)
a= list(a)
print(a, type(a))
