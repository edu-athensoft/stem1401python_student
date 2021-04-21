"""
file writing

a - appending

"""


try:
    # step 1. open
    file = open("file_7.txt",'a')

    # step 2. save
    content = "aaaa This is what I would like to save permanently.\n"

    file.write(content)

    # step 3. close
    file.close()


except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)