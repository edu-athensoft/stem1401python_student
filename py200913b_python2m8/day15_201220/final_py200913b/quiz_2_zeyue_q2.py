"""
2. List all files and directories under a specific location. (10')
Description
List them in a tree-like layout.
Please consider setting the indentation properly.
"""

"""
function:       ok                          5/5
structure:      ok                          1.25/1.25
convention:     ok                          1.25/1.25
comment:        ok                          0/1.25
user-friendly:  failed to use exception     0.75/1.25

subtotal:       8.25
"""

import os


def listDir(path, level):
    for i in os.listdir(path):
        print("    "*level, i)
        if os.path.isdir(f"{path}{os.sep}{i}"):
            level += 1
            listDir(f"{path}{os.sep}{i}", level)
            level -= 1


dir_to_list = input("What is the directory you want to list?")
dir_to_list_path = input("What is the absolute path of the directory you want to list?")
print(dir_to_list)
listDir(dir_to_list_path, 1)

