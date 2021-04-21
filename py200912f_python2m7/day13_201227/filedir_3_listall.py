"""
list all directories and files with subdirectories under specified directory

listdir()

test each one of returned path

if the path item is a directory,
    then listdir() it again
else
    then print(file path)

"""


import os

# result = os.listdir(path)
# print(result)


def list_current(path):
    result = os.listdir(path)

    for item in result:
        print(item, os.path.isdir(path+'/'+item))

        if os.path.isdir(path+'/'+item):
            # expand this sub-dir
            path = path + '/' + item
            print(f"path = {path}")
            list_current(path)

    # return result


path = '.'
res = list_current(path)
# print(res)
