"""
read a binary file
i.e. image file
"""


try:
    # step 1. open a file
    img = open('pic1.jpg','rb')

    # step 2. operate on the opened file
    content = img.read()
    print(content)

    # step 3. close the file
    img.close()

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)