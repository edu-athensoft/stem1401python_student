"""
File explorer
Finder

file, directory

File is a named location on disk to store related information.


open()
"""

# case 3. open file in specified full path
print("[info] open file in specified full path")
print("[info] opening file3_open.txt ...")

try:
    f = open(r"D:\workspace\pycharm201803\stem1401python_student\py200510_python2\day18_py200715\file3_open.txt")

    print("[info] closing ...")
    f.close()

    print("[info] done.")
except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)


