"""
Mouse Event
<Enter>
<Leave>
Binding multiple event is allowed.
"""

from tkinter import *


def handler_enter(event):
    # print("Entered")
    var.set("Mouse entered")


def handler_leave(event):
    # print("Left")
    var.set("Mouse left")


def handler_b3(event):
    var.set(f"x={event.x},y={event.y}")


root = Tk()
root.title("Event Handling")
root.geometry("640x480+300+300")
# root.config(bg="#ddddff")

var = StringVar()
var.set('Move your mouse to enter and leave the Label')

label1 = Label(root, textvariable=var, font=("Helvetica", 14),
               width=35, height=16, relief='groove', bg="#ddddff")
label1.pack(padx=20, pady=40, anchor=CENTER)

label1.bind("<Enter>", handler_enter)
label1.bind("<Leave>", handler_leave)
label1.bind("<Button-3>", handler_b3)

root.mainloop()
