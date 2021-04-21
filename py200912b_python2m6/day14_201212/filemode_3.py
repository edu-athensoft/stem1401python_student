"""
read specified line(s) #

function signature
"""


def getlines(start_no,  end_no):
    pass


def getline(line_no):
    # line_no = 2

    if line_no < 1:
        return "No such line"

    with open("filemode_3.txt") as file:
        data = file.readlines()

        if line_no > len(data):
            return "No such line"

        content = data[line_no-1]
        return content


# main program
try:
    lineno = int(input("Enter a line #:"))
    print(getline(lineno), end="")
except ValueError as ve:
    print(ve)

# print(getline(1), end="")
# print(getline(2), end="")
# print(getline(3), end="")
# print(getline(4), end="")
#
# print(getline(5), end="")