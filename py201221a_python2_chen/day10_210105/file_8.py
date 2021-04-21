"""
read()
read by size

parameter: size - int
read(size)

size is the number of char NOT the number of byte

read(size) makes file cursor move
read(size) start to read from the location where the file cursor stays at the moment
read(size) reads till the EOF
we can use for/while loop to perform reading work

"""

try:
    filepathname = 'testdir/file6a.txt'
    file = open(filepathname)
    print(file)
    print("==== 1")

    # read all content from the file opened
    SIZE = 5

    # 1st round
    content_by_size = file.read(SIZE)
    print(content_by_size)

    # 2nd round
    content_by_size = file.read(SIZE)
    print(content_by_size)


except FileNotFoundError as fe:
    print(fe)

finally:
    file.close()

