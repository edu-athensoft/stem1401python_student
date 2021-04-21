"""

file.read()
file.read(n)    n -> number of char

readline()

"""

try:
    file = open("homework_html.html")

    for i in file:
        # line = file.readline()
        print(i, end="")

except FileNotFoundError as fe:
    print(fe)

finally:
    file.close()





