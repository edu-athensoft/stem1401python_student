"""
Button
clear content (label)

[] operator

cget('option_name')
"""

from tkinter import *


def show_msg():
    label["text"] = "Button Widget"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"


def clear_msg():
    label["text"] = ""
    print(root.cget('bg'))
    label['bg']='SystemButtonFace'


root = Tk()
root.title("Python GUI - Athensoft")

# widget
label = Label(root)
btn1 = Button(root, text="Show Message", width=15, command=show_msg)
btn2 = Button(root, text="Exit", width=15, command=root.destroy)
btn3 = Button(root, text="Clear Message", width=15, command=clear_msg)

# layout
label.grid(row=0, column=0, columnspan=2)
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=2)
btn3.grid(row=1, column=1)

root.mainloop()
