try:
    file = open("File_To_Copy")
    content = file.read()
    file_2 = open("NewFile", "x")
    file_2.write(content)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
