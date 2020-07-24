"""
how many the number of 2 are there in the list1?

traversing
traversal

access : read and/or write
item/element:
"""

list1 = [2,3,4,5,6,3,2,1,3,5,6,7,5,3,5,5]

num = int(input("Enter a number: "))
count = 0

for i in list1:
    if i == num:
        count = count + 1
print("There are {} of {} in the list1".format(count, num))




"""
#
number_of_twos = 0
for i in list1:
    if i - 2 == 0:
        number_of_twos = number_of_twos + 1

print("There is {} twos.".format(number_of_twos))

#
two = 0
for i in list1:
    if i - 2 == 0:
        two = two + 1

print("n of two{}.".format(two))
"""

