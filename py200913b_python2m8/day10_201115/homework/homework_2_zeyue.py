"""
2. Calculate the size of a directory
"""

import os


def calcsize(path, size):
    for i in os.listdir(path):
        if os.path.isfile(f"{path}{os.sep}{i}"):
            size += os.path.getsize(f"{path}{os.sep}{i}")
        else:
            size += calcsize(f"{path}{os.sep}{i}", 0)
    return size


package_to_list = input("Input the absolute or relative path of the directory you want to list: ")

print(calcsize(package_to_list, 0))


