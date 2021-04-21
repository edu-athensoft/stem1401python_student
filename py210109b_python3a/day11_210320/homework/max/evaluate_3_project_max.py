"""
Homework 9
Date: 2021-03-13
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

from tkinter import *
from time import *

start = process_time()

root = Tk()
# root.geometry('640x480+220+200')      # by Max
root.geometry('+0+0')               # by Teacher
root.config(bg='#ddddff')

try:
    colors = open('colors.txt', 'r')
    colors_list = colors.read().splitlines()

    row = 0
    column = 0
    for i in colors_list:
        row += 1

        if row > 32:
            column += 1
            row = 1
        Label(root, text=i, width=13, relief=GROOVE, bg=i, font= 'Helvetica 10', padx=10, pady=6).grid(row=row,column=column)

except FileNotFoundError:
    print("File Not Found")

except Exception as e:
    print(e)

end = process_time()
print(f"Processing time: {end-start} seconds")

root.mainloop()