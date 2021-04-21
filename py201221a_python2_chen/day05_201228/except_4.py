"""
built-in exceptions
Illegal operations can raise exceptions.

"""


# dir()

builtin_errors = dir(locals()['__builtins__'])

# for item in builtin_errors:
#     print(item)

"""
AssertionError      raised when an assert statement fails
AttributeError      
EOFError            raised when input() hits end-of-file condition
FloatingPointError  raised floating point operation fails
GeneratorExit
ImportError         raised when the imported module is not found
ModuleNotFoundError raised when the module is not found
IndexError          raised when the index of a sequence is out of range
KeyError            raised when a key is not found in a dictionary
KeyboardInterrupt   raised when the user hits the interrupt key (Ctrl+C, Delete)
MemoryError         raised when an operation runs out of memory
NameError           raised when a variable name is not found in local or global scope
OSError             raised when system operation causes system related errors
OverflowError       raised when the result of an arithmetic operation is too large to be
ReferenceError      raised when a weak reference proxy is used to access a garbage
RuntimeError        raised when an error does not fall under any other category
SyntaxError         raised by parser when syntax error is encounted
IndentationError       
SystemError         Raised when interpreter detects internal error.
SystemExit          Raised by sys.exit() function
TypeError           Raised when a function or operation is applied to an object of incorrect
ValueError          Raised when a function gets an argument of correct type but improper value
ZeroDivisionError   
UnicodeError
UnicodeEncodeError
UnicodeDecodeError
UnicodeTranslateError

"""


"""
mylist = [1,2,3,4]
# print(mylist[-7])
print(mylist[6])

# print(mylist[-2])
"""

"""
# to produce a KeyError
mydict = {"abc":1, "ddd":2}
mydict['ccc']
"""

"""
# to generate or reproduce a NameError
NameError: name 'a' is not defined
"""
# print(a)


"""
# to generate a TypeError
TypeError: unsupported operand type(s) for -: 'str' and 'int'
"""

# a = 'abc'
# b = 1
# result = a - b


"""
ValueError
"""
# import math
# res = math.sqrt(-16)
# print(res)


