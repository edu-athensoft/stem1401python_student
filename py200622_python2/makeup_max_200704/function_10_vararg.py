"""
function variable argument

print(*object, sep=" ", end="\n")
"""


print()
print(1)
print(1,2)
print(1,2,3)
print(1,2,3,4)


# user defined function with variable parameter

# list all the names you input
# function name: listname

def listname(*x):
    print(*x, type(*x))

listname("Max", "Kevin", "Athens", "Neilson")


def listname2(*names):
    # print(names, type(names))
    for name in names:
        print(name)


listname2("Max", "Kevin", "Athens", "Neilson")



