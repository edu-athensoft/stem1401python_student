"""
readline()

"""

try:
    filepathname = 'testdir/file6a.txt'
    file1 = open(filepathname)

    content = file1.readline()
    # print(type(content))
    print(content,end='')

    content = file1.readline()
    # print(type(content))
    print(content,end='')

    # content = file1.readline()
    # # print(type(content))
    # print(content,end='')
    #
    # content = file1.readline()
    # # print(type(content))
    # print(content,end='')


except FileNotFoundError as fe:
    print(fe)

finally:
    file1.close()