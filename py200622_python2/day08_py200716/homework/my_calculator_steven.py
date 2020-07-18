"""
v1. doing arithmetic operation
   +, -, *, /

v2. upgrade
   add logical operation
   and, or, not

"""

def And(a, b):
    # if a == "True" and b == "False":
    #     return "False"
    # if a == "False" and b == "True":
    #     return "False"
    # if a == "True" and b == "True":
    #     return "True"
    # if a == "False" and b == "False":
    #     return "False"

    return a and b


def Or(a,b):
    # if a == "False" and b == "True":
    #     return "True"
    # if a == "True" and b == "False":
    #     return "True"
    # if a == "False" and b == "False":
    #     return "False"
    # if a == "True" and b == "True":
    #     return "True"
    return a or b

def Not(a):
    # if a == "True":
    #     return "False"
    # if a == "False":
    #     return "True"

    return not a


def add(a, b):
    return a + b

def times(a, b):
    return a * b

def minus(a, b):
    return a - b

def division(a, b):
    return a / b


print("=== My Calculator ===")
print()

print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. and")
print("6. or")
print("7. not")
print()
choice1 = input("Please choose the number of the calculation method:")
print()



if choice1 == "1":
    a = float(input("Please enter your first number to calculate: "))
    b = float(input("Please enter your second number to calculate: "))
    print(f"{a} + {b} =", add(a, b))

if choice1 == "2":
    a = float(input("Please enter your first number to calculate: "))
    b = float(input("Please enter your second number to calculate: "))
    print(f"{a} - {b} =",minus(a, b))

if choice1 == "3":
    a = float(input("Please enter your first number to calculate: "))
    b = float(input("Please enter your second number to calculate: "))
    print(f"{a} * {b} =", times(a, b))

if choice1 == "4":
    a = float(input("Please enter your first number to calculate: "))
    b = float(input("Please enter your second number to calculate: "))
    print(f"{a} / {b} =", division(a, b))

if choice1 == "5":
    a = eval(input("Please enter True or False: "))
    b = eval(input("Please enter True or False: "))
    print(f"{a} and {b} = {And(a,b)}")

if choice1 == "6":
    a = eval(input("Please enter True or False: "))
    b = eval(input("Please enter True or False: "))
    print(f"{a} or {b} = {Or(a,b)}")

if choice1 == "7":
    a = eval(input("Please enter True or False: "))
    print(f"Not {a} = {Not(a)}")





