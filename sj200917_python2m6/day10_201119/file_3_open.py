"""
open a file at a specified location
error-free

"""
# file path + filename

# Leon
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






