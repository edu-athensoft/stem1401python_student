"""[Homework]
Date: 2021-05-09
Design and implement a multiple option button list on the main window.
Click on each button to show a specific toplevel window.
The number of options should be at list 5.
Due date: by the end of next Sat.
"""

from tkinter import *


def windows(enter):
    window = Toplevel(root)
    window.title(enter)
    window.geometry("260x180")
    window.mainloop()


root = Tk()
root.title("Hw_Chengjun ")
root.geometry("+200+200")
root.config(bg="#ddddff")

button_List = ["A-window", "B-window", "C-window", "D-window", "E-window"]
column = 0

for Words in button_List:
    list_button = Button(root, command=lambda enter=Words: windows(enter),
                         text=Words, relief='raised', height=2, width=15, padx=10, pady=10, font='Times 12 bold')
    list_button.grid(row=0, column=column, padx=10, pady=10)
    column += 1

root.mainloop()
