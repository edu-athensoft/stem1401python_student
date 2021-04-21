"""
built-in errors
"""

"""
AssertionError      Raised when an assert statement fails
AttributeError      Raised when attribute assignment or reference fails.
EOFError            Raised when the input() function hits end-of-file condition
FloatingPointError  Raised when a floating point operation fails
GeneratorExit       Raise when a generator's close() method is called
ImportError		    Raised when the imported module is not found
ModuleNotFoundError 
IndexError          Raised when the index of a sequence is out of range
KeyError		    Raised when a key is not found in a dictionary
KeyboardInterrupt	Raised when the user hits the interrupt key (Ctrl+C or Delete)
MemoryError		    Raised when an operation runs out of memory
NameError		    Raised when a variable is not found in local or global scope
NotImplementedError	Raised by abstract methods
OSError		        Raised when system operation causes system related error
OverflowError		Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError	    Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError		Raised when an error does not fall under any other category.
StopIteration		Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError		    Raised by parser when syntax error is encountered.
IndentationError	Raised when there is incorrect indentation.
TabError		    Raised when indentation consists of inconsistent tabs and spaces.
SystemError		    Raised when interpreter detects internal error.
SystemExit		    Raised by sys.exit() function
TypeError		    Raised when a function or operation is applied to an object of incorrect type.
ValueError		    Raised when a function gets an argument of correct type but improper value.
"""


"""
Assert  verb.  predict

Grammar v.s Syntax
"""
# from math import sins
# from maths import sin
# import math
# import maths

def foo(num):
    print(num+1)

foo("abc")
foo(-1)


# de foo():
#  pass

import sys

result = 1 + "abc"



if True:
 print("indentation 1")
 print("indentation 1")
 print("indentation 1")
 print("indentation 1")


if True:
    print("indentation 1")
    print("indentation 1")
    print("indentation 1")
    print("indentation 1")

# sys.exit()

name = 'Peter'
print(name)

del name
# print(name)

print()



mydict = {1:'111',2:'222'}
print(mydict)
print(list(mydict.keys()))

# mydict['key1']


print()
mylist = [22,33,444,555,666]
first_item = mylist[0]
last_item = mylist[4]
print(first_item, last_item)

# first_item = mylist[5]
# first_item = mylist[-6]


# a = int(input("Enter a number: "))
# assert a > 3







