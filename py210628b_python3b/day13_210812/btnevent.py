"""
Event binding and handling
button
"""

from tkinter import *


def attack():
    print('This is a normal attacking action.')


root = Tk()

root.title('Python | Event handling')
root.geometry("640x480+200+200")

btn1 = Button(text='My Btn', command=attack)
btn1.pack()

root.mainloop()