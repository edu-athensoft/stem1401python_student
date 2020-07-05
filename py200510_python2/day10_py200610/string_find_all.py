"""
yield (generate)
function
iterator
compare with return
"""

def foo():
    for i in range(3):
        yield i

f = foo()
print(f.__next__())
print(f.__next__())
print(f.__next__())
