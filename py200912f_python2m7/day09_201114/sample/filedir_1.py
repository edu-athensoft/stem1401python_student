"""
Check if path is existing
"""

import os

# directory
path = "d:/assist"
os.path.exists(path)

# file
path2= 'd:/assist/getTeacherList.py'
os.path.exists(path2)


if not os.path.exists(path):
    file = open(path, 'x')
    file.close()
else:
    print("Already existed.")




