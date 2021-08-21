"""
mouse event
<Motion>

Move mouse and display current coordinate at the bottom

"""

from tkinter import *


def handler(event):
    # print(f"Mouse moved to {event.x}, {event.y}")
    # print("Mouse moved to {}, {}".format(event.x, event.y))

    x = event.x
    y = event.y

    var.set(f"Mouse cursor is at x={x}, y={y}")


root = Tk()
root.title("Event Handling")
root.geometry("640x480+300+300")
root.config(bg="#ddddff")

root.bind("<Motion>", handler)

var = StringVar()
x = 0
y = 0
var.set(f"Mouse cursor is at x={x}, y={y}")
label1 = Label(root, textvariable=var, font=(None, 16))
label1.pack(anchor=S, side=RIGHT, padx=10, pady=10)

root.mainloop()
