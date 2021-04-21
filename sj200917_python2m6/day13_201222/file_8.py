"""
file creating

x - creating
"""




try:
    file = open('file_8.txt', 'x')

    file.close()

except FileExistsError as fe:
    print(fe)

except Exception as e:
    print(e)