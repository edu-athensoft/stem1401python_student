"""
[Homework]
Date: 2021-05-09
Design and implement a multiple option button list on the main window.
Click on each button to show a specific toplevel window.
The number of options should be at list 5.
Due date: by the end of next Sat.
"""
from tkinter import *


def toplevel(enter):
    toplevel_window = Toplevel(root)
    toplevel_window.title(enter)
    toplevel_window.geometry('200x200')
    toplevel_label = Label(toplevel_window, text=f'this is the "{enter}" toplevel window', font='Times 10 bold')
    toplevel_label.grid(row=1, column=1)


root = Tk()
root.title("Python GUI - toplevel")
list_5 = ['a', 'b', 'c', 'd', 'e']
column = 0

for letter in list_5:
    list_button = Button(root, command=lambda enter=letter: toplevel(enter),
                         text=letter, relief='raised', height=2, width=15, padx=10, pady=10, font='Times 12 bold')
    list_button.grid(row=0, column=column, padx=10, pady=10)
    column += 1

root.mainloop()
