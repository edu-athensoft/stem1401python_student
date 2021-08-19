"""
KeyPress
a-z, 0-9, other printable characters

event.x
event.y
event.char
event.keycode

"""

from tkinter import *

def press(event):
    print(f"You have pressed the key of {event.char}, keycode: {event.keycode}")

root = Tk()
root.title("Event Handling")
root.geometry("640x480+300+300")
root.config(bg="#ddddff")

# root
root.bind("<Key>", press)

root.mainloop()