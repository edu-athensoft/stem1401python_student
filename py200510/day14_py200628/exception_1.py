"""
Exception Handling

1. what is an exception?
error

at runtime
at compile time
validate or syntax checking

python
detect, catch, handle possible exceptions

types of exception:
a. built-in exception
b. user-defined exception

2. why?
to avoid to crash frequently
to improve the tolerance ability of your programs, robust

3. how to use?

"""


"""
Logical Errors Example/Case
"""

# case 1.  Syntax Errors
a = 6
# if a>3
# SyntaxError: invalid syntaxs

if a > 3:
    pass


# case 2. Logical Errors
# when your program is going to read a file, open the file first, there is no such file.
# FileNotFoundError

a = 1
b = 1
# ....
result = a/b
# ZeroDivisionError

# import a not existing module
# ImportError


# list all the built-in exceptions
# print(dir(locals()['__builtins__']))

"""
locals()['__builtins__']
functions
attributes
exceptions

dir() - list them out
"""

for entry in dir(locals()['__builtins__']):
    print(entry)

