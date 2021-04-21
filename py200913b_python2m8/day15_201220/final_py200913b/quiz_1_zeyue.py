# Question 1

# Exception handling prevents the program from crashing when an error is encountered. It is needed to prevent the
# program from crashing.
# Syntax forms
"""
try:
    <code>
except <error>:
    <code to execute if an error is encountered>
else:
    <code to execute if there are no errors>
finally:
    <code that is executed no matter the result of the try>
"""

# Question 2

# A built-in exception is a default exception created by python.
"""
ZeroDivisionError          Occurs when a number is divided by or modulus by 0
ValueError                 Occurs when a value is not compatible with a function (for example when converting letters to int)
FileNotFoundError          Occurs when a file is not found when trying to open it with a mode that cannot create files.
IndexError                 Occurs when an index reference is out of range of the list it references.
SyntaxError                Occurs when a statement does not follow the syntax of python.
"""

# Question 3

# An user-defined exception is an exception created by the user and does not exist in other programs.
# We can organize them by category.

# Question 4

# An exception occurs when an error is raised while code in a try is ran.
# To raise an error manually, programmers can use the function raise <error>(<text>).

# Question 5

# File input is writing into a file, and file output is reading the text in a file.

# Question 6

"""
r     (Default)         Open a file in read-only mode
w                       Open a file in write-only mode
x                       Open a file for creation
t     (Default)         Open a file in text mode
b                       Open a file in binary mode
+                       Open a file in read and write mode.
"""

# Question 7

# We can use a character list that contains asian characters.

# Question 8

# We can store the file into a variable.

# Question 9

# We read it by chunks and store them afterwards. We handle them like that because python cannot read very big files at once.

# Question 10

# Use append when you want to add text to the end of a file, and use write when you want to delete all the content and write from the start.
# For a "Log" document, appending would be more suitable because it would keep the previous logs.

# Question 11

# Write writes characters 1 by 1, and writelines writes characters line by line.

# Question 12

# A tree structure is like a tree, there is a root and smaller branches coming out of the root and the other branches.
# In real life, sports tournaments or any tournaments where the competitors get eliminated when they lose, are like a tree structure.
# In programming, a computer's memory is like a tree structure, with directories and files being the branches.

# Question 13

"""
shutil.copyfile()        Copies a file's content to a new file
os.listdir()             Lists all items in a specific directory
os.rmtree()              Deletes a directory
os.mkdir()               Creates a directory
os.sep                   Contains the separator for the system on which the program is run.
os.walk()                "Walks" across the directory, accessing all the files.
os.rmdir()               Renames directory.
os.getcwd()              Returns current directory.
"""

# Question 14

# A relative path is a path that starts from a root other that the main root of the computer. An absolute path starts from
# the main root and is longer than a relative path.

# Question 15

# There are 3 ways to create a datetime object: datetime.datetime.now(), datetime.datetime.date(), datetime.datetime.fromtimestamp()

# Question 16

# To get current date and time, we can use datetime.datetime.now(). To get only the time, we can use datetime.datetime.now().time().
# To show date and time, we can use strftime("%Y-%m-%d %H:%M:%S"). To show the time with AM or PM, we can use strftime("%H:%M %p")

