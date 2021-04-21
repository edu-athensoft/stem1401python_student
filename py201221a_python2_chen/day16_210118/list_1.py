"""
Write a Python program to sum all the items in a list.

[Homework] 2021-01-18
Write a Python program to multiply all the items in a list.
"""


# step 1. to create a list
list1 = [1,2,3,4,5,6]

# step 2. to sum all the items
a = [1, 2, 3, 4, 5]
b = sum(a)
print(b)

# step 2. to sum all the items using for loop
# how to print out each item by using for loop
a = [4,7,3,2,5,9]

# for i in a:

sum = 0

list1 = [4,7,3,2,5,9]
for i in list1:
    # print(list1)
    print(i)
    sum = sum + i

# step 3.
print("The sum of the list items is {}".format(sum))

"""
1ST     4       SUM=(SUM)+4=4
2ND     7       SUM=(SUM)+7=11
3RD     3       SUM=(SUM)+3=14
4TH     2       SUM=(SUM)+2=16
5TH     5       SUM=(SUM)+5=21
6TH     9       SUM=(SUM)+9=30


"""





"""
4
7
3
2
5
9
"""

# how to write the print statement
# print('hello  goodbye  hello')
# print(1)
# print(a)
"""
mylist = ['10', '12', '14']
for elem in mylist:
    print elem

10
12
14
"""