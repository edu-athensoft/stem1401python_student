"""
to read a file
readlines() - returns a list - can only read small files


readline() - large files


[, , , , ,]

goal is to read and get the content of the file

"""

# list1 = [1,2,3,4,5]

# print list directly
# print(list1)


# to print item by item
# using a for loop



try:
    file = open('text14.txt')
    content = file.readlines()

    print(type(content))

    # 1. print them out
    print(content)

    # 2. how to print lines one by one?
    for line in content:
        # print(line, end="\n")
        print(line, end="")

except FileNotFoundError as fe:
    print(fe)

finally:
    file.close()

