"""
Special operators
1. identity operator
is ,  is not

2. membership operator
in, not in

"""

# 1. identity oper
# A is B

# case 1. integer
x1 = 5
y1 = 5

result = x1 is y1
print ('x1 is y1? {}'.format(result))

result2 = x1 == y1
print ('x1 == y1? {}'.format(result))

print("=========================")

# case 2. float
# x2 = 0.3
# y2 = 1 - 0.7

x2 = 0.3
y2 = 0.3

result = x2 is y2
print ('x2 is y2? {}'.format(result))

result2 = x2 == y2
print ('x2 == y2? {}'.format(result2))


print("=========================")

s1 = 'abc'
s2 = 'abc'
result = s1 is s2
print ('s1 is s2? {}'.format(result))

result2 = s1 == s2
print ('s1 == s2? {}'.format(result2))

result = s1 is not s2
print ('s1 is not s2? {}'.format(result))


print("=========================")

# list is mutable
# the 'is' operator is used to check if the two names stand for the identical object.
# twins

list1 = [1,2,3]
list2 = [1,2,3]

result = list1 is list2
print ('list1 is list2? {}'.format(result))

result2 = list1 == list2
print ('list1 == list2? {}'.format(result2))


print("=========================")

# tuple (read-only list)

# tuple is immutable
# not twins but the identical object

t1 = (1,2,3)
t2 = (1,2,3)

result = t1 is t2
print ('t1 is t2? {}'.format(result))

result2 = t1 == t2
print ('t1 == t2? {}'.format(result2))
print("=========================")

# membership operator
# case 1.
a = 10
list1 = [12,14,16,10,18]
result = a in list1
print(result)

result2 = a not in list1
print(result2)
print("========")

# case 2
a = 15
list1 = [12,14,16,10,18]
result = a in list1
print(result)

result2 = a not in list1
print(result2)


# membership with tuple
b = 4
t3 = (1,2,3)
print(b in t3)

b = int(input("enter an integer:"))
print(b in t3)

