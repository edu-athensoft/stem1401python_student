"""
Mini project:
v1. do arithmetic operation
    +, -, *, /
v2. upgrade
"""
# calculate
def add(x, y):
    return print("{} + {} = {}".format(x, y, x + y))


def subtract(x, y):
    return print("{} - {} = {}".format(x, y, x - y))


def multiply(x, y):
    return print("{} * {} = {}".format(x, y, x * y))


def divide(x, y):
    return print("{} / {} = {}".format(x, y, x / y))


def and_(x, y):
    if x == "True" and y == "True":
        return "True"
    elif x == "True" and y == "False":
        return "False"
    elif x == "False" and y == "True":
        return "False"
    elif x == "False" and y == "False":
        return "False"


def or_(x, y):
    if x == "True" and y == "True":
        return "True"
    elif x == "True" and y == "False":
        return "True"
    elif x == "False" and y == "True":
        return "True"
    elif x == "False" and y == "False":
        return "False"


def not_(x):
    if x == "True":
        return "False"
    elif x == "False":
        return "True"


# the operation
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. And \n6. Or \n7. Not")
operation = int(input("Please input the operation you want: "))
while operation != 1 or operation != 2 or operation != 3 or operation != 4 or operation != 5 or operation != 6 or operation != 7:
    if operation == 1 or operation == 2 or operation == 3 or operation == 4 or operation != 5 or operation != 6 or operation != 7:
        break
    print("That is not a supported operation")
    print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. And \n6. Or \n7. Not")
    operation = int(input("Please input the operation you want: "))
# values
if operation == 1 or operation == 2 or operation == 3 or operation == 4:
    value1 = float(input("Please input your first value: "))
    value2 = float(input("Please input your second value: "))
elif operation == 5 or operation == 6:
    value1 = input("Please input True or False: ")
    value2 = input("Please input True or False: ")
else:
    value1 = input("Please input True or False: ")
# returned value
if operation == 1:
    add(value1, value2)
elif operation == 2:
    subtract(value1, value2)
elif operation == 3:
    multiply(value1, value2)
elif operation == 4:
    divide(value1, value2)
elif operation == 5:
    print(f"{value1} and {value2} = {and_(value1, value2)}")
elif operation == 6:
    print(f"{value1} or {value2} = {or_(value1, value2)}")
elif operation == 7:
    print(f"{value1} not = {not_(value1)}")