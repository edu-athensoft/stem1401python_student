"""
tell() -

tell() and seek()

"""


try:
    filepathname = 'testdir/file6a.txt'
    file1 = open(filepathname)

    content = file1.read(1)
    print(content)

    print(file1.tell())

    content = file1.read(1)
    print(content)

    print(file1.tell())

except FileNotFoundError as fe:
    print(fe)

finally:
    file1.close()
    # file2.close()
