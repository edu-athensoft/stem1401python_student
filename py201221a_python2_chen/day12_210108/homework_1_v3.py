"""
[Homework]  2021-01-06
Read all content from a text file and write them into another file at the same location

to optimize the code to make it flexible and reusable


iteration
increamental

"""

def copy(src, dest):
    try:
        # sub-problem 1
        # 'datasource.txt'
        file1 = open(src)
        content = file1.read()
        print(content)

        # sub-problem 2
        # 'datadest.txt'
        file2 = open(dest,'w')
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

# main program
src = 'datasource.txt'
dest ='mydest.txt'
copy(src, dest)
