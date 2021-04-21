"""
create a new file

x mode()

"""


try:
    file = open("file12.txt",'x')

    file.close()

    print("File has been create.")

except FileExistsError as fe:
    print(fe)



