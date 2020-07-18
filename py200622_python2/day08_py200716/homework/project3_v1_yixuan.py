"""
v1. do arithmetic operator
     + , - , * , /
v2. upgrade
"""
def add(x, c):
    s = x + c
    return s
def moin(x, c):
    s = x + c
    return s
def mul(x, c):
    s = x + c
    return s
def div(x, c):
    s = x + c
    return s
def logical_and(x, c, z):
    s = x > z and c < z
def logical_or(x, c, z):
    s = x > z and c < z
def logical_not(x, c, z):
    s = x > z and c < z
print("==Calculer==")
print("1: add")
print("2: moin")
print("3: mul")
print("4: div")
print("5: logical_and")
print("6: logical_or")
print("7: logical_not")
choice = input("choice(1/2/3/4/5/6/7):")
if choice == '1':
        x = float(input("a number:"))
        c = float(input("a number:"))
        addition = add(x, c)
        print("the number {} + {} = {}".format(x, c, addition))
if choice == '2':
        x = float(input("a number:"))
        c = float(input("a number:"))
        soustraction = moin(x, c)
        print("the number {} - {} = {}".format(x, c, soustraction))
if choice == '3':
        x = float(input("a number:"))
        c = float(input("a number:"))
        multiple = mul(x, c)
        print("the number {} * {} = {}".format(x, c, multiple))
if choice == '4':
        x = float(input("a number:"))
        c = float(input("a number:"))
        division = div(x, c)
        print("the number {} / {} = {}".format(x, c, division))
if choice == '5':
    x = float(input("a number:"))
    c = float(input("a number:"))
    z = float(input("a number compere:"))
    logical = logical_and(x, c, z)
    print("the number {} > {} and {} < {} = {}".format(x, z, c, z, logical))
if choice == '6':
    x = float(input("a number:"))
    c = float(input("a number:"))
    z = float(input("a number compere:"))
    logical = logical_or(x, c, z)
    print("the number {} > {} and {} < {} = {}".format(x, z, c, z, logical))
if choice == '7':
    x = float(input("a number:"))
    c = float(input("a number:"))
    z = float(input("a number compere:"))
    logical = logical_or(x, c, z)
    print("the number {} > {} and {} < {} = {}".format(x, z, c, z, logical))