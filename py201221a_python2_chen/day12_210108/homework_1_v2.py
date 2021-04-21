"""
[Homework]  2021-01-06
Read all content from a text file and write them into another file at the same location

to optimize the code to make it safer

"""


try:
    # sub-problem 1
    file1 = open('datasource.txt')
    content = file1.read()
    print(content)

    # sub-problem 2
    file2 = open('datadest.txt','w')
    file2.write(content)

except FileNotFoundError as fe:
    print(fe)

except IOError as ioe:
    print(ioe)

except Exception as e:
    print(e)

finally:
    file1.close()
    file2.close()

