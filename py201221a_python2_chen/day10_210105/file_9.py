"""


"""


try:
    filepathname = 'testdir/file6a.txt'
    file1 = open(filepathname)

    # 1st round
    content = file1.read()
    print(content)

    # 2nd round
    file2 = open(filepathname)
    content = file2.read()
    print(content)

except FileNotFoundError as fe:
    print(fe)

finally:
    file1.close()
    file2.close()
