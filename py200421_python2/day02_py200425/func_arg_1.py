"""
function argument
"""

# case 1. accepting no arguments
def myfoo1():
    print("myfoo1()")

myfoo1()

print()

# case 2. accepting one argument
def myfoo2(name):
    print("myfoo2(name)")
    print("name=",name)

myfoo2("Peter")

# myfoo2()

print()

# case 3. accepting two or more specified arguments
def myfoo3(name, msg):
    print("myfoo3(name,msg)")
    print("name=",name, "msg=",msg)

# myfoo3("Peter")
myfoo3("Peter","You passed the exam")
