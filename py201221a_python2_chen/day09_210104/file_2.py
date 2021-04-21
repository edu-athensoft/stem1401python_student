"""

3 step to operate on a file

step 1. Open a file
step 2. Read/Write (perform operation)
step 3. Close the file

"""


# open()

try:
    file = open('text1.txt1')
    print(file)

except FileNotFoundError as fe:
    print(fe)




