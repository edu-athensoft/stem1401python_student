"""
variable parameters

positional argument
"""


def f1(a, b="abc"):
    print(a, b)


f1(10, 'xyz123')

f1(10)



def f2(*a):
    print(a)

    for item in a:
        print(item)

f2(1,2,3,4,5)
f2(1,2,3)
f2(1,2,3,4,5,6,7,8,9,10)
f2()
