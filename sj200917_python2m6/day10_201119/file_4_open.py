"""
open a file at a specified location
error-free

mode of file opening
r       for reading
w       for writing
x       for creating
a       for appending

t       in text mode
b       in binary mode

rb      mode for reading a binary file
rt      mode for reading a text file

wt
wb

default: none   (rt)
default: w      (wt)
default: r      (rt)

+       plus
r+      r/w
a+      w/r
w+      w/r

combination:
r+b     r/w binary file
r+t     r/w text file
w+b     r/w binary file


"""

import os

try:
    # filename = "sample/file1_open.txt"
    # file = open(filename)

    filepath = "sample"
    filename = "file1_open.txt"
    fullname = filepath+os.path.sep+filename
    print(f"fullname = {fullname}")

    file = open(fullname)

    print("Opening sample/file1_open.txt ...")
    file.close()
    print("Opened.")

except FileNotFoundError as fe:
    print(fe)

except IOError as ioe:
    print(ioe)

except Exception as e:
    print("cannot open")
    print(e)






