"""
change current directory

absolute path
"""


import os

current_path = os.getcwd()
print(current_path)

os.chdir(r"D:\workspace\pycharm201803\stem1401python_student\py200912b_python2m6\day12_201128")

current_path = os.getcwd()
print(current_path)