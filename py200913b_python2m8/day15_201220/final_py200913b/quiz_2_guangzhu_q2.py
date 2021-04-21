"""
part 2
question 2
"""

"""
function:       ok                          5/5
structure:      ok                          1.25/1.25
convention:     ok                          1.25/1.25
comment:        ok                          1.25/1.25
user-friendly:  failed to use exception     0.75/1.25

subtotal:       9.5
"""


import os
def directory(dir, level=1):
    for i in os.listdir(dir):
        print("    "*level, i)
        if os.path.isdir(dir+os.sep+i):
            level += 1
            directory(dir+os.sep+i, level)
            level -= 1
    return directory
dir_to_list_path = input('please enter the absolute path of the directory:')
directory(dir_to_list_path)