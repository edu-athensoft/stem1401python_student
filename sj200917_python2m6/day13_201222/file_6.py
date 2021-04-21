"""
file i/o - writing

file mode
w   - writing
a   - appending
x   - creating
"""


try:
    # step 1. open
    file = open("file_6.txt",'w')

    # step 2. save
    content = "This is what I would like to save permanently."

    file.write(content)

    # step 3. close
    file.close()


except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

