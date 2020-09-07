"""
dir() - is a built-in function
"""
import py200727_python2.day33_py208024.myfunc as myfunc

# print(dir(myfunc))

for name in dir(myfunc):
    print(name)


print(myfunc.__doc__)


import math
for name in dir(math):
    print(name)