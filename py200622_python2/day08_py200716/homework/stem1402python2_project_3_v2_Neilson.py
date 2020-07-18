"""
Project 3 v2
"""


def And(x, y):
    if a == "True" and b == "False":
        return "False"
    if a == "False" and b == "True":
        return "False"
    if a == "True" and b == "True":
        return "True"
    if a == "False" and b == "False":
        return "True"


def Or(x, y):
    if a == "False" and b == "True":
        return "True"
    if a == "True" and b == "False":
        return "True"
    if a == "False" and b == "False":
        return "False"
    if a == "True" and b == "True":
        return "True"


def Not(x):
    if a == "True":
        return "False"
    if a == "False":
        return "True"


def addition(x, y):
    return x + y


def multiplication(x, y):
    return x * y


def subtraction(x, y):
    return x - y


def division(x, y):
    return x / y


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
choice1 = int(input("Please enter your choice in form of integer:"))
print()

if choice1 == "1":
    a = float(input("Please enter your first number to calculate: "))
    b = float(input("Please enter your second number to calculate: "))
    print(f"{a} + {b} =", addition(a, b))

elif choice1 == "2":
    a = float(input("Please enter your first number to calculate: "))
    b = float(input("Please enter your second number to calculate: "))
    print(f"{a} - {b} =", subtraction(a, b))

elif choice1 == "3":
    a = float(input("Please enter your first number to calculate: "))
    b = float(input("Please enter your second number to calculate: "))
    print(f"{a} * {b} =", multiplication(a, b))

elif choice1 == "4":
    a = float(input("Please enter your first number to calculate: "))
    b = float(input("Please enter your second number to calculate: "))
    print(f"{a} / {b} =", division(a, b))

elif choice1 == "5":
    a = input("Please enter True or False: ")
    b = input("Please enter True or False: ")
    print(f"{a} and {b} = {And(a, b)}")

elif choice1 == "6":
    a = input("Please enter True or False: ")
    b = input("Please enter True or False: ")
    print(f"{a} or {b} = {Or(a, b)}")

elif choice1 == "7":
    a = input("Please enter True or False: ")
    print(f"Not {a} = {Not(a)}")

else:
    print("Error")
