"""
textvariable

trace()
"""

from tkinter import *


def callbackW(*args):
    print("data changed:", txt.get())


root = Tk()
root.title("Python GUI - Entry")
root.geometry("360x160")

txt = StringVar()

entry = Entry(root, textvariable = txt)
entry.pack()

txt.trace('w', callbackW)

root.mainloop()

