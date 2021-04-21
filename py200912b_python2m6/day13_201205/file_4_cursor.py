"""
file cursor

seek()

tell()

"""

try:
    file = open("homework/myweb.html")

    content = file.read()

    print(content)
    print("=================",end="\n")

    # read from start
    file.seek(0)
    content2 = file.read()
    print(content2)
    print("=================")
    file.close()

    print("\n\n")

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)



file2 = open("homework/myweb.html")

content = file2.read(4)

print(content)
print("=================",end="\n")

# read from start
file2.seek(9)
content2 = file2.read(4)
print(content2)
print("=================")
file.close()
