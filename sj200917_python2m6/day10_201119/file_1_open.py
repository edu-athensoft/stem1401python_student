"""
open a file at current dir/path
"""
# file path + filename
file = open("file_open.txt")
file.close()

# relative path
file = open("testdir/test1.py")
file.close()


file = open("testdir/test1.py")
file.close()


file = open("../day11_201126/testdir2/test2.py")
file.close()
# FileNotFoundError
# file = open("file_open2.txt")
# file.close()





