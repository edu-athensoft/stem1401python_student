"""
demo of string
"""

list1 = [1,2,1,4,5,6]
a = list1.count(1)
print(a)


str1 = 'abcde'

# for c in str1:
#     print(c)

print(str1[0])

# q6
list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# a = sorted(list1)
a = sorted(list1, key=lambda x : x[1])

print(a)

# q10
str1 = "The quick brown fox jumps over the lazy dog"
n = 3

a = str1.split()
print(a, type(a))


