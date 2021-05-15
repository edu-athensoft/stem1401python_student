"""
layout manager

place(x=a, y=b)

x and y can be both integer and floating number
"""

from tkinter import *

root = Tk()
root.title("Python GUI - Layout place")
root.geometry("640x480+300+300")
root.config(bg="#ddddff")

# label1
label1 = Label(root, text="Label1")
label1.place(x=50.5,y=45.5)

label1b = Label(root, text="Label1")
label1b.place(x=120.5,y=50.9)

# label2
label2 = Label(root, text="Label2")
label2.place(x=310,y=305)


root.mainloop()
