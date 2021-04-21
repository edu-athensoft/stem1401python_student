"""
part 1
"""


# question 1
# exception handling is to prevent the system crashing while something went wrong. We need exception
# handling because if something in a plane went wrong, it won't crash
# syntaxes of exception handling:
"""
try:    |  try:       try:       try:
    xxx |     xxx        xxx        xxx
except: |  except:    except:    except:
    xxx |     xxx        xxx        xxx
else:   |  else:                 finally:
    xxx |     xxx                   xxx
finally:|
    xxx |
"""

# question 2
# 5 built-in exceptions: OSError, FileNotFoundError, FileExistsError, IOError, ValueError
# OSError is an error for the os module, when your code has imported os and have an error of the os module, then it will show OSError.
# FileNotFoundError is occurred when you open a file and the file you opened isn't there.
# FileExistsError is occurred when you create a file and the file already exists.
# IOError is occurred when an operation such as input/output fails
# ValueError is occurred when there's a problem with the content of an object when you try to assign the value of something to.


# question 3
# a user defined exception is used with the class function, it defines an exception that the user can custom. We can organize them easily
# while putting some understandable variables.

# question 4
# the user can raise an exception while using the raise function for example:
"""
x = -1
if x < 0:
     raise Exception('sorry, the number is below zero')
"""

# question 5
# input is when you enter something in the code
# output is what the code will print out

# question 6
# python file modes:
# r:  it opens a file so the user could read    DEFAULT
# t:  it opens a file in text mode              DEFAULT
# w:  it opens a file for writing
# x:  it opens a file for exclusive creation
# a:  it opens a file for appending at the end of the file without removing the text before
# b:  it opens a file in binary
# +:  it opens a file for reading+writing

# question 7
# we can open a text in asian language by using the encoding function

# question 8
# we can use for loops to open a file multiple times

# question 9
# we can use for loops to read the large file line per line. I will do it in this way because it will prevent the system from crashing.

# question 10
# We use the append mode when you want to add things to the file and the write mode when you want to truncate all and replace it with
# what you want to write. If the document has already some data records on it and you want to add more infos, it's better to use append
# mode because if we use the write mode, all the data will disappear.

# question 11
# write() is for  writing strings and writelines() is for writing lists.

# question 12
# a tree structure in python is a tree but upside-down,
# the root of the tree is on top and there's branches comes out from the root that are lower.
# in real life, the tree structure is used for example, a family tree

# question 13
# os.renames, os.rmdir, os.mkdir, os.listdir, os.getcwd

# os.renames renames the old directory in a new name.
# os.rmdir removes the directory path
# os.mkdir creates a new directory at the path you put.
# os.listdir returns a list containing the names of the file in the directory given.
# os.getcwd returns the name of the current working directory

# question 14
# the relative path is for example init.py but the absolute path is C:/Users/sdan7/stem1401python/py201129/__init__.py,
# the relative path is in the absolute path,
# the absolute path starts from the main program of the computer and the relative path starts from your file in pycharm

# question 15
# there are 4 ways to create a datetime object:
# datetime.datetime.now, datetime.date.fromtimestamp, datetime.date.today, datetime.datetime.date

# question 16
# current date AND time: datetime.datetime.now()
# current time ONLY: datetime.datetime.now().time()
# show the time like'yyyy-mm-dd HH:MM:SS': datetime.strftime("%Y-%m-%d %H:%M:%S")
# show the time like'HH:MM AM' or 'HH:MM PM': datetime.strftime('%H:%M %p')
