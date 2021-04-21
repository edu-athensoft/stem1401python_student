"""
list dir(s)

listdir()
"""

import os

# current path
path = "."
result = os.listdir(path)
# print(type(result))

for name in result:
    print(name)

print()
print()

# subdir path
path = ".\\sample"
result = os.listdir(path)
# print(type(result))

for name in result:
    print(name)

print()
print()


# parent path
path = ".."
result = os.listdir(path)
# print(type(result))

for name in result:
    print(name)

print()
print()


# using absolute path
path = r"D:\workspace\pycharm201803\stem1401python_student\py200913b_python2m8"
result = os.listdir(path)
# print(type(result))

for name in result:
    print(name)
