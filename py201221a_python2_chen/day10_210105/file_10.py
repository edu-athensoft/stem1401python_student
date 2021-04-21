"""
seek(size)

size - Byte , not by Char


"""


try:
    filepathname = 'testdir/file6a.txt'
    file1 = open(filepathname)

    # 1st round
    content = file1.read()
    print(content)

    # 2nd round
    # file1.seek(0)

    file1.seek(1)

    content = file1.read()
    print(content)



except FileNotFoundError as fe:
    print(fe)

finally:
    file1.close()
    # file2.close()
