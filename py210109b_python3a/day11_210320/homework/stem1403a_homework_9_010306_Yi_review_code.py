"""
Homework 9
"""
from tkinter import *

root = Tk()
root.geometry('640x480+200+200')
root.config(bg = '#ddddff')

label1 = Label(root, text='Label 1')
label2 = Label(root, text='Label 2')
label3 = Label(root, text='Label 3')
label4 = Label(root, text='Label 4')
label5 = Label(root, text='Label 5')

# show on screen
# column number is 0 by default
label1.grid(row=2)
label2.grid(column=1)
label3.grid(row=2, column=2)
label4.grid(row=3, column=3, rowspan=2)
label5.grid(row=4, column=4, columnspan=2)

mainloop()