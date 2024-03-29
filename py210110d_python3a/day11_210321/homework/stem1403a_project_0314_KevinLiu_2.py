"""
Date: 2021-03-14
Project.  Full Color Charts
Description:
Save all color names into an external text file
Read the data (of color names) files
Display a full color chart
Calculate the execution time
Hints:
You may set MAX_ROWS or MAX_COLUMNS as you wish
All cells must be of equal width
Exception handling
Data file:
evaluate_3_project/full_color_chart/colors.txt
Required Tech:
tkinter (Label, grid layout)
flow control, arithmetic operation, file io, exception handling, date and time
Due date: by the end of next Friday
"""

# import tkinter module
from tkinter import *
# datetime module
import datetime
import os


# root
root = Tk()
root.title("Python GUI")


# start time of execution
start = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S.%f"), "%H:%M:%S.%f")
# print(f"The execution started at {start}")


# main program
try:
    # f = open("evaluate_3_project/full_color_chart/colors.txt", "r")
    f = open("colors.txt")

    colorlist = f.readlines()

    f.close()
except EXCEPTION as e:
    print(e)
    os._exit()


# generate list of color names
colors_from_file = []

# clean color name
for color in colorlist:
    color = color.strip()
    colors_from_file.append(color)
    # print(c)

# print(colors_from_file)

# color chart settings
max_rows = 40
max_cols = len(colors_from_file)//max_rows + 1
row = 0
col = 0

# generate labels for the color chart
for c in colors_from_file:
    Label(text=c, bg=c, font=(None, 9)).grid(row=row, column=col, sticky= E+W)

    row += 1
    if row > max_rows:
        row = 0
        col += 1

for col in range(max_cols):
    root.columnconfigure(col, minsize=120)


root.mainloop()

# end of execution
end = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S.%f"), "%H:%M:%S.%f")
# print(f"The execution ended at {end}")

# execution time
operation_time = end - start
print(f"The execution time was {operation_time}s")
