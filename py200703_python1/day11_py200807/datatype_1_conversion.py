"""
Type Conversion

The process of converting the value of one data type (integer, string, float, etc.)
to another data type is called type conversion.

Python has two types of type conversion.
Implicit Type Conversion
Explicit Type Conversion

Key Points to Remember
Type Conversion is the conversion of object from one data type to another data type.

Implicit Type Conversion is automatically performed by the Python interpreter.

Python avoids the loss of data in Implicit Type Conversion.

Explicit Type Conversion is also called Type Casting, the data types of object
are converted using predefined function by user.

In Type Casting loss of data may occur as we enforce the object to specific data type.


"""


# Converting integer to float
i1 = 123
f1 = float(i1)
print(f1)

# implicit type conversion
res = i1 + f1
print(res, type(res))


# explicit type conversion
res = i1 + int(f1)
print(res, type(res))

