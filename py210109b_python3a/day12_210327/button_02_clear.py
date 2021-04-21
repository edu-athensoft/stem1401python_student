"""
Button

Challenge
Clear message

1. click to show message
2. click to exit GUI program and close window
3. click to clear message
"""
from tkinter import *


def msgShow():
    label["text"] = "Button Widget"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    # label.config(text="Athensoft Python Course", bg="lightyellow", fg="blue")


def msgClear():
    """
    1.get value of a specified option name using cget()
    2.set value of an option by widget_name['option_name']
    :return:
    """
    # clear message
    label["text"]= ''
    label["bg"] = 'SystemButtonFace'
    # get default bg color
    # colorname = label.cget('bg')
    # print(colorname)


root = Tk()
root.title("Python GUI - Athensoft")

# widget
label = Label(root)
btn1 = Button(root, text="Show Message", width=15, command=msgShow)
btn2 = Button(root, text="Exit", width=15, command=root.destroy)
btn3 = Button(root, text="Clear Message", width=15, command=msgClear)

# layout
label.grid(row=0, column=0, columnspan=2)
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=2)
btn3.grid(row=1, column=1)

root.mainloop()
