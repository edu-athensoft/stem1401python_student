"""
read()
read by size

parameter: size - int
read(size)

size is the number of char NOT the number of byte

"""

try:
    filepathname = 'testdir/file6a.txt'
    file = open(filepathname)
    print(file)
    print("==== 1")

    # read all content from the file opened
    SIZE = 5
    content_by_size = file.read(SIZE)

    print(content_by_size)

except FileNotFoundError as fe:
    print(fe)

finally:
    file.close()

