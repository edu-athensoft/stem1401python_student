"""
get color names from a file
"""


def getColors(fname):
    """
    get all color names from the specified file
    :param fname: file name of data
    :return: the list of color names
    """
    colors = []

    with open(fname) as colorfile:
        color = colorfile.readline().strip()

        while color:
            print(color)
            colors.append(color)
            color = colorfile.readline()
            color = color.strip()

    return colors


# main program
# filename = 'colors.txt'
filename = 'mycolors.data'
COLORS = getColors(filename)

# test colors
print(COLORS)

