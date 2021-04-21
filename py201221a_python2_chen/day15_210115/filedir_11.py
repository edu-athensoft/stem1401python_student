"""
to check if an entity is a file(document) or a directory(folder)

os.path.isdir() - to check if it is a directory
returns - True or False

os.path.isfile() - to check if it is a file
returns - True or False

"""

import os

path = 'homework_210114.py'

# to check if it is a file
is_a_file = os.path.isfile(path)
print(is_a_file)

# to check if it is a dir
is_a_dir = os.path.isdir(path)
print(is_a_dir)


# let list all the size of files under a specified directory
# we should skip all the (sub)directories

#
path = '.'

# to list all things under the directory
# os.listdir()

filelist = os.listdir(path)
print(filelist)

# for
for item in filelist:
    is_a_file = os.path.isfile(item)
    # print(is_a_file)

    if is_a_file:
        print(f'the size of {item} is {os.path.getsize(item)} bytes')



