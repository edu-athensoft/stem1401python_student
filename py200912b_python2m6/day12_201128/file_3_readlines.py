"""
file
readlines()

readlines() v.s. readline()

readline - read file line by line, support to read large files
readlines - read all content of a file into a list
            access specific line by index
            manipulate content as a normal list

read() - read all content of a file
read(size) - read a certain number of chars, supporting big file
"""


file = open("file_1.txt", encoding="utf-8")

print("===")
content = file.readlines()
print(type(content))

for line in content:
    print(line,end='')
print("===")

# read line #2
lineno = 3
result = content[lineno-1]
print(result)

file.close()


"""
[Homework]
1. Read an HTML file
    readline() or readlines()
2. Read a CSV file
    readline() or readlines()  
3. Read a CSV file of its first half by line
    readline() or readlines()  
    
    
readline()
hint:
loop
when to break?

"""



