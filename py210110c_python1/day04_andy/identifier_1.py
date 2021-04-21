"""
An identifier is a name given to
entities like class, functions, variables, etc.


# rules of identifier
"""


# concrete names
mycar = 'BMW'

mybook = 'Frech Bascis'

counter = 0



# abstract names
a = 100
i = 0


# rule 1
# valid characters = 0-9a-zA-Z_  (- is not included.)
# digits, alphabet, underscore
mylist = [1,2,3]
MyList = [1,2,3]

counter1 = 0
counter2 = -1
counter3 = 100

obj_001 = 245
obj_002 = 234

_ab = 999
_ab_ = 111
__abc__ = 222

_01 = 34
_01_ = 23


# rule 2
# starts with a-zA-Z or/and _
# cannot start with digit
# 0a = 1  # error
# 99_abc = 11 # error


# rule 3
# cannot use keywords
# for = 1
# if = 6
For = 2
print(For)
print(For + 1)

If = 3
# if = 3
#
# for = 2


# rule 4
# cannot use punctuation and symbols (except _ underscore)
# We cannot use special symbols like
# !, @, #, *, $, %, +, -, /, \, ~ etc. in our identifier

# $a = 555
# a$b = 464
# _$ = 234


# rule 5
this_is_a_long_identifier = 23456
this_is_a_long_identifier_this_is_a_long_identifier_this_is_a_long_identifier = 3456


# special identifiers
# __doc__

def adding():
    """
    this is a function of adding two numbers
    :return:
    """
    print(1 + 1)


print(adding.__doc__)


# convention
# convention v.s rule

# 1 case sensitive
Car = 'Benz'
CAR = 'Mustang'
CAr = 123

# 2 Make sure it is meaningful and readable
c = 0
counter = 0

# 3 Multiple words can be separated using an underscore
thisisalongidentifier = 345
this_is_a_long_identifier = 345
getvalue = 34
setvalue = 34
get_value = 34
set_value = 34

# 4. do not use reserved words
# print = 1
# list = [1,2,3]
# list()




































