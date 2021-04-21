"""
lable counter 2

optimizing
optimization
optimize

refactor
refactoring

"""


# import tkinter as tk
from tkinter import *


def start_counting(mylabel):
    print("entered start_counting()")

    counter=0

    def counting():
        nonlocal counter
        counter = counter + 1
        mylabel.config(text=str(counter))
        mylabel.after(50, counting)

    counting()


# main program
root = Tk()
root.title('Python GUI - Label counter')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')


# label object
digit_label = Label(root,
              bg = "seagreen",
              fg = 'white',
              height = 3,
              width = 10,
              font = "Helvetic 30 bold")
digit_label.pack()

start_counting(digit_label)

root.mainloop()


