"""
Event binding

"""


from tkinter import *


def handler(event):
    print(f"I was clicked via bind() at {event.x}, {event.y}")


root = Tk()
root.title("Demo of Button and Click")
root.geometry("640x480+300+300")
root.config(bg="#ddddff")

# command option
btn1 = Button(root, text='Click me')
btn1.pack()

btn1.bind('<Button-1>',handler)

root.mainloop()