"""
to check if a file or dir does exist
"""


import os

# check for a file
filename = 'review_1.py'
isexists = os.path.exists(filename)
print(f'The {filename} does exist. {isexists}')

# check for a not-existing file
filename = 'review_1'
isexists = os.path.exists(filename)
print(f'The {filename} does exist. {isexists}')

# check for a dir
dirname = 'testdir'
flag = os.path.exists(dirname)
print(flag)

# check for a dir
dirname = 'testdir2'
flag = os.path.exists(dirname)
print(flag)





