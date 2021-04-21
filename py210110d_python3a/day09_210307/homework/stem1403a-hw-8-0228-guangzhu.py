"""
[Homework]
2021-02-28
Show and Hide a label in a window.
"""

"""
score:
one minor logic missing (-5)
hide and show (missing show-function)

improper char in file name (-1)

"""

from tkinter import *


def hidelabel(widget):
    return lambda: Pack.forget(widget)


root = Tk()
root.geometry('640x480+0+0')
root.config(bg='#ddddff')

#
label1 = Label(root, text='Python')
label2 = Label(root, text='Java',bg='yellow', font=(40))
label3 = Label(root, text='Web')
label4 = Label(root, text='Database',bg='yellow', font=(40))

#
label4.pack()
label1.pack()
label2.pack()
label3.pack()

# hide label1 after 3 seconds
label1.after(3000, hidelabel(label1))


root.mainloop()
