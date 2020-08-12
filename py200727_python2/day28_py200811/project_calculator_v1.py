"""
project: calculator
version 1.

Menu system
1.1 adding
1.2 subtracting
1.3 multiplying
1.4 division
1.5 floor division
1.6 modulus
1.7 exponent
2.1 logical and
2.2 logical or
2.3 logical not

user can choose an operation
    user can perform arithmetic operation
    user can perform logical operation
user can input operand(s) as needed

hints:
function
input()
"""

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def mul(x,y):
    return x * y

def div(x, y):
    return x/y

def logical_and(x, y):
    return x and y


# print out the menu with options that user can input
"""
My Calculator

Arithmetic Operation
1. adding
2. subtracting
3. multiplying
4. division
...

Logical Operation
8. and
9. or
10. not

Please choose an operation [1-10]:
"""

print("=== My Calculator ===")

# print out the menu



opt = input("Please choose an operation [1-10]:")

if opt == '1':
    pass
elif opt == '2':
    pass
#
#
else:
    pass

print("Good bye!")








