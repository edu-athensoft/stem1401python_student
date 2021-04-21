"""
os.listdir()

list all directories and files at current path

# path =? filename

os.path.sep

forward slash -> /
backward slash -> \  (for windows)

"""



import os

try:
    # path = 'review.py'
    path = 'testdir'
    result = os.listdir(path)
    print(result, type(result))
    print()

    path = 'testdir/dir1'
    result = os.listdir(path)
    print(result, type(result))
    print()

    path = '../day09_201114'
    result = os.listdir(path)
    print(result, type(result))
# NotADirectoryError: [WinError 267] The directory name is invalid: 'review.py'

except NotADirectoryError as nde:
    print(nde)
except Exception as e:
    print(e)




