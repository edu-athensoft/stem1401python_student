"""
String
join()
"""


tuple1 = ('a','b','c')

result = str(tuple1)
print(result)

# join()
# return a combined string
result = ''.join(tuple1)
print(result, type(result))

#
tuple2 = ('a','b', 3)
# TypeError: sequence item 2: expected str instance, int found
# result = ''.join(tuple2)
# print(result, type(result))

# the separator is not empty
result = ' '.join(tuple1)
print(result, type(result))

result = ','.join(tuple1)
print(result, type(result))

# List
data1 = ['a','b','c']
result = ''.join(data1)
print(result, type(result))

# Tuple

# string
data3 = 'wxyz'
result = ','.join(data3)
print(result, type(result))

# set
data4 = {'a','b','c'}
result = ','.join(data4)
print(result, type(result))
# c,b,a
# a,c,b
# b,c,a


# dictionary
# TypeError: sequence item 0: expected str instance, int found
# join keys only
data5 = {'1':'a','2':'b','3':'c'}
result = ','.join(data5)
print(result, type(result))
