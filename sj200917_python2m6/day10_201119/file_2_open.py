"""
open a file
error-free

"""
# file path + filename

# Leon
try:
    file = open("file_open2.txt")
    file.close()

except FileNotFoundError as fe:
    print(fe)

except IOError as ioe:
    print(ioe)

except Exception as e:
    print("cannot open")
    print(e)






