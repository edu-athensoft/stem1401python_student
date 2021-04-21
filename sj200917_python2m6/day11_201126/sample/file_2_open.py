"""
File operation

0. locate
1. open a file
2. read/write
3. close the file
"""

"""
open a file
open(filename)
open(location+filename)
"""

# case 1.
f = open('file2.txt')
print(f)

# case 2. open a file which does not exist

# fa = open('file2a.txt')
# print(fa)

# FileNotFoundError
try:
    fa = open('file2a.txt')
    print(fa)
except FileNotFoundError as e:
    print("No such file.")
except Exception as e:
    print("Unknown error.")





