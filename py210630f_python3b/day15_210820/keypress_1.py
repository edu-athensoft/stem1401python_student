"""
KeyPress

binding <Key>
a-z, 0-9, other printable characters (&%^&$^$

event.char

"""

from tkinter import *


def handle_press(event):
    print(f"You have pressed the key of {event.char}")


root = Tk()
root.title("Event Handling")
root.geometry("640x480+300+300")
root.config(bg="#ddddff")

root.bind('<Key>', handle_press)

root.mainloop()
