"""
change directory

chdir()
"""

import os

# before
current_path = os.getcwd()
print(current_path)


# after
os.chdir(r'D:\workspace\pycharm201803\stem1401python_student\py200912f_python2m7\day09_201114\homework')
changed_path = os.getcwd()
print(changed_path)



"""
# relative path
os.chdir(r'..\\..\\..')
changed_path = os.getcwd()
print(changed_path)
print()

# relative path
os.chdir(r'py200913b_python2m8')
changed_path = os.getcwd()
print(changed_path)
"""

