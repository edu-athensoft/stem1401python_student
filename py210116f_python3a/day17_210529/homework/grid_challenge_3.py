"""

Grid challenge 3

Color chart

"""

from tkinter import *
from datetime import datetime

start_time = datetime.now()

MAX_ROWS = 29

root = Tk()

root.title("Grid Challenge 3 - Colour Chart")

row = 0
column = 0

file = open("COLORS", "r")
content = file.read().splitlines()
# file.readlines()
for color in content:
    one = Label(root, text=color, bg=color)
    one.grid(row=row, column=column, sticky="ew")
    row += 1
    if row > MAX_ROWS:
        row = 0
        column += 1


end_time = datetime.now()
first_time = end_time - start_time
execution_time = str(first_time).replace("0:00:0", "")
print('Execution time is {} seconds.'.format(execution_time))

root.mainloop()


