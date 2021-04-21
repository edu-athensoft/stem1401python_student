"""

file.read()
file.read(n)    n -> number of char

readlines()

"""

try:
    file = open("homework_html.html")

    result = file.readlines()
    # print(type(result))

    # print(result)
    print(len(result[0]))
    print(len(result[1]))
    print(len(result[2]), result[2])


    # for item in result:
    #     print(item, end="")

except FileNotFoundError as fe:
    print(fe)

finally:
    file.close()


"""
[Homework]
1. Write a program to read a text file and calculate how many lines it contains.
2. Write a program to read a text file and calculate what size (how many characters) it is (it has).

3. Write a program to reproduce SyntaxError. Three syntax errors are required
4. Write a program to reproduce IndexError
5. Write a program to reproduce TypeError

"""


