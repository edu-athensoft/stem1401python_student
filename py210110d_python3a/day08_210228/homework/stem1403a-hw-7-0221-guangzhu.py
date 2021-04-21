"""
[Homework]
Date: 2021-02-20
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
no enough white spaces (-1)
improper font size at footer (-1)

invalid char in file name (-1)

"""


from tkinter import *
from tkinter.ttk import Separator
# main program
root = Tk()
root.title('Counter to 10')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')
def start_counting(mylabel):
    print('entered start counting')
    counter = 0
    def counting():
       nonlocal counter
       counter = counter + 1
       digit_label.config(text=counter)
       digit_label.after(1000,counting)
       if counter > 10:
           counter += 0
           digit_label.config(text='END')

           root.update()
    counting()

# label object
title_label = Label(root,text='Counter to 10', bg='navy', fg='snow', height=2, width=50, font='Roman 24 bold')
title_label.pack(side=TOP)
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)
digit_label = Label(root,
              bg = "seagreen",
              fg = 'white',
              height = 5,
              width = 50,
              font = "Helvetic 48 bold",relief='groove')
digit_label.pack()
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)
footer_label = Label(root, text='Version 1, Guang Zhu, 25/02/2021', bg='snow', fg='PeachPuff3', width=50, height=2, font='Roman 24 bold')
footer_label.pack(side=BOTTOM)
start_counting(digit_label)

root.mainloop()

