"""

Grid challenge 2

Color chart

"""

from tkinter import *


MAX_ROWS = 29

root = Tk()

root.title("Grid Challenge 3 - Colour Chart")

row = 0
column = 0

try:
    with open("COLORS", "r") as file:
        for line in file:
            lines = file.readline()
            for lines in line:
                for color in lines.split("', '"):
                    one = Label(root, text=color, bg=color)
                    one.grid(row=row, column=column, sticky="ew")
                    row += 1
                    if row > MAX_ROWS:
                        row = 0
                        column += 1
except FileNotFoundError as e:
    print(e)


root.mainloop()
