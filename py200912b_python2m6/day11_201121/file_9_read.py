"""
file mode

how to read a text file
read()

encoding:
utf-8
ascii
cp1252

"""

# import os
# import os.path
try:
    print("Start opening file...")
    filepath = "file_8.txt"
    print("\t"+filepath)
    # file = open(filepath, 'rt', encoding="utf-8")
    # file = open(filepath, encoding="utf-8")
    file = open(filepath, encoding="ascii")

    print("==================")
    content = file.read()
    print(content)
    print("==================")

    print("Closing...")
    file.close()

except FileNotFoundError as fe:
    print(fe)

except IOError as ioe:
    print(ioe)

except UnicodeDecodeError as ude:
    print(ude)

except Exception as e:
    print(e)

print("Done.")

