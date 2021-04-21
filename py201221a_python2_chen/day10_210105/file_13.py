"""
readline()

"""

try:
    filepathname = 'testdir/file6a.txt'
    file1 = open(filepathname)

    content = '1'

    while content:
        content = file1.readline()
        print(content,end='')


except FileNotFoundError as fe:
    print(fe)

finally:
    file1.close()