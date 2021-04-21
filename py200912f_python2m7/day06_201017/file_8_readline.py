"""

file.read()
file.read(n)    n -> number of char

readline()

"""

try:
    file = open("homework_html.html")

    line = file.readline()
    # print(line, end="\n")
    print(line, end="")

    line = file.readline()
    print(line, end="")

    line = file.readline()
    print(line, end="")

    line = file.readline()
    print(line, end="")

    line = file.readline()
    print(line, end="")

except FileNotFoundError as fe:
    print(fe)

finally:
    file.close()





