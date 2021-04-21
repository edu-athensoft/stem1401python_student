"""
file operation

readline()
readlines()
"""

try:
    # step 1. open a file
    file1 = open('file_1.txt')

    # step 2. operate on the opened file
    # line = file1.readline()
    # print(line,end="")
    #
    # while line:
    #     line = file1.readline()
    #     print(line, end="")


    # while line = file1.readline():
    #     # line = file1.readline()
    #     print(line, end="")

    while True:
        line = file1.readline()
        print(line, end="")
        if not line:
            break

    # step 3. close the file
    file1.close()

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)









