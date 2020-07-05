"""
homework 2
"""
"""
q1. find the max from 3 numbers
"""

# simple but not flexible
def getmax(a,b,c):
    max = a
    if b>a:
        max = b
    if c>a:
        max = c
    return max

print("the max number is {}".format(getmax(30,6,200)))
# print("the max number is {}".format(getmax(30)))


# robust and flexible
def getmax2(numberlist):
    if len(numberlist) == 0:
        return "cannot get the max number"
    elif len(numberlist) == 1:
        return numberlist[0]
    else:
        max = numberlist[0]
        for i in numberlist:
            if i> max:
                max = i
        return max

print("the max number is {}".format(getmax2([30,600,20])))


# robust and flexible
def getmax3(*numbers):
    size = len(numbers)
    if size == 0:
        return "cannot get the max number"
    # elif size == 1:
    #     return numbers[0]
    else:
        max = numbers[0]
        for i in numbers:
            if i> max:
                max = i
        return max

print("the max number is {}".format(getmax3(3,6,20)))


# robust and flexible
# efficient, fast
def getmax4(*numbers):
    size = len(numbers)
    if size == 0:
        return "cannot get the max number"
    # elif size == 1:
    #     return numbers[0]
    else:
        return max(numbers)

print("the max number is {}".format(getmax4(2,30,400)))


# optimize
# concerns of performance
# concerns of complexity




"""
q3
"""
def multiply(x):
    product = 1
    for i in x:
        product *= i
    return product
list1 = [1, 2, 3, 4, 5]
# list1 = []
print(multiply(list1))


"""
q4
"""
def reverse(x):
    strlist = list(x)
    text = ""
    for i in strlist:
        text = i + text
    return text
str1 = "hello_hello"
str1 = "abc"
print(reverse(str1))