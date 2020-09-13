"""
review
2-5 Data Types in Python
2-6 Python Type Conversion and Type Casting
"""

# numeric
num1 = 6        # integer
num2 = 9.18     # float
num3 = 0b110    # integer base 2 (binary number)

print("num1 is {}".format(num1))
print("num1 is {:b}".format(num1))  # binary

print("num3 is {}".format(num3))
print("num3 is {:}".format(num3))   # binary

"""
(10)    (2)
1        1
2       10
3       11
4      100
5      101
6      110  

9      1001 
10     1010
19
20
"""

# string
str1 = "Hello World"
str2 = "This is a book."
print("The datatype of {} is {}".format(str1, type(str1)))

# test datatype
# isinstance()
bool1 = isinstance(str1, str)
print("{} has the datatype of str? {}".format(str1, bool1))

bool2 = isinstance(str1, int)
print("{} has the datatype of int? {}".format(str1, bool2))


# if num1 is an integer, let us print 0 to num1
# else print num1

num1 = '9'
bool2 = isinstance(num1, int)
bool3 = isinstance(num1, float)
if bool2:
    print("str1 is an integer")
    a = 0
    while a < num1+1:
        print(a)
        a += 1
        # a = a + 1
else:
    print("str1:{} is not an integer".format(num1))

# validating or testing if an input is numeric

#
# a = 9
# if a >= 10:
#     pass
# else:
#     pass
#
# a = 0
# while a < 10:
#     print(a)
#     a += 1

