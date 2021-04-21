"""
datatype
# A variable or a constant has a data type.
# A literal has a data type

type() -  return what type it is
isinstance()  return if A is one instance of B or if A is of B type

class,  instance
A is an instance of B => A is one instance of B.





variable or literal has a value
Every value has a data type
1. space allocated for the value
2. available operations

statement, assignment statement
variables and constants which store data
literals (raw data)
1. numeric literal
2. boolean literal
3. string literal
4. collection literal

"""

# sample code
a = 1
a2 = 1.5
b = 'abc'
c = True
c2 = False
list1 = [1,2,3]
tuple1 = (1,2,3)
set1 = {1,2,3}
dict1 = {1:'a', 2:'b', 3:'c'}


#
a = 1
b = a   # where a is NOT a literal


# A variable or a constant has a data type.
# A literal has a data type

# how to check the data type of a value (incl. var and const)
# 1. type(data or name) returns the data type of that data
result = type(10)
print("The data type of 10 is",result)

result = type(list1)
print("The data type of list1 is",result)


# ex.1
# 1. create a set, tuple, dict
# 2. test data type of each data

# ex.1 Andy
print("Andy")
tuple1 = (1, 2, 3)
set1 = {1, 2, 3}
dict1 = {1: 'a', 2: 'b', 3: 'c'}

result = type(tuple1)
print("The data type of 10 is", result)

result = type(set1)
print("The data type of 10 is", result)

result = type(dict1)
print("The data type of 10 is", result)


# ex.1 Leon
set1 = {1,2,3,4,5,6}
result = type(set1)
print("The data type of set1 is",result)

tuple1 = (4,6,8,10,12,14)
result = type(tuple1)
print("The data type of tuple1 is",result)

animals = {1:'mouse',2:'horse',3:'dog'}
# dict1 = type(dict1)
result = type(animals)
print("the data type of animals is",result)


# ex.1 Yiding
set1 = {1, 2, 3, 4, 5, 6}
result = type(set1)
print("The data type of set1 is", result)

tuple1 = (7, 8, 9, 10, 11, 12)
result = type(tuple1)
print("The data type of tuple1 is", result)

instrument_dict = {1: 'trumpet', 2: 'guitar', 3: 'piano'}
# dict1= type(dict1)
result= type(dict1)
print("the data type of instrument_dict is", result)

set1 = {1, 2, 3, 4, 5, 6}
result = type(set1)
print("The data type of set1 is", result)
tuple1 = (7, 8, 9, 10, 11, 12)
result = type(tuple1)
print("The data type of tuple1 is", result)
instrument_dict = {1: 'trumpet', 2: 'guitar', 3: 'piano'}
result = type(instrument_dict)
print("the data type of list is", result)

# ex.1 Kevin
tuple4 = (a, b, c)
set2 = {1, 2, 3}
dict3 = {1:'d', 2:'e', 3:'f'}

result = type(tuple4)
print('The data type of tuple4 is', result)

result = type(set2)
print('The data type of set2 is', result)

result = type(dict3)
print('The data type of dict3 is', result)


# isinstance(data_or_value,  expected_data_type)
a = 10
result = isinstance(a, int)
print(a, 'is instance of int?', result)

a = 10.0
result = isinstance(a, int)
print(a, 'is instance of int?', result)
print('The type of a is',type(a))










