"""
anonymous function (lambda function)
"""

# syntax
# lambda arg1,[arg2,arg3,...] : expr


def foo(x):
    return x
    # print("foo({})".format(x))


print("foo({})".format(1))
print("foo({})".format(2))
print("foo({})".format("abc"))
print("foo({})".format(True))
print("foo({})".format([1,2,3]))
print()

# case 1. def lambda
foo2 = lambda x: x
print(foo2(1))
print(foo2(2))
print(foo2("abc"))
print(foo2(True))
print(foo2([1,2,3]))
print()

# case 2. def lambda
foo3 = lambda x : 2*x
print(foo3(9))




