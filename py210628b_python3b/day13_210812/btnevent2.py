"""
Event binding and handling
button
"""

from tkinter import *


def attack(event):
    print('This is a normal attacking action.')
    print(event.x,event.y)


root = Tk()

root.title('Python | Event handling')
root.geometry("640x480+200+200")

btn1 = Button(text='My Btn 2')
btn1.pack()

btn1.bind('<Button-1>',attack)

root.mainloop()