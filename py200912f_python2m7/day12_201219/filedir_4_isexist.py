"""
check if a file or directory exists or not
"""

import os

# check dir
path = 'sample1'
isexist = os.path.exists(path)

print(isexist)


# check file
path = 'homework.py'
isexist = os.path.exists(path)

print(isexist)