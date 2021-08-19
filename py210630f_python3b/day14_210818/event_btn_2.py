"""
Event binding

"""


from tkinter import *


def handler(event):
    print(f"I was Clicked up via bind() at {event.x}, {event.y}")


root = Tk()
root.title("Demo of Button and Click")
root.geometry("640x480+300+300")
root.config(bg="#ddddff")

# command option
label1 = Label(root, text='Scroll me')
label1.pack()

label1.bind('<Button-3>',handler)

root.mainloop()