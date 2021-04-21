"""
file operation

readlines()
"""

try:
    # step 1. open a file
    file1 = open('file_1.txt')

    # step 2. operate on the opened file
    content = file1.readlines()
    print(type(content))
    print(content)

    for line in content:
        print(line, end="")

    print("\n")

    # print specified line(s)
    # print line #1
    print(content[0])

    print(content[1:4])


    # step 3. close the file
    file1.close()

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)