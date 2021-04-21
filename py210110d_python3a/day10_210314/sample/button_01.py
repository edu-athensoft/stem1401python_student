"""
button

command

"""
from tkinter import *


def msgShow():
    label["text"] = "I love tkinter."
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    label.config(text="Python tkinter - Button", bg="lightyellow", fg="blue")


root = Tk()
root.title("Python GUI - Button")

label = Label(root)
btn1 = Button(root, text="Show Message", width=15, command=msgShow)
btn2 = Button(root, text="Exit", width=15, command=root.destroy)
label.pack()

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)

root.mainloop()
