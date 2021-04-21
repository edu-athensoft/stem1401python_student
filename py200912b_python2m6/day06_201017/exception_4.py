"""
pre-defined errors in Python

"""

"""
MemoryError         Raised when an operation runs out of memory.
NameError		    Raised when an entity is not found in local or global scope.
NotImplementedError Raised by abstract methods
OSError             Raised when system operation causes system related error.
OverflowError		Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError	    Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError		Raised when an error does not fall under any other category.
StopIteration		Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError		    Raised by parser when syntax error is encountered.
IndentationError	Raised when there is incorrect indentation.
TabError		    Raised when indentation consists of inconsistent tabs and spaces.
SystemError		    Raised when interpreter detects internal error.
SystemExit		    Raised by sys.exit() function.
TypeError		    Raised when a function or operation is applied to an object of incorrect type.
UnboundLocalError	Raised when a reference is made to a local variable in a function or 
                    method, but no value has been bound to that variable.
UnicodeError		Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError	Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError	Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError Raised when a Unicode-related error occurs during translating.

ValueError		    Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError	Raised when the second operand of division or modulo operation is zero.
"""

"""
Primary Errors you should know and use

AttributeError
ImportError
ModuleNotFoundError
IndexError
KeyError
NameError
SyntaxError
RuntimeError
TypeError
ValueError
ZeroDivisionError
"""

# NameError
mydict = {1:'a'}

del mydict

print(mydict)
mydict[1]


# ZeroDivisionError
# ZeroDivisionError: division by zero
a = 1
b = 2

# ....
b = 0
# ....

result = a / b

print(result)


# SystemExit
import sys
print("1123")
print("1123")
print("1123")
sys.exit()
print("aaaa")
print("bbbb")
print("ccccc")




# make a name error
# foo()
# print(ab)

# syntax error
# if True
#     pass

# if True:
#     print("")
#     print("")
#     print("")
#     print("")


# for i in range(10):
# print("")
#
# print("")
#     print("")
#     print("")


#
# if () {
#
# }


# javascript
# function foo(){
#     print("");
# print("");
#  print("");
#    print("");
# }


