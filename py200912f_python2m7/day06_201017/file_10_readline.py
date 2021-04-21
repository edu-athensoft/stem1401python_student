"""

file.read()
file.read(n)    n -> number of char

readline()

"""

try:
    file = open("homework_html.html")

    file.seek(2)

    line1 = file.readline(2)
    print(line1, end="")

    line2 = file.readline(2)
    print(line2, end="")

    line2 = file.readline()
    print(line2, end="")

except FileNotFoundError as fe:
    print(fe)

finally:
    file.close()





