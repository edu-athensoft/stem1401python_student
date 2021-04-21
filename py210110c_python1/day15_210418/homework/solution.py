"""
Quiz 5

question 7

data type conversion
From data type to another data type

"""

f1 = 1.5

# explicit conversion
# float -> str
# str()
result = str(f1)


# a = '10.1'
# b = 'abc'
# result = a + str(b)

a = 10.1
print(type(a))
# result = a+ str(a)
result = str(a)
print(type(result))
print(result)


# part 2.
# result: string  -> int
# 'abc' -> int  # invalid
result2 = int(float(result))
# ValueError: invalid literal for int() with base 10: '10.1'
print(result2, type(result2))
