"""
layout - relief
"""

"""
lable1 = Label(root, text='flat',   relief='flat')
lable2 = Label(root, text='groove', relief='groove')
...
label6 = Label(root, text='',       relief='')

x = 'flat'
# mylabel = Label(root, text=x, relief=x)
"""

from tkinter import *


root = Tk()
root.config(bg="#ddddff")

reliefs = ["flat", "groove", "raised","ridge", "solid", "sunken"]

# create 6 labels
for relief in reliefs:
    # mylabel = Label(root, text=relief, relief=relief, font=(40))
    # mylabel.pack(side=LEFT)

    Label(root, text=relief, relief=relief, font=(40)).pack(side=LEFT,padx=10, pady=20)

root.mainloop()




