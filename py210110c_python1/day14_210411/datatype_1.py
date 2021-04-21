"""
datatype conversion

1. what is datatype conversion?
convert one datatype to another
str -> int,   str -> float
int -> float,
float->int,  float->str
int -> str

2. why do we need datatype conversion?


3. type of datatype conversion
3.1 implicit conversion  (automatically)
3.2 explicit conversion  (manually)

4. functions of datatype conversion
int()
float()
str()

5. data lost
float -> int

6. Things to remember
1) Type Conversion is the conversion of an object from one data type to another data type.
2) Implicit Type Conversion is automatically performed by the Python interpreter.
3) Python avoids the loss of data in Implicit Type Conversion.
4) Explicit Type Conversion is also called Type Casting,
the data types of objects are converted using predefined function by the user.
5) In Type Casting loss of data may occur as we enforce the object to specific data type.


"""

"""
a -> int
b -> float

step 1. get '+' operator
step 2. check operand and get two numbers (numeric values)
step 3. determine to do adding operation (arithmetic operation)
step 4. convert a from int to float  (int -> float)
step 5. float + float
step 6. return result (value)
"""

a = 10
b = 1.5
result = a + b    # implicit conversion
print('result = ',result, type(result))


#  TypeError: can only concatenate str (not "float") to str
# a = '10'
# b = 1.5
# result = a + b
# print('result = ',result, type(result))

# to resolve it we have two ways
# option 1. str -> float
a = '10'
b = 1.5
result = int(a) + b  # explicit conversion
# result = float(a) + b
print('result = ',result, type(result))

# option 2. float -> str
a = '10A'
b = 1.5
result = a + str(b)
print('result = ',result, type(result))


# example 1. str -> int
# int(string_value)
print("=== str -> int ===")
s1 = '100'
result = int(s1)
print(result, type(result))


# example 2. str -> float
# float(string_value)
print("=== str -> float ===")
s1 = '100.123'
result = float(s1)
print(result, type(result))


# example 3. str -> int/float
# anti-example
# print("=== str -> int/float anti-ex ===")
# s1 = '100.xyz'
# result = float(s1)
# print(result, type(result))
# ValueError: could not convert string to float: '100.xyz'


# example 4. int -> float
print("=== int -> float ===")
a1 = 200
result = float(a1)
print(result, type(result))


# example 5. int -> str
print("=== int -> str ===")
a1 = 200
result = 'abc'+str(a1)+'xyz'
print(result, type(result))


# example 6. float -> int  !!!!!!
# data lost!
print("=== float -> int ===")
f1 = 200.9
result = int(f1)
print(result, type(result))


# example 7. float -> str
print("=== float -> str ===")
f1 = 200.9
result = 'abc'+str(f1)+'xyz'
print(result, type(result))
