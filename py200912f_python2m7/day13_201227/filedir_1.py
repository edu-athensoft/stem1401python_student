"""
to check if a path is existing
"""


import os



# case 1. directory or folder
path = '../day12_201219'
result = os.path.exists(path)
print(f"The path of {path} exists? {result}")

# case 2. files or documents
path = '../filedir_1_rmfile.py'
path = r'D:\workspace\pycharm201803\stem1401python_student\py200912f_python2m7\day12_201219\filedir_1_rmfile.py'
result = os.path.exists(path)
print(f"The path of {path} exists? {result}")


