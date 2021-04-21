"""
Homework 10
"""

from tkinter import *

def getColors(fname):
    colors = []

    with open(fname) as colorfile:
        color = colorfile.readline().strip()

        while color:
            colors.append(color)
            color = colorfile.readline()
            color = color.strip()
    return colors

root = Tk()
root.title('Python GUI - pack file')

MAX_ROWS = 34
FONT_SIZE = 5 # (pixels)

row = 0
col = 0

filename = 'file_1.txt'
colors = getColors(filename)

try:
    for color in colors:
        e = Label(root, text=color, width=12,
                  font= 'Helvetica 7',
                  padx=11, pady=6).grid(row=row, column=col, sticky=E + W)

        e = Label(root, bg=color, width=12,
                  font= 'Helvetica 7',
                  padx=11, pady=6).grid(row=row, column=col+1, sticky=E + W)

        row += 1
        if (row > MAX_ROWS):
            row = 0
            col += 2

except FileNotFoundError:
    print("File Not Found")

except Exception as e:
    print(e)

mainloop()