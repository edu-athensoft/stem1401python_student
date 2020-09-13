"""
function arguments

arbitrary arguments

def foo(*object):
    pass

"""

# list or tuple?
# taken as a tuple


def foo(*object):
    print(object, type(object))

    for i in object:
        print(i, end="\t")
    # pass

# print('aaa','bbb','ccc',1,2,3)
foo('aaa','bbb','ccc',1,2,3)





