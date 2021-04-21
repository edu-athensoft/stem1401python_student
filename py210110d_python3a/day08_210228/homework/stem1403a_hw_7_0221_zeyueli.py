"""
[Homework]
Date: 2021-02-21
1. Write a GUI program of Label counter for implementing version 3.
Requirements:
(Function)
When the number reaches 10, then it comes to stop and displays the text of 'END'.
If a user clicks to close the main window, the program terminates.
(UI)
Using the layout manager of pack() for the UI.
A recommended UI design is given below.
"""

"""
score:
perfect

"""

# import tkinter as tk
from tkinter import *
from tkinter.ttk import Separator


def start_counting(mylabel):
    print("entered start_counting()")

    counter = 0

    def counting():
        nonlocal counter

        counter = counter + 1
        if counter > 10:
            counter = "END"
        mylabel.config(text=str(counter))

        if counter == "END":
            return
        mylabel.after(1000, counting)

    counting()


# main program
root = Tk()
root.title('Python GUI - Label counter')
root.geometry("{}x{}+200+240".format(800, 560))
root.configure(bg='#ddddff')

# title label object
label1 = Label(root, text="Label Counter", bg="blue", fg="white", height=2, width=100, font="Helvetic 35 bold")
label1.pack()

# separator
sep1 = Separator(root, orient=HORIZONTAL)
sep1.pack(fill=X)

# counter label object
digit_label = Label(root,
                    bg="seagreen",
                    fg='white',
                    height=8,
                    width=100,
                    font="Helvetic 30 bold")
digit_label.pack()

# separator
sep1 = Separator(root, orient=HORIZONTAL)
sep1.pack(fill=X)

# footer label object
label2 = Label(root, text="Version 3 | Ze Yue Li | 2021-02-26", bg="red", fg="white", height=2, width=100, font="Helvetic 35 bold")
label2.pack()

# counting
start_counting(digit_label)

root.mainloop()
