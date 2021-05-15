"""
grid challenge 1

color chart
"""

from tkinter import *

root = Tk()

root.config(bg="gray91")

colors = ("red", "orange", "yellow", "green", "cyan", "blue", "purple")

row_index = -1

for color in colors:
    row_index += 1
    Label(root, text=color, bg="gray90", relief="raised").grid(row=row_index, column=0, ipadx=50, ipady=10, sticky="nsew")
    Label(root, bg=color).grid(row=row_index, column=1, ipadx=50, ipady=10)

root.mainloop()
