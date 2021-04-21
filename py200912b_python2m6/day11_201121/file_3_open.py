"""
open a file
operate
close

file path(location)
file name
file path + file name

When to omit file path?
under the same directory or path

file path:
1. absolute path
D:\workspace\pycharm201803\stem1401python_student\py200912b_python2m6\day11_201121\file_1.txt

2. relative path
py200912b_python2m6/day11_201121/file_1.txt

"""

# import os
# import os.path

print("Start opening file...")
file = open("file_1.txt")

print("Closing...")
file.close()

print("Done.")

