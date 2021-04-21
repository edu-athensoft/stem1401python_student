"""
Tkinter
using grid layout
grid()
rowspan, columnspan
merge cells
"""


from tkinter import *


root = Tk()
root.geometry('320x240+200+200')
root.config(bg='#ddddff')

# create label widgets
label1 = Label(root, text='Label 0,0',bg='yellow')
label2 = Label(root, text='Label 0,1')
label3 = Label(root, text='Label 1,1')

# show on screen
label1.grid(row=0, column=0, columnspan=2)
label2.grid(row=1, column=0)
label3.grid(row=1, column=1)

root.mainloop()