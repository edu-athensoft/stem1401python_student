"""
button

command
changing color

"""
from tkinter import *


def changeColor(bgColor):
    root.config(bg = bgColor)

root = Tk()
root.title("Python GUI - Button")
root.geometry("300x200")

# create 3 buttons
btn_blue = Button(root, text="Blue", command=lambda:changeColor("blue"))
btn_yellow = Button(root, text="Yellow", command=lambda:changeColor("yellow"))
btn_exit = Button(root, text="Exit", command=root.destroy)

btn_yellow.pack(anchor=S, side=RIGHT, padx=5, pady=5)
btn_blue.pack(anchor=S, side=RIGHT, padx=5, pady=5)
btn_exit.pack(anchor=S, side=RIGHT, padx=5, pady=5)

root.mainloop()
