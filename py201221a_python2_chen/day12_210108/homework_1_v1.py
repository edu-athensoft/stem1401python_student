"""
[Homework]  2021-01-06
Read all content from a text file and write them into another file at the same location

problem 1. Read all content
constraints:
    read a text file

problem 2. Write what you read
constraints:
    write to the file at the same location

"""

# sub-problem 1
file = open('datasource.txt')
content = file.read()
print(content)
file.close()


# sub-problem 2
file = open('datadest.txt','w')
file.write(content)
file.close()
