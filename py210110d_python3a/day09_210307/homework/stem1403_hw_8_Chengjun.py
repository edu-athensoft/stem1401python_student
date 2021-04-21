"""
[Homework]
2021-02-28
Show and Hide a label in a window
Due date: By the end of next Sat.
"""
"""
score:
one minor logic defect (-5)

"""

from tkinter import *

def hide(widget):
    return lambda: Pack.forget(widget)


def show(widget):
    return lambda: widget.pack(side=LEFT)


root = Tk()
root.title("Python GUI - Homework")
root.geometry("640x480+0+0")

label1 = Label(root, text='label_A', font=('Time', 20), fg='black', bg="#F0F0EC")
label2 = Label(root, text='Label_B', font=('Time', 20), bg='yellow')
label3 = Label(root, text='Label_C', font=('Time', 20), fg='white', bg='#83b5dd')

label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)

label1.after(2000, hide(label1))

label1.after(2000, show(label1))

root.mainloop()
