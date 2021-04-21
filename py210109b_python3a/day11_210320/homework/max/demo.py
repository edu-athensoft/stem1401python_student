"""

"""


with open('colors.txt') as file:
    colors = file.readlines()
    print(type(colors))

for color in colors:
    color = color.strip()
    print(color,end='')