"""
stem1402_python_homework_2_steven
"""


# 1. Write a Python function to find the Max of three numbers.
def maximum(x, y, z):
    list1 = [x, y, z]
    return max(list1)


x = 21
y = 346
z = 345
print("The maximum number of {}, {} and {}, is {}".format(x, y, z, maximum(x,y,z)))

print("-------------------------------------------------------------------------")
print()


# 2. Write a Python function to sum all the numbers in a list.


list1 = [1,3,4,23,5,463,45,36,1]


def adding(list):
    sum = 0
    for num in list1:
        sum += num
    return sum

print("The sum of the numbers in {} is {}.".format(list1, adding(list1)))

print("-------------------------------------------------------------------------")
print()


# 3. Write a Python function to multiply all the numbers in a list.


list1 = [1,3,4,23,5,463,45,36,1]


def multiplying(list):
    product = 1
    for num in list1:
        product *= num
    return product

print("The product of the numbers in {} is {}.".format(list1, multiplying(list1)))

print("-------------------------------------------------------------------------")
print()


# 4. Write a Python program to reverse a string.


a = [1,32,354,36,3]


def reverse(list):
    n = len(a) - 1
    while n >= 0:
        print(a[n], end=" ")
        n -= 1


print("When you reverse", a, "you get", end=" "), reverse(list)
print()
print("-------------------------------------------------------------------------")




