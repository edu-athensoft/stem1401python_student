"""
[Homework]
2021-02-28
Show and Hide a label in a window
Due date: By the end of next Sat.
"""

"""
score:
one fatal syntax error (-10)
one minor logic defect (-5)

"""

from tkinter import *


def hide(label):
    return lambda : Pack.forget(label)


def show(label):
    return lambda : label.pack(side=LEFT)


root = Tk()
root.title("Python GUI - Homework")
root.geometry("640x480+0+0")

label1 = Label(root, text='Label 1', font=('Times', 25), bg="orange", fg='blue')
label2 = Label(root, text='Label 2', font=('Times', 25), bg="orange", fg="red")
label3 = Label(root, text='Label 3', font=('Times', 25), bg="orange", fg='yellow')

label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)

# label1.after(2000, Pack.forget(label1))
# label1.after(2000, label1.pack(side=LEFT))


label1.after(2000, hide(label1))
label1.after(2000, show(label1))
### minor logic error
### fatal syntax error

root.mainloop()