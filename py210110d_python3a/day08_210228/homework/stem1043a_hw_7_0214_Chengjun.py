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
Due date: by the end of next Friday
"""

"""
score:
not executable	(-35)
not test apparently

one fatal error (-10)
"""

from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title('Counting')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

def run_counter(digit):

    def counting(digit):
        global counter
        counter += 1
        digit.config(text=counter)
        digit.after(1000, counting)
        if counter > 10:
            counter += 0
            # digit.label.config(text='END')
            digit.config(text='END')

    counting(digit)
    ### fatal error

title_label = Label(root,text='Counting', bg='snow', fg='#ddddff', height=2, width=40, font='Roman 12 bold')
title_label.pack(padx = 20,pady = 20)
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)
digit_label = Label(root,
              bg = "seagreen",
              fg = 'white',
              height = 3,
              width = 40,
              font = "Roman 35 bold",relief='groove')
digit_label.pack()
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)
footer_label = Label(root, text='Version1_Chengjun_2021_02_26', bg='snow', fg='#ddddff', width=40, height=2, font='Roman 12 bold')
footer_label.pack(padx = 20,pady = 20)

counter = 0
run_counter(digit_label)
root.mainloop()