"""
file operation

read()
read(size)
readline()
readlines()
"""

try:
    # step 1. open a file
    file1 = open('file_1.txt')

    # step 2. operate on the opened file
    # round 1
    content = file1.read()
    print(content)
    print("==================")

    file1.close()

    # round 2
    file1 = open('file_1.txt')
    content2 = file1.read()
    print(content2)

    # step 3. close the file
    file1.close()

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)









