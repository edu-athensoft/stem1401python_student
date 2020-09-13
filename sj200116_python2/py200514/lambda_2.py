"""

"""

mylist1 = [1,2,3,4,5,6,7,8,9,10]

# double each item of the list
# print out [2,4,6,8,...,20]

my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(my_list1*2)

# solution 1
result = []
for item in my_list1:
    result.append(2 * item)

print("The result is {}".format(result))

print()

# solution 2
for index in range(len(my_list1)):
    my_list1[index] = my_list1[index] * 2

print(my_list1)
print()

# solution 3
# lambda x: 2 * x
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [2*x for x in my_list1]
print(result)
