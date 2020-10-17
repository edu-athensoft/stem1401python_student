"""
Exception Handling
exception
error

Type 1. Syntax errors

Type 2. Logical errors (Exceptions)
Errors that occur at runtime (after passing the syntax test) are called exceptions or logical errors

Built-in exceptions
    TypeError
    ZeroDivisionError
    ValueError

User-defined exception
    PasswordTooShortError
    PasswordCaseError
    PasswordSymbolError

"""


# result = str(1) + 'abc'
# result = 1 + 'abc'
#
# if 1>5:
#     print("yes")
#
# while True:
#     print("a")
#   print("b")

a = 8
print("a=",a)
if a > 0:
    print("Negative")
else:
    print("Positive")

# print(b)
#
# if a < 3
#     pass


# result = 1 / 0


def foo(a):
    print(a+1)

foo('abc')





