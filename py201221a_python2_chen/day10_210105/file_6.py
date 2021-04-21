"""
To read content from a file （i.e. text file)

filepath and filename

filepath + filename

"""

try:
    filepathname = 'testdir/file6a.txt'
    file = open(filepathname)
    print(file)
    print("==== 1")

    # read all content from the file opened
    content = file.read()
    print(content)
    print("==== 2")

    content2 = file.read()
    print(content2, end='')
    print("===== 3")

    # content2 = file.read()
    # print(content2, end='')
    # print("===== 3")
    #
    # content2 = file.read()
    # print(content2, end='')
    # print("===== 3")

except FileNotFoundError as fe:
    print(fe)

finally:
    file.close()

