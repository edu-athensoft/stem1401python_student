"""
create a new file

x mode()

"""


try:
    file = open("file13.txt",'x')

    content = "test file writing\n"
    file.write(content)
    file.close()

    file = open("file13.txt")
    content = file.read()
    print(content)
    file.close()

    print("File has been create.")

except FileExistsError as fe:
    print(fe)



