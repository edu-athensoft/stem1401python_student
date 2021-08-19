"""
Button and Event handling

Event source
Event - Mouse LMB - Single Click
Event handling
Event binding

"""

from tkinter import *


def handler():
    print("I was clicked.")


root = Tk()
root.title("Demo of Button and Click")
root.geometry("640x480+300+300")
root.config(bg="#ddddff")

# command option
btn1 = Button(root, text='Click me', command=handler)
btn1.pack()

root.mainloop()
